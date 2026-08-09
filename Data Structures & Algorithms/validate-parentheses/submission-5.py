class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {'(': ')', '{': '}', '[':']'}

        for item in s:
            if item in pairs.keys():
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                if pairs[stack[-1]] == item:
                    stack.pop() 
                else:
                    return False
        if len(stack) > 0:
                    return False
        return True
        