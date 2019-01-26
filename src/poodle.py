#!/usr/bin/python3
from lexer import Lexer
#from pprint import pprint

def main():
    filename = 'hello.poo'
    file = open(filename, 'r')
    lexer = Lexer(file)

    lexer.tokenizer()
    print("Tokens:")
    print(lexer.tokens)
    print("Comments:")
    print(lexer.comm)


if __name__ == "__main__":
    main()
