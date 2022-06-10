"""
Tag: 2ptr, Medium
Lookback:
- Classic slide window
"""


from collections import Counter
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        def fxr_slide():
            l, r = 0, 0
            win = Counter()
            ans = sm = 0
            while r < len(nums):
                c = nums[r]
                r += 1
                sm += c
                win[c] += 1
                while len(win) < r - l:
                    d = nums[l]
                    l += 1
                    sm -= d
                    win[d] -= 1
                    if win[d] == 0:
                        win.pop(d)
                # now win is unique
                ans = max(ans, sm)
            return ans

        return fxr_slide()


sl = Solution()
print(sl.maximumUniqueSubarray(nums=[4, 2, 4, 5, 6]))
print(sl.maximumUniqueSubarray(nums=[5, 2, 1, 2, 5, 2, 1, 2, 5]))
