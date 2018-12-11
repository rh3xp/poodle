

class VariableObject(object):

    def __init__(self):
        # This will hold the exec string for var declaration
        self.exec_string = ""

    def transpile(self, name, operator, value):
        # return the string to be executed
        self.exec_string += name + " " + operator + " " + value + '\n'
        return self.exec_string
