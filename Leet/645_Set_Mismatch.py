"""
✅ GOOD Skill: HOLY SHIT (WA x 6)
Tag: Easy, math, 2ptr, Skills
Lookback:
- damn, I got WA x 6! 
- Please understand problem (aka: find inner property), then code.
"""

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        def gongshui_math():
            """
            Runtime: 200 ms, faster than 92.72% of Python3 online submissions for Set Mismatch.

            https://leetcode-cn.com/problems/set-mismatch/solution/gong-shui-san-xie-yi-ti-san-jie-ji-shu-s-vnr9/
            T: O(N)
            """
            n = len(nums)
            tot = (1 + n) * n // 2
            dup = sum(nums) - sum(set(nums))
            miss = tot - sum(set(nums))
            return [dup, miss]

        return gongshui_math()

        def os_cn_sort():
            """
            https://leetcode-cn.com/problems/set-mismatch/solution/cuo-wu-de-ji-he-by-leetcode-solution-1ea4/
            T: O(nlogn)
            """
            nums.sort()
            res = [0, 0]
            prev = 0
            for n in nums:
                if n == prev:
                    res[0] = n
                elif n - prev > 1:
                    res[1] = n - 1
                prev = n
            if nums[-1] != len(nums):
                res[1] = len(nums)
            return res

        return os_cn_sort()

        def fxr_WA():
            nums.sort()
            miss, dup = -1, -1
            for i, n in enumerate(nums):
                if miss == -1 and n != i + 1:
                    miss = i + 1
                if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                    dup = nums[i]
            return [dup, miss]

        return fxr_WA()


sl = Solution()
print(sl.findErrorNums(nums=[1, 2, 2, 4]))
print(sl.findErrorNums(nums=[1, 1]))
print(sl.findErrorNums(nums=[2, 2]))
print(sl.findErrorNums([3, 3, 1]))
print(sl.findErrorNums([3, 2, 3, 4, 6, 5]))
# assert sl.findErrorNums([3, 2, 3, 4, 6, 5]) == [3, 1]
print(sl.findErrorNums([1, 5, 3, 2, 2, 7, 6, 4, 8, 9]))
print(sl.findErrorNums([1, 2, 2, 3, 4, 5]))
