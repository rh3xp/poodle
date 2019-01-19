class Lexer:

    def __init__(self, data):
        self.data = data
        self.tokens = []
        self.comm = []
        self.keywords = [
                'vomit'
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

                elif l == ' ' and tid != 'char':
                    continue
                
                elif l == '/*' and tid == '':
                    tid = 'comment'
                    tmp = []

                elif l == '*/' and tid == 'comment':
                    self.comm.append({'id': tid, 'value': ''.join(com)})
                
                else:
                    tmp.append(l)
                    com.append(l)
