# Fizz Buzz/三五游戏

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for i in range(1, n+1):             # O(n) time
            if i % 3 == 0 and i % 5 == 0:   # 15的倍数
                answer.append("FizzBuzz")
            elif i % 3 == 0:                # 3的倍数
                answer.append("Fizz")
            elif i % 5 == 0:                # 5的倍数
                answer.append("Buzz")
            else:                           # 其他数字
                answer.append(str(i))
                
        return answer