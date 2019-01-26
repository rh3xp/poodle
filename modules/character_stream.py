class characterStream:

    def __init__(self, string):
        self.iterator = iter(string)
        self._fill()

    def _fill(self):
        try:
            self.next = next(self.string)
        except StopIteration:
            self.next = None

    def move_next(self):
        ret = self.next()
        self._fill()
        return ret

