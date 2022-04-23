"""
tag: medium, recursion
Lookback:
- learn the pattern from textbook, then recursion is easy
Similar:
- #2217. palindrome of size
"""

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        def dbabichev():
            ans = [0]
            for i in range(n):
                ans += [(1 << i) ^ c for c in reversed(ans)]
            return ans

        def fxr():
            """
            Runtime: 141 ms, faster than 63.31% of Python3 online submissions for Gray Code.
            https://leetcode.com/problems/gray-code/discuss/1308570/Python-Short-recursive-solution-explained

            """

            def rec(b):
                if b == 0:
                    return [0]
                t = rec(b - 1)
                return t + [i + (1 << (b - 1)) for i in t][::-1]

            return rec(n)

        return fxr()


sl = Solution()
print(sl.grayCode(2))
