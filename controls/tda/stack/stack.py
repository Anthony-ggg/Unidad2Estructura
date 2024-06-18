from controls.tda.stack.StackOperation import Stack
class Stack():
    def __init__(self,size):
        self.__stack = StackOperation(size)

    def push(self,data):
        self.__stack.push(data)

    def pop(self):
        return self.__stack.pop
    
    def print(self):
        self.__stack.print

    def verify(self):
        return self.__stack.verifyTop