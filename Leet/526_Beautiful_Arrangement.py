"""

✅ GOOD DP (subsets)
Problem 465 Optimal Account Balancing
Problem 473 Matchsticks to Square
Problem 698 Partition to K Equal Sum Subsets
Problem 847 Shortest Path Visiting All Nodes]
Problem 854 K-Similar Strings
Problem 943 Find the Shortest Superstring
Problem 1434 Number of Ways to Wear Different Hats to Each Other
Problem 1494 Parallel Courses II
Problem 1655 Distribute Repeating Integers
Problem 1659 Maximize Grid Happiness
Problem 1681. Minimum Incompatibility
"""
from collections import defaultdict
from functools import cache


class Solution:
    def countArrangement(self, n: int) -> int:
        def dbabichev_bitmask():
            """
            Runtime: 108 ms, faster than 90.79% of Python3 online submissions for Beautiful Arrangement.

            https://leetcode.com/problems/beautiful-arrangement/discuss/1000132/Python-DP-%2B-bitmasks-explained
            T: O(N*2^N)
            """

            @cache
            def dfs(bm, place):
                """
                bm is binary mask for visited numbers.
                pl is current place we want to fill.
                XXX: Idea is to start from the end, and fill places in opposite direction, because for big numbers we potentially have less candidates.
                """
                if place == 0:
                    print(bm, f"{bm:b}")
                    return 1
                S = 0
                for i in range(n):  # try all number (i+1) in [1,2,3..n]
                    if not bm & (1 << i) and (
                        (i + 1) % place == 0 or place % (i + 1) == 0
                    ):  # pl is the place to fill number (i+1) in perm list
                        S += dfs(bm ^ (1 << i), place - 1)
                return S

            return dfs(0, n)

        return dbabichev_bitmask()

        def fxr_bt():
            """[summary]
            Runtime: 2017 ms, faster than 21.48% of Python3 online submissions for Beautiful Arrangement.
            T: O(N!)
            """
            sn = set(range(1, n + 1))

            def bt(idx, used, path, res):
                if idx == n + 1:
                    res.append(path[:])
                    return
                for i in sn - used:
                    if not (i % idx == 0 or idx % i == 0):
                        continue
                    used.add(i)
                    bt(idx + 1, used, path + [i], res)
                    used.discard(i)

            res = []
            bt(1, set(), [], res)
            return len(res)

        return fxr_bt()


sl = Solution()
# print(sl.countArrangement(n=2))
# print(sl.countArrangement(n=1))
# print(sl.countArrangement(n=3))
print(sl.countArrangement(n=5))
