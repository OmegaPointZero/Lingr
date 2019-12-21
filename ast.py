import lexer
import argparse

class expressions:
    def __init__(self, phrase):
        self.phrase = phrase
        self.self = self

    def add(self):
        self.self = self
        phrase = self.phrase

        addable = ['INT', 'STRING', 'FLOAT', 'ARRAY']
        first = phrase[0]
        operator = phrase[1]
        second = phrase[2]
        if(first['TYPE'] in addable and second['TYPE'] in addable):
            return "ADD "+first['TOKEN']+" "+second['TOKEN']
        else: return None

    def lookup_phrase(self):
        self.self = self
        print(self.phrase)
        return(self.add())

class AST:
    def __init__(self, token_list):
        self.token_list = token_list
        self.self = self

    def generate_tree(self):
        self.self = self
        tokens = self.token_list
        tree = []
        exp = []
        for token in tokens:
            if(len(exp)>2):
                phr = expressions(exp).lookup_phrase()
                if token['TYPE'] == 'IDENTIFIER' and token['TOKEN'] == ';': 
                    if phr == None:
                        print('Abstract Syntax Table ERROR: %s\n\nNO SUCH EXPRESSION FOUND' % exp)
                        exp = []
                        break
                    else:
                        tree = tree + exp
                        exp = []
                else:
                    exp.append(token)
            else:
                exp.append(token)
        return tree

ast = AST(lexer.main(argparse.Namespace(file_path='test.lr', printast=True, printlex=False, standalone=False)))

ast.generate_tree()
