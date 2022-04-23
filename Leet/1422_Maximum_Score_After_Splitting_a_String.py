"""
tag: Easy, math
Lookback:
- re-state formula!
"""


class Solution:
    def maxScore(self, s: str) -> int:
        def ye15_1pass():
            """
            Runtime: 40 ms, faster than 78.04% of Python3 online submissions for Maximum Score After Splitting a String.

            Max( zeroL + oneR )
            =Max( zeroL - oneL + oneL + oneR )
            =Max( zeroL - oneL ) + oneTotal
            """
            zeros = ones = 0
            ans = float("-inf")
            for i in range(len(s) - 1):
                if s[i] == "0":
                    zeros += 1
                else:
                    ones -= 1
                ans = max(ans, zeros + ones)
            return ans - ones + (1 if s[-1] == "1" else 0)

        return ye15_1pass()

        def fxr():
            # Runtime: 66 ms, faster than 27.21% of Python3 online submissions for Maximum Score After Splitting a String.
            ones = s.count("1")
            mxscore = 0
            l1 = 0
            for i in range(len(s) - 1):
                l1 += s[i] == "1"
                l0 = i + 1 - l1
                r1 = ones - l1
                mxscore = max(mxscore, l0 + r1)
            return mxscore

        return fxr()


sl = Solution()
print(sl.maxScore(s="011101"))
print(sl.maxScore(s="00111"))
print(sl.maxScore(s="1111"))
