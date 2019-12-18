import argparse
import io
import re 

parser = argparse.ArgumentParser(description='Lexical analyzer for Lingr')

parser.add_argument('-f, --file', action='store', dest='file_path', help='Specify a single file to work with, or comma seperated files')
parser.add_argument('-l, --printlex', action='store_true', dest='printlex', help='Print the lexed lexed token list')
parser.add_argument('-a, --printast', action='store_true', dest='printast', help='Print the Abstract Syntax Tree')

results = parser.parse_args()

def tokenize(token):
    operators = ['+', '-', '*', '/', '=']
    start_identifiers = ['"', '(', '[']
    end_identifiers = [';', ']', ')', '"']

    if token[0] in start_identifiers:
        return[{'TYPE' : 'IDENTIFIER', 'TOKEN': token[0]}] + tokenize(token[1:])
    elif token[-1] in end_identifiers:
        return tokenize(token[:-1]) + [{ 'TYPE' : 'IDENTIFIER', 'TOKEN' : token[-1] }]
    if token[0] == '_':
        return [{ 'TYPE': 'NAME', 'TOKEN': token }]
    elif re.match('^\d+$', token):
        return [{'TYPE' : 'INT', 'TOKEN': token}]
    elif token in operators:
        return [{ 'TYPE' : 'OPERATOR', 'TOKEN' : token}]
    else:
        return [{ 'TYPE' : 'ITEM', 'TOKEN' : token }]

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
    return stringified

def sentenced(tokens):
    sentences = []
    this_sentence = []
    for t in tokens:
        if t['TYPE'] == 'IDENTIFIER' and t['TOKEN'] == ';':
            sentences.append(this_sentence)
            this_sentence = []
        else:
            this_sentence.append(t)
    return sentences

def generateAST(tokens):
    # A sentence is a line of code. Sentences are demarcated by the ';' symbol.
    sentences = sentenced(tokens)
    print('Sentences:')
    for sentence in sentences:
        print(sentence)

def main(options):
    lexed_items = parse_file(options.file_path)
    if options.printlex == True:
        for s in lexed_items:
            print(s)
    ast = generateAST(lexed_items)
main(results)
