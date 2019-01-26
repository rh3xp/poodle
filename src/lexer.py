import sys
sys.path.insert(0, '../modules/')
from character_stream import characterStream


def _scan(first_char, chars, allowed):
    ret = first_char
    p = chars.next
    while p is not None and re.match(allowed, p):
        ret += chars.move_next()
        p = chars.next
    return ret


def _scan_string(delim, chars):
    ret = ""
    while char != delim:
        c = chars.move_next()
        if c is None:
            raise Exception("A string ran off the end of the program.")


class Lexer:

    def __init__(self, data):
        self.data = data
        self.tokens = []
        self.comm = []
        self.keywords = [
                'vomit',
                'wrap',
                'as',
                'pp',
                'eq',
                'let',
                'exit()'
                ]

    def tokenizer(self):

        for loc in self.data:
            tmp = []
            com = []
            tid = ''

            for l in loc:
                if l == '"' and tid == '':
                    tid = 'char'
                    tmp = []

                elif l == '"' and tid == 'char':
                    self.tokens.append({'id':tid, 'value': ''.join(tmp)})
                    tid = ''
                    tmp = []

                elif ''.join(tmp) in self.keywords:
                    self.tokens.append({'id': 'keyword', 'value': ''.join(tmp)})
                    tmp = []

                elif l == "/*" and tid == '':
                    tid = 'comment'
                    com = []

                elif l == "*/" and tid == 'comment':
                    self.comm.append({'id': "comment", 'value': ''.join(com)})
                    tid = ''
                    com = []

                elif l == ' ' and tid != 'char' and tid != 'comment':
                    continue


                else:
                    tmp.append(l)
                    com.append(l)
