"""
tag: medium, math
Lookback:
- TODO: 1-pass
"""

from collections import Counter


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def fxr():
            """
            Runtime: 58 ms, faster than 92.93% of Python3 online submissions for Substrings That Begin and End With the Same Letter.

            T: O(2N)
            """
            C = Counter(s)
            ans = len(s)
            for f in C.values():
                ans += f * (f - 1) // 2
            return ans

        return fxr()


sl = Solution()
for s in ["abcba", "abacad"]:
    print(sl.numberOfSubstrings(s))
