from rply.token import BaseBox

class String(BaseBox):

    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class Print():

    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())
