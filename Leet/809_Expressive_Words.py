"""
tag: medium, str, skills
Lookback:
- groupby type str is good for practice skills
"""

from itertools import groupby
from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def lee215():
            """
            Runtime: 100 ms, faster than 17.92% of Python3 online submissions for Expressive Words.

            4 pointers, is more easier to undersand and debug.
            https://leetcode.com/problems/expressive-words/discuss/122660/C%2B%2BJavaPython-2-Pointers-and-4-pointers
            """

            def check(s, w):
                i, j, i2, j2 = 0, 0, 0, 0
                n, m = len(s), len(w)
                while i < n and j < m:
                    if s[i] != w[j]:
                        return False
                    while i2 < n and s[i2] == s[i]:
                        i2 += 1
                    while j2 < m and w[j2] == w[j]:
                        j2 += 1
                    if not (i2 - i == j2 - j or i2 - i >= max(3, j2 - j)):
                        return False
                    i, j = i2, j2
                return i == n and j == m

            return sum(check(s, w) for w in words)

        return lee215()

        def fxr():
            """
            Runtime: 56 ms, faster than 83.72% of Python3 online submissions for Expressive Words.

            similar: https://leetcode.com/problems/expressive-words/discuss/1429353/Python-Compress-String-S-and-Words-Clean-and-Concise
            """

            def rle(s):
                def os_groupby():
                    res = []
                    for k, grp in groupby(s):
                        res.append([k, len(list(grp))])
                    return res

                def ptr2():
                    l, r = 0, 0
                    res = []
                    while l < len(s):
                        # res.append(s[l])
                        while r < len(s) and s[l] == s[r]:
                            r += 1
                        # s[l] != s[r] or r = len(s)
                        res.append((s[l], r - l))
                        l = r
                    return res

                return os_groupby()

            ss = rle(s)
            cnt = 0
            for ew in map(rle, words):
                if len(ss) != len(ew):
                    continue
                for i in range(len(ss)):
                    if ss[i][0] != ew[i][0]:
                        break
                    if not (ss[i][1] == ew[i][1] or ss[i][1] >= max(3, ew[i][1])):
                        break
                else:
                    cnt += 1
                    # print(ss, ew)
            return cnt

        return fxr()


sl = Solution()
print(sl.expressiveWords(s="heeellooo", words=["hello", "hi", "helo"]))
print(sl.expressiveWords(s="zzzzzyyyyy", words=["zzyy", "zy", "zyy"]))
