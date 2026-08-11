class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(token)
            if token not in "+-*/":
                stack.append(int(token))
            else:
                if token == '+':
                    res = int(stack.pop()) + int(stack.pop())
                    stack.append(res)
                elif token == '-':
                    second = int(stack.pop())
                    first = int(stack.pop())
                    res = first - second
                    stack.append(res)
                elif token == '*':
                    res = int(stack.pop()) * int(stack.pop())
                    stack.append(res)
                else:
                    second = int(stack.pop())
                    first = int(stack.pop())
                    res = int(first / second)
                    stack.append(res)
        return int(stack.pop())
        
        
        