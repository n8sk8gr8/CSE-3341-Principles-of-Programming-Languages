import re
import sys

class Tokenizer:
        'Tokenizer that generates tokens from a list of strings'
        
        # Generates a list of tokens from a string
        def generate_tokens(self, tokens):
                lower = lowercase.match(tokens)
                ID = identifier.match(tokens)
                number = integers.match(tokens)
                equals = equal.match(tokens) 
                semicolon = semi.match(tokens)
                cond_or = cond.match(tokens)
                
                if lower:
                        check_legal_token(tokens, lower)
                        decode_token(lower.group())
                        check_multi_token(tokens, lower)
                        
                elif equals:
                        check_legal_token(tokens, equals)
                        decode_token(equals.group())
                        check_multi_token(tokens, equals)
                        
                elif ID :
                        check_legal_token(tokens, ID)
                        decode_token(ID.group())
                        check_multi_token(tokens, ID)          
                    
                elif number :
                        check_legal_token(tokens, number)
                        decode_token(number.group())
                        check_multi_token(tokens, number)
                   
                elif semicolon:
                        check_legal_token(tokens, semicolon)
                        decode_token(semicolon.group())
                        check_multi_token(tokens, semicolon)
                
                elif cond_or:
                        check_legal_token(tokens, cond_or)
                        decode_token(cond_or.group())
                        check_multi_token(tokens, cond_or)
               
                else:
                        quit("Error with token " + str(tokens))        
                

# Prints a list, each item in the list on a seperate line 
def print_tokens(tokens):
        for token in tokens:
                print token


# Decode a single token and print the corresponding int value
def decode_token(token):
        
        lower = lowercase.match(token)
        ID = identifier.match(token)
        number = integers.match(token)
        equals = equal.match(token) 
        semicolon = semi.match(token)
        cond_or = cond.match(token)
        
        LOWERCASE = 1
        EQUALS = 14
        DOUBLE_EQUALS = 26
        IDENTIFIER = 32
        NUMBER = 31
        SEMICOLON = 12
        OR = 19
        
        if lower:
                print LOWERCASE
                
        elif equals:
                if equals.group() == '=':
                        print EQUALS                
                else:
                        print DOUBLE_EQUALS
                                 
        elif ID :
                print IDENTIFIER
            
        elif number :
                print NUMBER              
           
        elif semicolon:
                print SEMICOLON
                
        elif cond_or:
                print OR

# Separates tokens that are concatonated together                       
def check_multi_token(token, list):
        
        if len(token[len(list.group()) :]) != 0 and len(list.group()) !=0:      
                t = token[len(list.group()):]
                tokenizer.generate_tokens(t)        

# Checks if the current token is valid
def check_legal_token(token, list):
        special_char = re.compile(';|=|\|') 
                
        if len(token[len(list.group()) :]) != 0 and len(list.group()) !=0:
                special_token = special_char.match(token[len(list.group())])
                special_list = special_char.match(list.group())

                if not (special_token or special_list):
                        #raise Exception("Error with token " + str(token))
                        #print "Error with token " + str(token)
                        quit("Error with token " + str(token))        


# Read data from file into a string
def read_file(filename):
        f = open(filename)
        filedata = f.read()
        return filedata


# Main method
if __name__ == "__main__":
        remove_spaces = re.compile('\S+')
        
        if len(sys.argv) != 2:
                quit("Usage progam_name data_file ")
        
        fname = sys.argv[1]
                     
        data = read_file(fname)
        tokens = remove_spaces.findall(data)
        
        # Regex's
        lowercase = re.compile('[a-z]+')
        identifier = re.compile('[A-Z]+[0-9]*')
        integers = re.compile('[0-9]+')#[^a-zA-Z]')
        equal = re.compile('==|=')
        semi = re.compile(';')
        cond = re.compile('[|]{2}')
                
        # Create tokenizer object        
        tokenizer = Tokenizer()
        
        for token in range(len(tokens)):
                tokenizer.generate_tokens(tokens[token])
        