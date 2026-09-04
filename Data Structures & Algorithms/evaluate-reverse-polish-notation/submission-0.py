class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                y = stack.pop()
                x = stack.pop()
                stack.append(x+y)
            elif i == "-":
                y = stack.pop()
                x = stack.pop()
                stack.append(x-y)
            elif i == "*":
                y = stack.pop()
                x = stack.pop()
                stack.append(x*y)
            elif i == "/":
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x/y))
            else:
                stack.append(int(i))
        return stack[-1]
