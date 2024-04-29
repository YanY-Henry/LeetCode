# Valid Parentheses/有效的括号

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # 建栈检测
        for i in s:                                 # O(n) time
            if i == '(' or i == '{' or i == '[':    # O(n) space
                stack.append(i)
            elif len(stack) == 0:
                return False
            elif i == ')' and stack.pop() != '(':
                return False
            elif i == '}' and stack.pop() != '{':
                return False
            elif i == ']' and stack.pop() != '[':
                return False

        if len(stack) != 0:
            return False
        
        return True