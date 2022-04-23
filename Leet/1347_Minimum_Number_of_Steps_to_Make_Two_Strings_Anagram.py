"""
tag: medium, hash, str
Lookback:
- analysis => simpler logic
"""

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def kevin():
            """
            Runtime: 384 ms, faster than 24.93% of Python3 online submissions for Minimum Number of Steps to Make Two Strings Anagram.

            """
            freq = Counter(s)
            ans = len(s)  # init ans to all need to change
            for c in t:
                if c in freq and freq[c] != 0:
                    freq[c] -= 1
                    ans -= 1
            return ans

        return kevin()


sl = Solution()
print(sl.minSteps(s="bab", t="aba"))
