import lexer
import argparse
import re


class expressions:
    def __init__(self, phrase):
        self.phrase = phrase
        self.self = self

    def add(self):
        self.self = self
        phrase = self.phrase

        addable = ['INT', 'STRING', 'FLOAT', 'ARRAY']
        if len(phrase) == 0 or len(phrase) == 1 or len(phrase) == 2:
            return None
        elif len(phrase) == 3:
            first = phrase[0]
            operator = phrase[1]
            second = phrase[2]
            if(first['TYPE'] in addable and second['TYPE'] in addable):
                return "ADD "+first['TOKEN']+" "+second['TOKEN']
            elif(first['TYPE'] in addable and second['TYPE'] == 'RESOLVABLE'):
                return "ADD "+first['TOKEN']+" RESOLVABLE "+second['TOKEN']
            else: return None
        else: 
            return None
 

    def lookup_phrase(self):
        self.self = self
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

    # Parse for parenthesis and exponents, return an object
    def pe(self, tokens):
        # int 9 + (9 + (18)) + ( 4 + 1 )
        nested_expressions = [[]] # an array of arrays
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

    def generate_tree(self):
        self.self = self
        tokens = self.token_list
        first_iteration = self.pe(tokens)

        for expression in first_iteration: 
            print(expression)
        return first_iteration

ast = AST(lexer.main(argparse.Namespace(file_path='test2.lr', printast=True, printlex=False, standalone=False)))

ast.generate_tree()


