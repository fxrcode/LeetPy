"""
https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions

"""
# Definition for a binary tree node.


from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        def os():
            """
            XXX: OS is always cleaner!
            """
            ans = anchor = 0
            for i in range(len(nums)):
                if i and nums[i - 1] >= nums[i]:
                    anchor = i
                ans = max(ans, i - anchor + 1)
            return ans

        def fxr():
            """
            Runtime: 68 ms, faster than 96.82% of Python3 online submissions for Longest Continuous Increasing Subsequence.

            AC in 1
            """
            l = 0
            mx = nums[0] - 1
            ans = 1
            for r, v in enumerate((nums)):
                if v <= mx:
                    l = r
                else:
                    ans = max(ans, r - l + 1)
                mx = v
            return ans
