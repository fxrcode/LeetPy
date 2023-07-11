"""
✅ GOOD Backtrack (multi-state)
kevin: partition-type problem (Backtrack/DP)

tag: medium, backtrack, DP

lookback:
- get strong in dfs w/ args & return
"""


class Solution:
    def splitString(self, s: str) -> bool:
        def archit91():
            """
            Runtime: 47 ms, faster than 45.23% of Python3 online submissions for Splitting a String Into Descending Consecutive Values.

            XXX: real backtrack rather template! cuz we need these info to judge!
            """

            def solve(s, i, l, prev, splits):
                """[summary]

                Args:
                    s : const s
                    i : start index
                    l : substr len
                    prev : last cut value
                    splits: last splits

                Returns:
                    bool: if there's valid splits to fulfill requirements
                """
                if i == len(s) and splits >= 2:
                    return True
                while i + l <= len(s):
                    cur = int(s[i : i + l])
                    l += 1
                    if prev != -1 and cur != prev - 1:
                        continue
                    if solve(s, i + l - 1, 1, cur, splits + 1):
                        return True
                return False

            return solve(s, 0, 1, -1, 0)

        return archit91()

        def fxr_bt():
            """
            Runtime: 57 ms, faster than 26.32% of Python3 online submissions for Splitting a String Into Descending Consecutive Values.

            """

            def bt(s, path, res):
                print(s, path, res)
                if not s:
                    res.append(path[:])
                    return
                for i in range(1, len(s) + 1):
                    cut = s[:i]
                    if not cut:
                        continue
                    if not path or int(cut) + 1 == path[-1]:
                        bt(s[i:], path + [int(cut)], res)

            res = []
            bt(s, [], res)
            print(res)
            return len(res) > 1


sl = Solution()
s = "050043"
# s = "9080701"
print(sl.splitString(s))
