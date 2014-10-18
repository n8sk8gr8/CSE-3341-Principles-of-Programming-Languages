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
                comma = comm.match(tokens)
                explanation_mark = expl.match(tokens)
                left_bracket = left_brack.match(tokens)
                right_bracket = right_brack.match(tokens)
                and_percent = and_per.match(tokens)
                left_paren = left_par.match(tokens)
                right_paren = right_par.match(tokens)
                plus = add.match(tokens)
                minus = sub.match(tokens)
                times = mult.match(tokens)
                not_equal = not_eq.match(tokens)
                less_than = less.match(tokens)
                greater_than = greater.match(tokens)
                less_than_equal = less_than_eq.match(tokens)
                greater_than_equal = greater_than_eq.match(tokens) 
                
                
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
                                          
                elif comma:
                        check_legal_token(tokens, comma)
                        decode_token(comma.group())
                        check_multi_token(tokens, comma)
                        
                elif not_equal:
                        check_legal_token(tokens, not_equal)
                        decode_token(not_equal.group())
                        check_multi_token(tokens, not_equal) 
                        
                elif explanation_mark:
                        check_legal_token(tokens, explanation_mark)
                        decode_token(explanation_mark.group())
                        check_multi_token(tokens, explanation_mark)  
                        
                elif left_bracket:
                        check_legal_token(tokens, left_bracket)
                        decode_token(left_bracket.group())
                        check_multi_token(tokens, left_bracket)  
                        
                elif right_bracket:
                        check_legal_token(tokens, right_bracket)
                        decode_token(right_bracket.group())
                        check_multi_token(tokens, right_bracket) 
                        
                elif and_percent:
                        check_legal_token(tokens, and_percent)
                        decode_token(and_percent.group())
                        check_multi_token(tokens, and_percent)  
                        
                elif left_paren:
                        check_legal_token(tokens, left_paren)
                        decode_token(left_paren.group())
                        check_multi_token(tokens, left_paren)
                        
                elif right_paren:
                        check_legal_token(tokens, right_paren)
                        decode_token(right_paren.group())
                        check_multi_token(tokens, right_paren) 
                        
                elif plus:
                        check_legal_token(tokens, plus)
                        decode_token(plus.group())
                        check_multi_token(tokens, plus) 
                        
                elif minus:
                        check_legal_token(tokens, minus)
                        decode_token(minus.group())
                        check_multi_token(tokens, minus)
                        
                elif times:
                        check_legal_token(tokens, times)
                        decode_token(times.group())
                        check_multi_token(tokens, times)   
                        
                elif less_than:
                        check_legal_token(tokens, less_than)
                        decode_token(less_than.group())
                        check_multi_token(tokens, less_than)
                        
                elif greater_than:
                        check_legal_token(tokens, greater_than)
                        decode_token(greater_than.group())
                        check_multi_token(tokens, greater_than) 
                        
                elif less_than_equal:
                        check_legal_token(tokens, less_than_equal)
                        decode_token(less_than_equal.group())
                        check_multi_token(tokens, less_than_equal)  
                        
                elif greater_than_equal:
                        check_legal_token(tokens, greater_than_equal)
                        decode_token(greater_than_equal.group())
                        check_multi_token(tokens, greater_than_equal)               
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
        comma = comm.match(token)
        explanation_mark = expl.match(token)
        left_bracket = left_brack.match(token)
        right_bracket = right_brack.match(token)
        and_percent = and_per.match(token)
        left_paren = left_par.match(token)
        right_paren = right_par.match(token)
        plus = add.match(token)
        minus = sub.match(token)
        times = mult.match(token)
        not_equal = not_eq.match(token)
        less_than = less.match(token)
        greater_than = greater.match(token)
        less_than_equal = less_than_eq.match(token)
        greater_than_equal = greater_than_eq.match(token)       
        
        PROGRAM = 1
        BEGIN = 2
        END = 3
        INT = 4
        IF = 5
        THEN = 6
        ELSE = 7
        WHILE = 8
        LOOP = 9
        READ = 10
        WRITE = 11
        EQUALS = 14
        DOUBLE_EQUALS = 26
        IDENTIFIER = 32
        NUMBER = 31
        SEMICOLON = 12
        OR = 19
        COMMA = 13
        EXPLANATION_MARK = 15
        LEFT_BRACKET = 16
        RIGHT_BRACKET = 17
        AND_PERCENT = 18
        LEFT_PAREN = 20
        RIGHT_PAREN = 21
        PLUS = 22
        MINUS = 23
        TIMES = 24
        NOT_EQUAL = 25
        LESS_THAN = 27
        GREATER_THAN = 28
        LESS_THAN_EQUAL = 29
        GREATER_THAN_EQUAL = 30
        
        if lower:
                if lower.group() == 'program':
                        print PROGRAM
                
                elif lower.group() == 'begin':
                        print BEGIN
                
                elif lower.group() == 'end':
                        print END
                
                elif lower.group() == 'int':
                        print INT
                
                elif lower.group() == 'if':
                        print IF
                
                elif lower.group() == 'then':
                        print THEN
                
                elif lower.group() == 'else':
                        print ELSE
                
                elif lower.group() == 'while':
                        print WHILE
                
                elif lower.group() == 'loop':
                        print LOOP
                
                elif lower.group() == 'read':
                        print READ
                
                elif lower.group() == 'write':
                        print WRITE
                
                else:
                        quit("Error with token " + str(token)) 
                
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
        
        elif comma:
                print COMMA
                
        elif not_equal:
                print NOT_EQUAL
        
        elif explanation_mark:
                print EXPLANATION_MARK

        elif left_bracket:
                print LEFT_BRACKET
                
        elif right_bracket:
                print RIGHT_BRACKET
                
        elif and_percent:
                print AND_PERCENT
        
        elif left_paren:
                print LEFT_PAREN
                
        elif right_paren:
                print RIGHT_PAREN
        
        elif plus:
                print PLUS
                
        elif minus:
                print MINUS
        
        elif times:
                print TIMES
                
        elif less_than:
                print LESS_THAN
                
        elif greater_than:
                print GREATER_THAN
        
        elif less_than_equal:
                print LESS_THAN_EQUAL
                
        elif greater_than_equal:
                print GREATER_THAN_EQUAL

# Separates tokens that are concatonated together                       
def check_multi_token(token, list):
        
        if len(token[len(list.group()) :]) != 0 and len(list.group()) !=0:      
                t = token[len(list.group()):]
                tokenizer.generate_tokens(t)        

# Checks if the current token is valid
def check_legal_token(token, list):
        special_char = re.compile(';|=|\||,|!|\[|\]|&|\(|\)|\+|-|\*|!=|<|>|') 
        if len(token[len(list.group()) :]) != 0 and len(list.group()) !=0:
                special_token = special_char.match(token[len(list.group())])
                special_list = special_char.match(list.group())

                if not (special_token or special_list):
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
        integers = re.compile('[0-9]+')
        equal = re.compile('==|=')
        semi = re.compile(';')
        cond = re.compile('[|]{2}')
        comm = re.compile(',')
        expl = re.compile('!')
        left_brack = re.compile('\[')
        right_brack = re.compile('\]')
        and_per = re.compile('[&]{2}')
        left_par = re.compile('\(')
        right_par = re.compile('\)')
        add = re.compile('\+')
        sub = re.compile('-')
        mult = re.compile('\*')
        not_eq = re.compile('!=')
        less = re.compile('<')
        greater = re.compile('>')
        less_than_eq = re.compile('<=')
        greater_than_eq = re.compile('>=')
        EOF = 33
        
        # Create tokenizer object        
        tokenizer = Tokenizer()
        
        for token in range(len(tokens)):
                tokenizer.generate_tokens(tokens[token])
        
        
        print EOF
        