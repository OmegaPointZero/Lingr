import argparse
import io
import re 

parser = argparse.ArgumentParser(description='Lexical analyzer for Lingr')

parser.add_argument('-f, --file', action='store', dest='file_path', help='Specify a single file to work with')
parser.add_argument('-p, --printlex', action='store_true', help='Print the lexed AST')

results = parser.parse_args()

def tokenize(token):
    operators = ['+', '-', '*', '/', '=']
    start_identifiers = ['"', '(', '[']
    end_identifiers = [';', ']', ')', '"']

    if token[0] in start_identifiers:
        return[{'TYPE' : 'IDENTIFIER', 'TOKEN': token[0]}] + tokenize(token[1:])
    elif token[-1] in end_identifiers:
        return tokenize(token[:-1]) + [ { 'TYPE' : 'IDENTIFIER', 'TOKEN' : token[-1] } ]
    if token[0] == '_':
        return [ { 'TYPE': 'NAME', 'TOKEN': token } ]
    elif re.match('^\d+$', token):
        return [{'TYPE' : 'INT', 'TOKEN': token}]
    elif token in operators:
        return [ { 'TYPE' : 'OPERATOR', 'TOKEN' : token} ]
    else:
        return [ { 'TYPE' : 'ITEM', 'TOKEN' : token } ]

def lex_line(line):
    items = line.split(' ')
    items = filter(None, items)
    lexed = []

    for item in items:
        t = tokenize(item)
        lexed = lexed + t
    return lexed

def identify_strings(lexed_list):
    strings = False
    new_list = []
    temp_string = []
    for item in lexed_list:
        if item['TYPE'] == 'IDENTIFIER' and item['TOKEN'] == '"':
            strings = not strings
            if strings == False:
                string = { 'TYPE' : 'STRING', 'TOKEN' : ' '.join(temp_string) }
                new_list.append(string)
            elif strings == True:
                temp_string = []
        elif strings == False:
            new_list.append(item)
        elif strings == True:
            temp_string.append(item['TOKEN'])
    return new_list

def parse_file(path):
    f = io.open(path, 'r')
    contents = (f.read()).split('\n')
    file_lexed = []
    for line in contents:
        lexed = lex_line(line)
        for lex in lexed:
            file_lexed.append(lex)
    stringified = identify_strings(file_lexed)
    for s in stringified:
        print(s)

parse_file(results.file_path);





