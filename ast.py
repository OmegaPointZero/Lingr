import lexer
import argparse
import re

class AST:
    def __init__(self, token_list):
        self.token_list = token_list
        self.self = self
        self.leaf_count = 0
        self.making_leaf = False
        self.leaves = []
        self.count = 0
    def tokeneval(self,token,ttype,value):
        self.self = self
        if token['TYPE'] == ttype and token['TOKEN'] == value:
            return True
        else:
            return False

    # Parse for parenthesis and exponents, return an object
    def pe(self, tokens):
        nested_expressions = [[]] 
        resolvables = 0
        layers = [0]
        for token in tokens:

            if self.tokeneval(token,'IDENTIFIER','(') == True:
                nested_expressions.append([])
                resolvables += 1
                nested_expressions[layers[-1]].append({'TYPE' : 'RESOLVABLE', 'TOKEN': 'RESOLVABLE'+str(resolvables)})
                layers.append(resolvables)
                nested_expressions[layers[-1]].append({'TYPE' : 'META', 'SUBTYPE': 'START', 'TOKEN': 'RESOLVABLE'+str(layers[-1])})

            elif self.tokeneval(token,'IDENTIFIER',')'):
                nested_expressions[layers[-1]].append({'TYPE': 'META', 'SUBTYPE' : 'END', 'TOKEN': 'RESOLVABLE'+str(layers[-1])})
                layers.pop()

            else:
                nested_expressions[layers[-1]].append(token)

        nested_expressions.reverse()
        return nested_expressions

    def evalleaf(self, sentence, operators):
        token = sentence[self.count]
        operator = sentence[self.count+1]
        third = sentence[self.count+2]
        for ops in operators:
            if self.tokeneval(operator,'OPERATOR',ops) == True:
                if self.making_leaf == False:
                    self.making_leaf = True
                    self.leaves += [[token]]
                    self.count += 2
                self.leaves[self.leaf_count] += [operator, third]
                print('Leaves so far: %s' % self.leaves)


    def leafy(self, sentences, parsetype):
        operators = []
        if parsetype == 'multdiv':
            operators = ['*','/']
        elif parsetype == 'exponent':
            operators = ['**']
        elif parsetype == 'addsub':
            operators = ['+', '-']

        for sentence in sentences:
            print('[*] +-- SENTENCE: %s' % sentence)
            length = len(sentence)
            self.count = 0
            while(self.count < length-2):
                self.making_leaf = False
                self.evalleaf(sentence, operators)
                while self.making_leaf == True and self.count < length-2:
                    self.evalleaf(sentence, operators)
                    self.count += 2
                self.count += 1
        return sentences

    def generate_tree(self):
        self.self = self
        tokens = self.token_list
        first_iteration = self.pe(tokens)
        second_iteration = self.leafy(first_iteration, "multdiv")

        for expression in second_iteration: 
            """print(expression)"""
        return second_iteration

ast = AST(lexer.main(argparse.Namespace(file_path='test.lr', printast=True, printlex=False, standalone=False)))

ast.generate_tree()


