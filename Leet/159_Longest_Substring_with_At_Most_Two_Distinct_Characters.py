"""
tag: Medium, slide-window
Lookback:
- classic slide-window, but what template should I use? (careful on indexing)
"""

from typing import Counter


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        def fxr():
            # Runtime: 580 ms, faster than 37.62% of Python3 online submissions for Longest Substring with At Most Two Distinct Characters.
            l, r = 0, 0
            win = Counter()
            ans = 0
            while r < len(s):
                win[s[r]] += 1
                r += 1
                while len(win) > 2:
                    d = s[l]
                    win[d] -= 1
                    if win[d] == 0:
                        win.pop(d)
                    l += 1
                # now local max win of len(win) <= 2
                ans = max(ans, r - l)
            return ans

        return fxr()


sl = Solution()
print(sl.lengthOfLongestSubstringTwoDistinct(s="eceba"))
print(sl.lengthOfLongestSubstringTwoDistinct(s="ccaabbb"))
print(sl.lengthOfLongestSubstringTwoDistinct(s="ec"))
