"""
tag: Medium, 2ptr
Lookback:
Similar:
- smallest range I/II, 2ptr to try all possibles and battle
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def fxr():
            """
            Runtime: 983 ms, faster than 47.54% of Python3 online submissions for Container With Most Water.

            XXX: AC after hint2. proof by SFC in OS.
            """
            l, r = 0, len(height) - 1
            ans = 0
            while l < r:
                w = r - l
                hl, hr = height[l], height[r]
                h = min(hl, hr)
                ans = max(ans, w * h)
                if hl <= hr:
                    l += 1
                else:
                    r -= 1
            return ans

        return fxr()


sl = Solution()
print(sl.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
