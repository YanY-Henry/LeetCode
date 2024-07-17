# Longest Consecutive Sequence/最长连续数列

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Htable = {}

        # 哈希记录该值是否为某一连续序列最左or最右项
        for num in nums:        # O(n) time
            if num in Htable:
                continue
            else:
                left, right = 1, 1
                if (num-1) in Htable:
                    Htable[num-1] = (Htable[num-1][0], 0)
                    left = 0

                if (num+1) in Htable:
                    Htable[num+1] = (0, Htable[num+1][1])
                    right = 0

                Htable[num] = (left, right)     # O(n) space

        # 哈希表中搜索每一序列的最左项，并记录序列长度
        max_len = 0
        for num_l in nums:      # O(n) time
            if Htable[num_l][0] == 1:
                num_r = num_l
                while True:
                    if Htable[num_r][1] == 1:
                        len_num = num_r - num_l + 1
                        max_len = max(len_num, max_len)
                        break
                    else:
                        num_r += 1
        
        return max_len


# set()去掉重复项
# 在set中直接进行查找
class Solution_opt:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums = set(nums)

        for num in nums:
            # 找到序列最左项
            if num-1 not in nums:
                length = 0

                num_r = num
                # 开始记录该序列长度
                while num_r in nums:
                    length += 1
                    num_r += 1

                max_length = max(length, max_length)
        return max_length
