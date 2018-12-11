

class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):

        # Where all the tokens created by the lexer will be stored
        tokens = []

        # Create a word list of the source code
        source_code = self.source_code.split()

        # This willkeep a trackof word index we are at in source code
        source_index = 0

        # Loop through each word in source code to generate tokens
        while source_index < len(source_code):
            print(source_code[source_index])
 
            # Increases word after checking it
            source_index += 1

        # Return created tokens
        return tokens
