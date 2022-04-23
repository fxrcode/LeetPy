from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        o, e = 1, 0
        for n in nums:
            if n > 0:
                ans[e] = n
                e += 2
            else:
                ans[o] = n
                o += 2
        return ans

    def findLonely(self, nums: List[int]) -> List[int]:
        nums = [-10] + nums + [1e6 + 1]
        nums.sort()
        ans = []
        for i in range(1, len(nums) - 1):
            if nums[i - 1] == nums[i] or nums[i] == nums[i + 1]:
                continue
            if nums[i - 1] + 1 != nums[i] != nums[i + 1] - 1:
                ans.append(nums[i])
        return ans

    def maximumGood(self, statements: List[List[int]]) -> int:
        


sl = Solution()
# print(sl.rearrangeArray(nums=[3, 1, -2, -5, 2, -4]))
# print(sl.findLonely(nums=[10, 6, 5, 8]))
print(sl.findLonely(nums=[1, 3, 5, 3]))
