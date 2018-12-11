import re


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
            word = source_code[source_index]

            # This will recognize a var and create a VAR_DECLARED token for it
            if word == 'var':
                tokens.append(['VAR_DECLARATION', word])

            # This will recognize a word and create an IDENTIFIER token for it
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[len(word) - 1] == ';':
                    tokens.append(['IDENTIFIER', word[0:len(word) - 1]])
                else:
                    tokens.append(['IDENTIFIER', word])

            # This will recognize numbers and create an INTEGER token for it
            elif re.match('[0-9]', word):
                if word[len(word) - 1] == ';':
                    tokens.append(['INTEGER', word[0:len(word) - 1]])
                else:
                    tokens.append(['INTEGER', word])

            # This will recognize operators and create an OPERATOR token for it
            elif word in '=/*=-+':
                tokens.append(['OPERATOR', word])

            # Increases word after checking it
            source_index += 1

        print(tokens)

        # Return created tokens
        return tokens
