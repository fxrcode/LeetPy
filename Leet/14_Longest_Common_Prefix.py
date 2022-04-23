"""
FB tag
tag: easy, logic, bisect, sort
Lookback
- sort then compare first vs last, due to COMMON prefix, draw the diagram then you know
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def powcai():
            """
            https://leetcode-cn.com/problems/longest-common-prefix/solution/duo-chong-si-lu-qiu-jie-by-powcai-2/
            """

            def vertical_scan():
                # Runtime: 57 ms, faster than 34.43% of Python3 online submissions for Longest Common Prefix.
                res = []
                for chrs in zip(*strs):
                    chrs_set = set(chrs)
                    if len(chrs_set) == 1:
                        res.append(chrs[0])
                    else:
                        break
                return "".join(res)

            def smart_ass():
                # Runtime: 38 ms, faster than 78.25% of Python3 online submissions for Longest Common Prefix.
                if not strs:
                    return ""
                strs.sort()
                first, last = strs[0], strs[-1]
                i = 0
                for cd in zip(first, last):
                    if cd[0] != cd[1]:
                        return first[:i]
                    i += 1
                return first[:i]

            return smart_ass()

        return powcai()

        def short_post():
            """
            Runtime: 69 ms, faster than 5.15% of Python3 online submissions for Longest Common Prefix.

            T: O(N + N*minL)
            """
            if not strs:
                return ""

            shortest = min(strs, key=len)
            for i, c in enumerate(shortest):
                for other in strs:
                    if other[i] != c:
                        return shortest[:i]
            return shortest

        def fxr():
            """
            Runtime: 47 ms, faster than 26.27% of Python3 online submissions for Longest Common Prefix.

            T: O(N*minL)
            """
            N = len(strs)
            ans = 0
            while True:
                vs = set()
                for i in range(N):
                    if ans >= len(strs[i]):
                        return strs[0][:ans]
                    v = strs[i][ans]
                    vs.add(strs[i][ans])
                    if len(vs) >= 2:
                        return strs[0][:ans]
                ans += 1
            return strs[0][:ans]

        return fxr()


sl = Solution()
print(sl.longestCommonPrefix(strs=["flower", "flow", "flight"]))
print(sl.longestCommonPrefix(strs=["dog", "racecar", "car"]))
