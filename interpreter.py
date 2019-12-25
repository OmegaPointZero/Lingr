import ast
import lexer

class expressions:
    def __init__(self):
        self.self = self
    
    def plus(first,second):
        strings = False

        def parseplus(item):
            if item['TYPE'] == 'INT':
                z = int(item['TOKEN'])
            elif item['TYPE'] == 'STRING':
                z = item['TOKEN']
                strings = True
            return z

        f = parseplus(first)
        s = parseplus(second)

        if not strings:
            return f + s

        elif strings:
            return str(f) + str(s)

class interpreter:
    def __init__(self, abstractSyntaxTree):
        self.self = self
        self.AbstractSyntaxTree = abstractSyntaxTree


