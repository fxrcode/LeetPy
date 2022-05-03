"""
✅ GOOD Str (Skill)
Tag: Easy, 2ptr, Skills
Lookback:
- groupby snippet! Must be fluent
"""

from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        def rle_groupby():
            # Runtime: 39 ms, faster than 87.50% of Python3 online submissions for Positions of Large Groups.
            l, r = 0, 0
            res = []
            while l < len(s):
                while r < len(s) and s[l] == s[r]:
                    r += 1
                # r == len(s) or s[l] != s[r]:
                if r - l >= 3:
                    res.append([l, r - 1])
                l = r
            return res

        return rle_groupby()

        def os():
            """
            Runtime: 54 ms, faster than 45.09% of Python3 online submissions for Positions of Large Groups.

            """
            res = []
            i = 0  # start of each group
            for j in range(len(s)):
                if j == len(s) - 1 or s[j] != s[j + 1]:
                    # here, [i,j] repr a group
                    if j - i + 1 >= 3:
                        res.append([i, j])
                    i = j + 1
            return res

        return os()

        def fxr():
            # Runtime: 82 ms, faster than 6.80% of Python3 online submissions for Positions of Large Groups.
            pre, idx = "", 0
            res = []
            for i, c in enumerate(s + "*"):
                if pre != c:
                    if pre and i - idx >= 3:
                        res.append([idx, i - 1])
                    pre, idx = c, i
            return res

        return fxr()


sl = Solution()
print(sl.largeGroupPositions(s="abbxxxxzzy"))
print(sl.largeGroupPositions(s="abc"))
print(sl.largeGroupPositions(s="abcdddeeeeaabbbcd"))
print(sl.largeGroupPositions(s="aaaabcccc"))
