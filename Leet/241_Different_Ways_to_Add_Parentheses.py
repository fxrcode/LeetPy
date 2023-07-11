"""
Labuladong: Divide & Conquer

"""
from functools import cache
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def labuladong(expr) -> list[int]:
            """
            Runtime: 39 ms, faster than 42.41% of Python3 online submissions for Different Ways to Add Parentheses.

            T: O(N * 2^N) as in https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/866096/Python%3A-Divde-and-Conquer-%2B-Memoization-%2B-O(N-*-2N)
            """
            ans = []

            for i, c in enumerate(expr):
                if c in "+-*":
                    l = labuladong(expr[:i])
                    r = labuladong(expr[i + 1 :])
                    for a in l:
                        for b in r:
                            if c == "+":
                                ans.append(a + b)
                            elif c == "-":
                                ans.append(a - b)
                            else:
                                ans.append(a * b)

            if not ans:
                ans.append(int(expr))
            return ans

        return labuladong(expression)


sl = Solution()
print(sl.diffWaysToCompute(expression="2-1-1"))
print(sl.diffWaysToCompute(expression="2*3-4*5"))
