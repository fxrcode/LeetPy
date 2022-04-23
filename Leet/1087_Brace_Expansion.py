"""
tag: Medium, Backtrack
Lookback:
- How to get dfs/backtrack Time complexity? T: O(N * 3^{N/7})
- not familiar w/ backtrack
[ ] REDO
"""

from typing import List


class Solution:
    def expand(self, s: str) -> List[str]:
        def fxr():
            """
            Runtime: 40 ms, faster than 88.32% of Python3 online submissions for Brace Expansion.

            """

            def bt(i, path, res):
                if i == len(s):
                    res.append("".join(path))
                    return
                if s[i] not in "{}":
                    # still do single char choice! think about DFS tree
                    bt(i + 1, path + [s[i]], res)
                if s[i] == "{":
                    j = s.index("}", i + 1)
                    opt = s[i + 1 : j].split(",")
                    opt.sort()
                    for c in opt:
                        bt(j + 1, path + [c], res)

            res = []
            bt(0, [], res)
            return res

        return fxr()


sl = Solution()
print(sl.expand(s="{a,b}c{d,e}f"))
print(sl.expand(s="abcd"))
assert sl.expand("{a,b}{z,x,y}") == ["ax", "ay", "az", "bx", "by", "bz"]
