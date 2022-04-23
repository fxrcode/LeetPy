"""
tag: Easy
Lookback:
- always Neat! esp: easy
"""


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        def discuss():
            cnt = 0
            for i in range(len(s) - 2):
                if len(set(s[i : i + 3])) == 3:
                    cnt += 1
            return cnt

        def fxr():
            # Runtime: 42 ms, faster than 66.22% of Python3 online submissions for Substrings of Size Three with Distinct Characters.
            cnt = 0
            for i in range(len(s)):
                if i + 2 < len(s):
                    ss = s[i : i + 3]
                    if len(set(ss)) == len(ss):
                        cnt += 1
            return cnt

        return fxr()


sl = Solution()
print(sl.countGoodSubstrings("xyzzaz"))
print(sl.countGoodSubstrings("aababcabc"))
print(sl.countGoodSubstrings("a"))
