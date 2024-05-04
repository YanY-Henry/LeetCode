# Decode String/字符串解码

class Solution:
    def decodeString(self, s: str) -> str:
        result = ""                                 # O(n) space
        begin, num = -1, -1
        for i in range(len(s)):                     # O(n) time
            # 正常搜索
            if begin == -1:
                if '0'<=s[i]<='9':
                    num = i
                    begin = i + 1
                    stack_bracket = []
                else:
                    result += s[i]
            # 判断数字k
            elif begin == i:
                if '0'<=s[i]<='9':
                    begin += 1
                elif s[i] == '[':
                    k = int(s[num:i])
                    stack_bracket.append(i)
            # 判断最外层括号范围
            else:
                if s[i] == '[':
                    stack_bracket.append(i)
                elif s[i] == ']':
                    stack_bracket.pop()
                    # 找到最外层括号内容，开始递归
                    if len(stack_bracket) == 0:
                        end = i
                        result += Solution.decodeString(Self, s[begin+1:end]) * k
                        begin = -1
        return result


# 用 for c in s: 代替 for i in range(len(s)):
class Solution_opt:
    def decodeString(self, s: str) -> str:
        stack, result, k = [], "", 10               # O(n) space
        for c in s:                                 # O(n) time
            # last_result + k[result] + unknown 
            # <----stack---->
            if c == '[':
                stack.append([result, k])
                result, k = "", 0
            elif c == ']':
                last_result, cur_k = stack.pop()
                result = last_result + result * cur_k
            elif '0' <= c <= '9':
                k = k * 10 + int(c)            
            else:
                result += c
        return result
