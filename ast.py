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
        resolvables = [] 
        resolvable_count = 0 
        current_count = 0
        resolvable_nest = []
        for token in tokens: 
            print('token: %s' % token)
            phrase = expressions(exp).lookup_phrase()
            if phrase == None:
                print('No Phrase!')
                if self.tokeneval(token,'IDENTIFIER',';'): 
                    print('Abstract Syntax Table ERROR: %s\nNO SUCH EXPRESSION FOUND' % exp)
                    exp = []
                    break
                elif self.tokeneval(token,'IDENTIFIER','(') == True:
                    exp.append({'TYPE' : 'RESOLVABLE', 'TOKEN' : 'RESOLVABLE'+str(resolvable_count)})
                    resolvable_nest.append(resolvable_count)
                    resolvable_count += 1
                    current_count += 1
                elif self.tokeneval(token,'IDENTIFIER',')') == True:
                    exp.append({'TYPE': 'RESOLVABLE', 'TOKEN' : 'END'+str(resolvable_nest[current_count])}) 
                    current_count -= 1
                    resolvable_nest.pop()
                else:
                    exp.append(token)
            elif re.match('/^RESOLVABLE/', phrase.split(' ')[-1]):
                """ writing an AST and lexer is really,  really hard """
            else:
                print('phrase: %s' % phrase)
                if self.tokeneval(token,'IDENTIFIER',';'): 
                    if(exp == []):
                        print('End of line detected')
                    else:
                        tree = tree + exp
                        exp = []
        print(tree)
        return tree

ast = AST(lexer.main(argparse.Namespace(file_path='test.lr', printast=True, printlex=False, standalone=False)))

ast.generate_tree()


