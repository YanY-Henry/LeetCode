# Single Number/只出现一次的数字

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = []
        for num in nums:            # O(n) time, O(n) space
            if num in once:
                once.remove(num)
            else:
                once.append(num)

        return once[0]


# 使用位运算
class Solution_opt:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0          # O(1) space
        for num in nums:    # O(n) time
            result ^= num

        return result