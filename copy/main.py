import lexer
#import parser


def main():
    # Read the current poodle source code in test.lang and store it in variable
    content = ""
    with open("test.lang", 'r') as file:
        content = file.read()

    #
    # Lexer
    #

    # We call the lexer class and initialize it with the source code
    lex = lexer.Lexer(content)
    # We now call the tokenize method

    tokens = lex.tokenize()

    #
    # Parser
    #

    # We call the parser
    #parse = parser.Parser(tokens)
    #parse.parse()


main()
