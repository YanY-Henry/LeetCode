# Roman to Integer/罗马数字转整数

# 小值在左则做减法，否则做加法
class Solution:
    def romanToInt(self, s: str) -> int:
        alphabet = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        integer = 0                     # O(1) space
        for i, c in enumerate(s):       # O(n) time
            integer += alphabet[c]

            if i>0 and alphabet[s[i-1]] < alphabet[c]:
                integer -= 2 * alphabet[s[i-1]]

        return integer
