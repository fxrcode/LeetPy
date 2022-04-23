'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

✅ GOOD 基本功
'''


from typing import List
from collections import Counter


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        def os_hash():
            """
            Runtime: 44 ms, faster than 88.73% of Python3 online submissions for Largest Unique Number.

            T: O(N), M:O(N)
            """
            cnt = Counter(nums)
            ans = -1
            for k, v in cnt.items():
                if v == 1:
                    ans = max(ans, k)
            return ans

        def os_sort():
            """
            Runtime: 48 ms, faster than 74.18% of Python3 online submissions for Largest Unique Number.

            T: O(nlogn), M:O(1)
            XXX: basic coding skill
            """
            nums.sort(reverse=True)
            i = 0
            while i < len(nums):
                # return if there's no duplicate
                if i == len(nums)-1 or nums[i] != nums[i+1]:
                    return nums[i]
                # while duplicate exists
                while i < len(nums)-1 and nums[i] == nums[i+1]:
                    i += 1
                # loop invariant: i always point to next unique or out of range
                i += 1
            return -1

        def fxr_brute():
            """
            Runtime: 48 ms, faster than 74.18% of Python3 online submissions for Largest Unique Number.

            AC in 1. But spent 10min to tune coding.
            """
            nums.sort(reverse=True)
            i, j = 0, 0
            ans = nums[i]
            while i < len(nums):
                while j < len(nums) and nums[j] == ans:
                    j += 1
                if j-i == 1:
                    return ans
                if j == len(nums):
                    return -1
                i = j
                ans = nums[i]
            return -1

        return fxr_brute()


sl = Solution()
print(sl.largestUniqueNumber(nums=[8]))
print(sl.largestUniqueNumber(nums=[9, 8, 9, 8]))
print(sl.largestUniqueNumber(nums=[9, 8, 9, 8, 7]))
