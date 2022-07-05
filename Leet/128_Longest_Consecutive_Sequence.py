"""
✅ GOOD Logic (The Invariance Principle - <Problem-solving strategies>)
Tag: Medium, Set
Lookback:
- Top 100 Liked Questions
- clean thought by Pochmann: just walk every streak, how to decrease invariant (both direction)? simply check x-1 not in ns
"""


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def pochmann():
            """
            Runtime: 528 ms, faster than 62.02% of Python3 online submissions for Longest Consecutive Sequence.

            OS: use space to speed up query, and intelligent sequence building.
            Only start from smallest in subsequnce.
            """
            ns = set(nums)
            best = 0
            for x in ns:
                if x - 1 not in ns:
                    y = x + 1
                    while y in ns:
                        y += 1
                    # current streak broken
                    best = max(best, y - x)
            return best

        return pochmann()


sl = Solution()
print(sl.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
