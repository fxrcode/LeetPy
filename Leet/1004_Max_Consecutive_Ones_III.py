"""
✅ GOOD Slide-window
tag: medium, slide-window
Lookback:
* when substr w/ constrains => slide-window 
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        def hiepit():
            """
            Runtime: 873 ms, faster than 38.39% of Python3 online submissions for Max Consecutive Ones III.

            """
            l, r = 0, 0
            ans = 0
            zeros = 0
            while r < len(nums):
                c = nums[r]
                r += 1
                if c == 0:
                    zeros += 1
                while zeros > k:
                    d = nums[l]
                    l += 1
                    if d == 0:
                        zeros -= 1
                # now windows at most k flip
                ans = max(ans, r - l)
            return ans

        return hiepit()


sl = Solution()
print(sl.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(sl.longestOnes(nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
