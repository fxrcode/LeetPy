"""
✅ GOOD Greedy
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
tag: easy, DP, dfs
Lookback
- backward thinking + logic
"""


from functools import cache
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def greedy() -> bool:
            """
            REF: https://www.youtube.com/watch?v=Yan0cv2cLy8
            Runtime: 496 ms, faster than 89.67% of Python3 online submissions for Jump Game.

            XXX: Neet says this is his favorite question!
                Neet's brute force backtrack analysis is inspiring, so does Greedy impl
            """
            n = len(nums)
            goal = n - 1
            for i in range(n)[::-1]:
                if i + nums[i] >= goal:
                    goal = i
            return goal == 0

        return greedy()

        def dp() -> bool:
            """
            TLE: 141 / 169 test cases passed.

            REF: https://leetcode.com/problems/jump-game/discuss/1443541/Python-2-approaches%3A-Top-down-DP-Max-Pos-So-Far-Clean-and-Concise

            XXX: rec(i) means if you can reach the last index from index i or not.
            """
            n = len(nums)

            @cache
            def rec(i):
                if i == n - 1:
                    return True
                # XXX: sage in this range! It handles i+nums[i] > n-1,
                #       also, if nums[i] == 0! which means pos i can not move furthor!
                for j in range(i + 1, min(i + nums[i], n - 1) + 1):
                    if rec(j):
                        return True
                else:
                    return False

            return rec(0)


sl = Solution()
print(sl.canJump(nums=[1, 2]))
print(sl.canJump(nums=[0, 2, 3]))
print(sl.canJump(nums=[2, 3, 1, 1, 4]))
print(sl.canJump(nums=[3, 2, 1, 0, 4]))
