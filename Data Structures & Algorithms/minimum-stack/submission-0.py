class MinStack:

    def __init__(self):
        self.stack = []
        self.hiddenStack = []

        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.hiddenStack:
            self.hiddenStack.append(val)
        else:
            self.hiddenStack.append(min(val,self.hiddenStack[-1]))

        

    def pop(self) -> None:
        self.stack.pop()
        self.hiddenStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.hiddenStack[-1]


        
