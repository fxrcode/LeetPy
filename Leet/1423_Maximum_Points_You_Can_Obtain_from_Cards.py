"""
✅ GOOD Slide-window (Unshrinkable)
tag: Medium, DP, Slide-window 
Lookback:
- common re-state: two sides max <=> inner min
Similar:
- 1013. three equal segments => sum = tot//3
"""

from functools import cache
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        def rock_slide_win():
            """
            Runtime: 648 ms, faster than 29.24% of Python3 online submissions for Maximum Points You Can Obtain from Cards.

            since take from head/tail, so we connect 2 ends => circular array
            # unshrinkable slide window: only outer loop
            https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175088/C%2B%2B-Maximum-Sliding-Window-Cheatsheet-Template!
            """
            ans = win = 0
            L = len(cardPoints)
            for i in range(L - k, L + k):
                win += cardPoints[i % L]
                if i >= L:
                    win -= cardPoints[i - k]
                ans = max(win, ans)
            return ans

        return rock_slide_win()

        def fxr_roll_hash():
            """
            Runtime: 604 ms, faster than 39.69% of Python3 online submissions for Maximum Points You Can Obtain from Cards.

            """
            tot = sum(cardPoints)
            M = len(cardPoints)
            N = M - k
            mn = 0
            for i in range(N):
                mn += cardPoints[i]
            sm = mn
            for i in range(1, M - N + 1):
                sm = sm - cardPoints[i - 1] + cardPoints[i + N - 1]
                mn = min(sm, mn)
            return tot - mn

        return fxr_roll_hash()

        def fxr_TLE():
            """
            TLE: 28 / 40 test cases passed.
            T: O()
            """

            @cache
            def dp(i, j, k):
                if k <= 0 or i > j:
                    return 0
                if i == j:
                    return cardPoints[i]
                return max(
                    cardPoints[i] + dp(i + 1, j, k - 1),
                    cardPoints[j] + dp(i, j - 1, k - 1),
                )

            return dp(0, len(cardPoints) - 1, k)

        return fxr_TLE()


sl = Solution()
print(sl.maxScore(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3))
print(sl.maxScore(cardPoints=[2, 2, 2], k=2))
print(sl.maxScore(cardPoints=[9, 7, 7, 9, 7, 7, 9], k=7))
