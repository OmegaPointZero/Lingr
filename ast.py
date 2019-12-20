import lexer
import argparse

class program:
    def __init__(self, sentences):
        self.sentences = sentences
        self.static_variables = []
        self.uninitialized_variables = []

    def get_sentences(self):
        for sentence in self.sentences:
            self.generate_tree(sentence)
        return self.sentences

    def generate_tree(self,sentence):
        print('Number of things to interpret: %s' % len(sentence))
                
        
        
        for thing in sentence:
            print(thing)

prog = program(lexer.main(argparse.Namespace(file_path='test.lr', printast=True, printlex=False, standalone=False)))

test_sentence = prog.get_sentences()
