"""
💡insight (logic + 2ptr)
tag: Medium, Logic
Lookback:
- crystal clear logic, then coding is trivial
- You cann't modify (add/remove) collections while iterating it. But while len(S) is OK b/c you're not iterating collection S!
"""


class Solution:
    def magicalString(self, n: int) -> int:
        def realisking():
            """
            Runtime: 208 ms, faster than 47.41% of Python3 online submissions for Magical String.

            https://leetcode.com/problems/magical-string/discuss/96472/Short-Python-using-queue
            """
            S = [1, 2, 2]
            idx = 2
            while len(S) < n:
                x = 3 - S[-1]
                times = S[idx]
                S += [x] * times
                idx += 1
            return S[:n].count(1)

        return realisking()


sl = Solution()
assert sl.magicalString(n=6) == 3
assert sl.magicalString(n=1) == 1
