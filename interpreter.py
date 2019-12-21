import ast
import lexer

class expressions:
    def __init__(self):
        self.self = self
    
    def plus(first,second):
        strings = False

        def parseplus(item):
            if item['TYPE'] == 'INT':
                z = int(first['TOKEN'])

        if first['TYPE'] == 'INT':
            f = int(first['TOKEN'])
        elif first['TYPE'] == 'STRING':
            f = first['TOKEN']
            strings = True

        if second['TYPE'] == 'INT':
            s = int(second['TOKEN'])
        elif second['TYPE'] == 'STRING':
            s = second['TOKEN']
            strings = True

        if not strings:
            return f + s

        elif strings:
            return str(f) + str(s)

class interpreter:
    def __init__(self, abstractSyntaxTree):
        self.self = self
        self.AbstractSyntaxTree = abstractSyntaxTree

    
