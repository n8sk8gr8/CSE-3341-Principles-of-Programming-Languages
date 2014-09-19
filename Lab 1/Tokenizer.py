import re
#import sys

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
 
# Decode a single token and print the corresponding int value
def decode_token(token):
        lower = lowercase.match(token)
        ID = identifier.match(token)
        number = integers.match(token)
        equals = equal.match(token) 
        semicolon = semi.match(token)
        cond_or = cond.match(token)
        
        if lower:
                decoded_tokens.append(1)
                
        elif equals:
                if equals.group() == '=':
                        print 14                 
                else:
                        print 26
                                 
        elif ID :
                print 32
            
        elif number :
                print 31               
           
        elif semicolon:
                print 12
                
        elif cond_or:
                print 19

# Separates tokens that are concatonated together                       
def check_multi_token(token, list):
        #special_char = re.compile(';|=|\|')
        
        if len(token[len(list.group()) :]) != 0 and len(list.group()) !=0:      
                t = token[len(list.group()):]
                generate_tokens(t)        

# Checks if the current token is valid
def check_legal_token(token, list):
        special_char = re.compile(';|=|\|') 
                
        if len(token[len(list.group()) :]) != 0 and len(list.group()) !=0:
                special_token = special_char.match(token[len(list.group())])
                special_list = special_char.match(list.group())

                if not (special_token or special_list):
                        #raise Exception("Error with token " + str(token))
                        print "Error with token " + str(token)
                        quit("Error with token " + str(token))        


# Generates a list of tokens from a list of strings
def generate_tokens(tokens):
        lower = lowercase.match(tokens)
        ID = identifier.match(tokens)
        number = integers.match(tokens)
        equals = equal.match(tokens) 
        semicolon = semi.match(tokens)
        cond_or = cond.match(tokens)
        
        if lower:
                check_legal_token(tokens, lower)
                print lower.group()
                decode_token(lower.group())
                all_tokens.append(lower.group())
                check_multi_token(tokens, lower)
                
        elif equals:
                check_legal_token(tokens, equals)
                print equals.group()
                decode_token(equals.group())
                all_tokens.append(equals.group())                
                check_multi_token(tokens, equals)
                
        elif ID :
                check_legal_token(tokens, ID)
                print ID.group()
                decode_token(ID.group())
                all_tokens.append(ID.group())                
                check_multi_token(tokens, ID)          
            
        elif number :
                check_legal_token(tokens, number)
                print number.group()
                decode_token(number.group())
                all_tokens.append(number.group())                
                check_multi_token(tokens, number)
           
        elif semicolon:
                check_legal_token(tokens, semicolon)
                print semicolon.group()
                decode_token(semicolon.group())
                all_tokens.append(semicolon.group())
                check_multi_token(tokens, semicolon)
        
        elif cond_or:
                check_legal_token(token, cond_or.group())
                print cond_or.group()
                decode_token(cond_or.group())
                all_tokens.append(cond_or.group())                
                #print str(cond_or.group()) == '||'
                check_multi_token(tokens, cond_or)
       
        else:
                quit("Error with token " + str(tokens))

remove_spaces = re.compile('\S+')
tokens = remove_spaces.findall(";%this")#";|this remainder doesn't matter")#";xyXY")#";;XYxy this remainder doesn't matter")#"||xy74 this remainder doesn't matter")#"===XY74Z this remainder doesn't matter")#"program int X; begin X===328XY74||")

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