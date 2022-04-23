"""
✅ GOOD Hash
FB tag
tag: easy

Lookback:
- # of dict.keys() as rank!
"""
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        def one_liner():
            """
            Runtime: 336 ms, faster than 96.52% of Python3 online submissions for Rank Transform of an Array.

            https://leetcode.com/problems/rank-transform-of-an-array/discuss/492212/Python-3-(two-lines)-(beats-~100)
            """
            ranks = {n: i + 1 for i, n in enumerate(sorted(set(arr)))}
            return map(ranks.get, arr)

        def lee215():
            """
            Runtime: 529 ms, faster than 37.07% of Python3 online submissions for Rank Transform of an Array.

            https://leetcode.com/problems/rank-transform-of-an-array/discuss/489753/JavaC%2B%2BPython-HashMap

            T: O(NlogN), M: O(N)
            """
            rank = {}
            for a in sorted(arr):
                rank.setdefault(a, len(rank) + 1)
            return list(map(rank.get, arr))

        return lee215()

        def fxr():
            """
            Runtime: 424 ms, faster than 57.51% of Python3 online submissions for Rank Transform of an Array.
            T: O(NlogN), M: O(N)
            """
            if not arr:
                return []
            vi = sorted([(v, i) for i, v in enumerate(arr)])
            ans = [None] * len(arr)
            pre = vi[0][0] - 1
            rank = 0
            for v, i in vi:
                if v == pre:
                    ans[i] = rank
                else:
                    rank += 1
                    ans[i] = rank
                    pre = v
            return ans


sl = Solution()
print(sl.arrayRankTransform(arr=[40, 10, 20, 30]))
print(sl.arrayRankTransform(arr=[100, 100, 100]))
