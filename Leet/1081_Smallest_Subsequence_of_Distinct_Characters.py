"""
✅ GOOD Stack
✅ GOOD Greedy
tag: medium, stack
Lookback:
TuSimple Phone!
A bit change: was asked Largest rather smallest

[ ] REDO
Similar:
lexicographically order: 1663...
stack
1130 Minimum Cost Tree From Leaf Values
907 Sum of Subarray Minimums
901 Online Stock Span
856 Score of Parentheses
503 Next Greater Element II
496 Next Greater Element I
84 Largest Rectangle in Histogram
42 Trapping Rain Water
"""


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        def lee215_mono():
            """
            Runtime: 28 ms, faster than 90.26% of Python3 online submissions for Smallest Subsequence of Distinct Characters.

            meta: same idea as 316
            """
            mono = []
            last = {c: i for i, c in enumerate(s)}
            instk = set()
            for i, c in enumerate(s):
                if c in instk:
                    continue
                while mono and mono[-1] > c:
                    if last[mono[-1]] > i:
                        instk.remove(mono.pop())
                    else:
                        break

                mono.append(c)
                instk.add(c)
            return "".join(mono)

        return lee215_mono()


sl = Solution()
print(sl.smallestSubsequence(s="cbacdcbc"))
