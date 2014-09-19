import re

# Prints a list, each item in the list on a seperate line 
def print_tokens(tokens):
        for token in tokens:
                print token

# Decodes the tokens from strings to ints
def decode_tokens():
        for tokens in all_tokens:
                lower = lowercase.match(tokens)
                ID = identifier.match(tokens)
                number = integers.match(tokens)
                equals = equal.match(tokens) 
                semicolon = semi.match(tokens)
                cond_or = cond.match(tokens)
                
                if lower:
                        decoded_tokens.append(1)
                        
                elif equals:
                        if equals.group() == '=':
                                decoded_tokens.append(14)                
                        else:
                                decoded_tokens.append(26)
                                         
                elif ID :
                        decoded_tokens.append(32)
                    
                elif number :
                        decoded_tokens.append(31)                
                   
                elif semicolon:
                        decoded_tokens.append(12)
                        
                elif cond_or:
                        decoded_tokens.append(19)
 
# Separates tokens that are concatonated together                       
def check_multi_token(token, list):
        if len(token[len(list.group()) :]) != 0 and len(list.group()) !=0:
                t = token[len(list.group()):]
                generate_tokens(t)        

# Generates a list of tokens from a list of strings
def generate_tokens(tokens):
        lower = lowercase.match(tokens)
        ID = identifier.match(tokens)
        number = integers.match(tokens)
        equals = equal.match(tokens) 
        semicolon = semi.match(tokens)
        cond_or = cond.match(tokens)
        
        if lower:
                print "LOWER CASE = " + lower.group()
                all_tokens.append(lower.group())
                check_multi_token(tokens, lower)
                
        elif equals:

                print "EQUALS " + equals.group()
                all_tokens.append(equals.group())                
                check_multi_token(tokens, equals)
                
        elif ID :
                print "ID = " + str(ID.group())
                all_tokens.append(ID.group())                
                check_multi_token(tokens, ID)          
            
        elif number :
                print "NUM = " + number.group()
                all_tokens.append(number.group())                
                check_multi_token(tokens, number)
           
        elif semicolon:
                print "SEMI = " + str(semicolon.group())
                all_tokens.append(semicolon.group())
                check_multi_token(tokens, semicolon)
        
        elif cond_or:
                print "OR = " + str(cond_or.group())
                all_tokens.append(cond_or.group())                
                print str(cond_or.group()) == '||'
                check_multi_token(tokens, cond_or)
       
        else:
                print "Error with " + tokens   

remove_spaces = re.compile('\S+')
tokens = remove_spaces.findall("program int X; begin X===328XY74||")#"program int X; begin X===328;XY74||")#"===328")#AAA;;;AA")#"ABC123;;;AA")#"===328")#"program 345;;")# hello time KDKDKD JFJFJ55 J4J4 0012 0ab 00AB =====")

# Regex's
lowercase = re.compile('[a-z]+')
identifier = re.compile('[A-Z]+[0-9]*')
integers = re.compile('[0-9]+')#[^a-zA-Z]')
equal = re.compile('==|=')
semi = re.compile(';')
cond = re.compile('[|]{2}')

all_tokens = []
decoded_tokens = []

print tokens

for token in range(len(tokens)):
        generate_tokens(tokens[token])
        
print all_tokens
decode_tokens()
print_tokens(decoded_tokens)