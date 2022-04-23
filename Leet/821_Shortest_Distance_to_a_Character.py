"""
tag: Easy, logic, Skills
Lookback:
- simple 2-pass
- how to write neat impl? Check dbabichev, rock, lee215
"""

from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def dbabichev():
            """
            Runtime: 71 ms, faster than 52.13% of Python3 online submissions for Shortest Distance to a Character.

            """

            def letter_get(ch, dir):
                n = len(s)
                res, cur = [0] * n, -n
                for i in range(n)[::dir]:
                    if s[i] == ch:
                        cur = i
                    res[i] = abs(i - cur)
                return res

            return [min(x, y) for x, y in zip(letter_get(c, 1), letter_get(c, -1))]

        return dbabichev()

        def fxr():
            """
            Runtime: 77 ms, faster than 45.18% of Python3 online submissions for Shortest Distance to a Character.
            T: O(2N)
            """
            n = len(s)
            ans = [n + 1] * n
            prev = next = -1  # BUG: None
            for i in range(n):
                if c == s[i]:
                    prev = i
                if prev != -1:
                    ans[i] = i - prev
            for j in range(n - 1, -1, -1):
                if c == s[j]:
                    next = j
                if next != -1:
                    ans[j] = min(ans[j], next - j)
            return ans

        return fxr()


sl = Solution()
print(sl.shortestToChar(s="loveleetcode", c="e"))
print(sl.shortestToChar(s="aaab", c="b"))
print(sl.shortestToChar("baaa", "b"))
