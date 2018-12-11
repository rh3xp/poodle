

class Parser(object):
    def __init__(self, tokens):
        # This will hold all the tokens created by the lexer
        self.tokens = tokens
        # This will hold the token index we are parsing at
        self.token_index = 0

    def parse(self):

        while self.token_index < len(self.tokens):

            # Holds the type of token ie. IDENTIFIER
            token_type = self.tokens[self.token_index][0]
            # Holds the value o token eg. var
            token_value = self.tokens[self.token_index][1]

            # This will trigger when a variable declaration token is found
            if token_type == "VAR_DECLARATION" and token_value == "var":
                self.parse_variable_declaration(self.tokens[self.token_index: len(self.tokens)])

            # Increment token index so that we can loop through tokens
            self.token_index += 1

    def parse_variable_declaration(self, token_stream):
        tokens_checked = 0

        for token in range(0, len(token_stream)):

            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            # Helps parse 1 statement at a time
            if token_type == 'STATEMENT_END':
                break

            # This will get variable type rg. var, let, const
            if token == 0:
                print('Variable type: ' + token_value)

            # This will take variable name and also perform error validation
            elif token == 1 and token_type == "IDENTIFIER":
                print('Variable name: ' + token_value)

            elif token == 1 and token_type != "IDENTIFIER":
                print("ERROR: Invalid Variable Name '" + token_value + "'")
                quit()

            # This will get variable assignment operator ie. '='
            elif token == 2 and token_type == "OPERATOR":
                print('Assignment Operator: ' + token_value)
            elif token == 2 and token_type != "OPERATOR":
                print("ERROR: Assignment Operator is missing or invalid, should be '='")
                quit()

            # This will get the variable value assigned
            elif token == 3 and token_type in ['STRING', 'INTEGER', 'IDENTIFIER']:
                print('Variable value: ' + token_value)
            elif token == 3 and token_type not in ['STRING', 'INTEGER', 'IDENTIFIER']:
                print("ERROR: Invalid Variable Assignment Value '" + token_value + "'")
                quit()

            tokens_checked += 1

        # Increment token index by amount of tokens we checked to avoid repetition
        self.token_index += tokens_checked
