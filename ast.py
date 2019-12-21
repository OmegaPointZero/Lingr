import lexer
import argparse

class AST:
    def __init__(self, token_list):
        self.token_list = token_list
        self.self = self

    def generate_tree(self):
        self.self = self
        print('Number of things to interpret: %s' % len(self.token_list))
        print(self.token_list)

class expressions:
    def __init__(self, phrase):
        self.phrase = phrase
        self.self = self
    
    def lookup_phrase(self,phrase):
        print(phrase)

ast = AST(lexer.main(argparse.Namespace(file_path='test.lr', printast=True, printlex=False, standalone=False)))

ast.generate_tree()
