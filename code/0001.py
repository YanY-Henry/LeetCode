# Two Sum/两数之和

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}

        # 哈希表记录num和其位置
        n_nums = len(nums)
        for i in range(n_nums):                     # O(n) time
            if hashNums.get( nums[i] ) == None:
                hashNums[ nums[i] ] = [i]
            else:
                hashNums[ nums[i] ].append(i)       # O(n) space

        # 搜索target - nums[i]
        for i in range(n_nums):                     # O(n) time
            ans = target - nums[i]
            ans_key = hashNums.get( ans )

            if ans_key != None:
                if ans != nums[i]:
                    return [i, ans_key[0]]
                elif len(ans_key) > 1:
                    return [i, ans_key[1]]


# 使用for i, num in enumerate(nums):
# 同时完成哈希表的插值与搜索
class Solution_opt:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}

        for i, num in enumerate(nums):              # O(n) time
            ans = target - num
            if ans in hashNums:
                return [hashNums[ans], i]
            else:
                hashNums[num] = i                   # O(n) space
