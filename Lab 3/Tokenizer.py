import re
import sys

class Singleton:
        'Singleton class to ensure only one tokenizer'
        instance = None
        num = 0        
        
        def Instance(self):
                if (Singleton.instance == None):
                        Singleton.instance = Tokenizer()
                        Singleton.num += 1
                        print Singleton.num
                        return Singleton.instance
                else:
                        Singleton.num += 1
                        print "NUM2 = " + str(Singleton.num)
                        return Singleton.instance

class Program:
        'Program class that parses, prints and executes core programs'
        
class ID:
        'Identifier class'
        
        id_array = []
        id_count = 0    
        
        def __init__(self, name):
                self.__name = name
                self.value = None
                self.initalized = False
                
        def get_Id_name(self):
                return self.__name
       
        '''
        Function overloads == operator to be able to compare tokens and ID's 
        based on name. self is the id objects and other is the token
        
        '''
        def __eq__(self, other):
                return self.__name == other
        
        @staticmethod
        def parse_id():
                t = Singleton().Instance()
                print t.get_token()
                if t.get_token() in ID.id_array:
                        print "ID in id_array"
                        return ID.id_array[ID.id_array.index(t.get_token())]
                else:
                        new_id = ID(t.get_token())
                        ID.id_array.extend([new_id])
                        ID.id_count += 1
                        print "ID not in id_array"
                        return new_id
        
        def get_Id_value(self):
                return self.value
        
        def set_Id_value(self, value):
                self.value = value
        
                
        
class Tokenizer:
        'Tokenizer that generates tokens from a list of strings'
        
        def __init__(self):
                #self.current_token = ""
                self.all_tokens = []
                self.position = 0;
        
        def skip_token(self):
                self.position += 1
                
        def get_token(self):
                print 
                return self.all_tokens[self.position]       
                
        
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
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'begin':
                        print BEGIN
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'end':
                        print END
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'int':
                        print INT
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'if':
                        print IF
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'then':
                        print THEN
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'else':
                        print ELSE
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'while':
                        print WHILE
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'loop':
                        print LOOP
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'read':
                        print READ
                        tokenizer.all_tokens.extend([lower.group()])
                
                elif lower.group() == 'write':
                        print WRITE
                        tokenizer.all_tokens.extend([lower.group()])
                
                else:
                        quit("Error with token " + str(token)) 
                
        elif equals:
                if equals.group() == '=':
                        print EQUALS 
                        tokenizer.all_tokens.extend([equals.group()])
                else:
                        print DOUBLE_EQUALS
                        tokenizer.all_tokens.extend([equals.group()])
                                 
        elif ID :
                print IDENTIFIER
                tokenizer.all_tokens.extend([ID.group()])
            
        elif number :
                print NUMBER
                tokenizer.all_tokens.extend([number.group()])
           
        elif semicolon:
                print SEMICOLON
                tokenizer.all_tokens.extend([semicolon.group()])
                
        elif cond_or:
                print OR
                tokenizer.all_tokens.extend([cond_or.group()])
        
        elif comma:
                print COMMA
                tokenizer.all_tokens.extend([comma.group()])
                
        elif not_equal:
                print NOT_EQUAL
                tokenizer.all_tokens.extend([not_equal.group()])
        
        elif explanation_mark:
                print EXPLANATION_MARK
                tokenizer.all_tokens.extend([explanation_mark.group()])

        elif left_bracket:
                print LEFT_BRACKET
                tokenizer.all_tokens.extend([left_bracket.group()])
                
        elif right_bracket:
                print RIGHT_BRACKET
                tokenizer.all_tokens.extend([right_bracket.group()])
                
        elif and_percent:
                print AND_PERCENT
                tokenizer.all_tokens.extend([and_percent.group()])
        
        elif left_paren:
                print LEFT_PAREN
                tokenizer.all_tokens.extend([left_paren.group()])
                
        elif right_paren:
                print RIGHT_PAREN
                tokenizer.all_tokens.extend([right_paren.group()])
        
        elif plus:
                print PLUS
                tokenizer.all_tokens.extend([plus.group()])
                
        elif minus:
                print MINUS
                tokenizer.all_tokens.extend([minus.group()])
        
        elif times:
                print TIMES
                tokenizer.all_tokens.extend([times.group()])
                
        elif less_than:
                print LESS_THAN
                tokenizer.all_tokens.extend([less_than.group()])
                
        elif greater_than:
                print GREATER_THAN
                tokenizer.all_tokens.extend([greater_than.group()])
        
        elif less_than_equal:
                print LESS_THAN_EQUAL
                tokenizer.all_tokens.extend([less_than_equal.group()])
                
        elif greater_than_equal:
                print GREATER_THAN_EQUAL
                tokenizer.all_tokens.extend([greater_than_equal.group()])

# Separates tokens that are concatonated together                       
def check_multi_token(token, list):
        
        if len(token[len(list.group()) :]) != 0 and len(list.group()) !=0:      
                t = token[len(list.group()):]
                tokenizer.current_token = list.group()
                tokenizer.generate_tokens(t)        

# Checks if the current token is valid
def check_legal_token(token, list):
        special_char = re.compile(';|=|\||,|!|\[|\]|&|\(|\)|\+|-|\*|!=|<|>')
        
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
        
        #if len(sys.argv) != 2:
        #        quit("Usage progam_name data_file ")
        
        #fname = sys.argv[1]
        #data = read_file(fname)
        data = "ABCD1234 ABC THE CAT ABC ABC 12;"
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
        #tokenizer = Tokenizer()
        tokenizer = Singleton().Instance()
        
        for token in range(len(tokens)):
                tokenizer.generate_tokens(tokens[token])
        
        # Testing get_token() and skip_token()        
        #for t in range(len(tokenizer.all_tokens)):
        #        print "TOKEN = " + str(tokenizer.get_token())
        #        
        #        tokenizer.skip_token()
        
        print EOF
        
        Id = ID("HELLO")
        print Id.get_Id_name()
        
        Id2 = ID("WORLD")
        Id3 = ID("HELLO")
        
        t = Singleton().Instance()
        ID.parse_id()
        t.skip_token()
        ID.parse_id()
        t.skip_token()
        ID.parse_id()
        t.skip_token()    
        ID.parse_id()
        t.skip_token()   
        ID.parse_id()
        t.skip_token() 
        ID.parse_id()
        t.skip_token()        
        #ID.parse_id()
        #ID.parse_id()        

        

        
        