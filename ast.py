import lexer
import argparse

class expressions:
    def __init__(self, phrase):
        self.phrase = phrase
        self.self = self

    def add(self):
        self.self = self
        phrase = self.phrase
        print('working phrase: %s' % phrase)
        addable = ['INT', 'STRING', 'FLOAT', 'ARRAY']
        first = phrase[0]
        operator = phrase[1]
        second = phrase[2]
        if(first['TYPE'] in addable and second['TYPE'] in addable):
            return "ADD "+first['TOKEN']+" "+second['TOKEN']
        elif(first['TYPE'] in addable and second['TYPE'] == 'RESOLVABLE'):
            return "ADD "+first['TOKEN']+" RESOLVABLE "
        else: return None

 

    def lookup_phrase(self):
        self.self = self
        print(self.phrase)
        add = self.add()

        return add 

class AST:
    def __init__(self, token_list):
        self.token_list = token_list
        self.self = self

    def tokeneval(self,token,ttype,value):
        self.self = self
        if token['TYPE'] == ttype and token['TOKEN'] == value:
            return True
        else:
            return False

    def generate_tree(self):
        self.self = self
        tokens = self.token_list
        tree = []
        exp = [] # expression being built
        nested = [] # things contained within parenthesis
        nesting = 0 # how far nested we are right now
        n_count = 0 # the number of nested items
        for token in tokens:
            if(len(exp)>2):
                phrase = expressions(exp).lookup_phrase()
                print('HERE IS THE PHRASE!! ######### LOOK HERE #########')
                print(phrase)
                if self.tokeneval(token,'IDENTIFIER',';'): 
                    print('End of line detected')
                    if phrase == None:
                        print('Abstract Syntax Table ERROR: %s\nNO SUCH EXPRESSION FOUND' % exp)
                        exp = []
                        break
                    else:
                        tree = tree + exp
                        exp = []
                if self.tokeneval(token,'IDENTIFIER','(') == True:
                    exp.append({'TYPE' : 'RESOLVABLE', 'TOKEN' : 'RESOLVABLE'+str(nesting)})
                    nesting += 1 
                    n_count += 1
                    nested.insert(0,exp)
                elif self.tokeneval(token,'IDENTIFIER',')') == True:
                    print("FOUND A CLOSING BRACKET!")
                else:
                    exp.append(token)
            else:
                exp.append(token) 

        return tree

ast = AST(lexer.main(argparse.Namespace(file_path='test.lr', printast=True, printlex=False, standalone=False)))

ast.generate_tree()


