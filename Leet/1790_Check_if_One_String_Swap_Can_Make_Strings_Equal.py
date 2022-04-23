"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, math
Lookback:
- neat and elegant coding style: pythonic
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        def ye15():
            """
            Your runtime beats 98.90 % of python3 submissions.

            """
            dif = [[x, y] for x, y in zip(s1, s2) if x != y]
            return not dif or len(dif) == 2 and dif[0][::-1] == dif[1]

        return ye15()


sl = Solution()

print(sl.areAlmostEqual(s1="b", s2="k"))
print(sl.areAlmostEqual(s1="bank", s2="kanb"))
