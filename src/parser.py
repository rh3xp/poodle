

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

