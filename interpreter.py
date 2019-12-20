import ast
import lexer

class expressions:
    def __init__(self):
        self.self = self
    
    def plus(first,second):
        strings = False

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
            # return f + s
            # determine number lengths, in bytes
            # Then determine opcode.
            opcodes = [0xa,]                

        elif strings:
            return str(f) + str(s)
