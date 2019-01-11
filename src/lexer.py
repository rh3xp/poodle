#!/usr/bin/python3

# read file
with open("hello.poo", "r") as code:
    # print lines
    for line in code.readlines():
        print(line)
        
        # print words
        for word in line.split():
            print(word)
