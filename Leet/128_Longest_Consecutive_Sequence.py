"""
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

"""


from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Runtime: 184 ms, faster than 89.77% of Python3 online submissions for Longest Consecutive Sequence.

        OS: use space to speed up query, and intelligent sequence building.
        Only start from smallest in subsequnce.
        """
        num_set = set(nums)
        longest_streak = 0

        # only traverse unique numbers!
        for n in num_set:
            # intelligent sequence building
            if n-1 not in num_set:
                cur = n
                cur_streak = 1

                while cur + 1 in num_set:
                    cur = cur + 1
                    cur_streak += 1
                longest_streak = max(longest_streak, cur_streak)
        return longest_streak


sl = Solution()
print(sl.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
