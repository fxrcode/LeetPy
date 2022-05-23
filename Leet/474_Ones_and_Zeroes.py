"""
✅ GOOD DP (Knapsack)
Tag: Medium, DP
Lookback:
- I knew its knapsack and I've got state (i,z,o), but stuck on return len,z,o, and choosing prefix vs suffix subproblems...
Similar:
Bounded 0/1 Knapsack problems
LC 416. Partition Equal Subset Sum
LC 494. Target Sum
LC 474. Ones and Zeroes
LC 343. Integer Break

Unbounded 0/1 Knapsack problems
LC 322. Coin Change
LC 518. Coin Change 2
LC 377. Combination Sum IV
LC 983. Minimum Cost For Tickets
"""
from functools import cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def dbabichev_knapsack():
            """
            Runtime: 2921 ms, faster than 87.02% of Python3 online submissions for Ones and Zeroes.

            https://leetcode.com/problems/ones-and-zeroes/discuss/1138534/Python-short-dp-explained
            T: O(mnk)
            """
            xy = [(s.count("0"), s.count("1")) for s in strs]

            @cache
            def dp(mm, nn, kk):
                """
                The order of two conditions matter. ow, it fails with test case:
                ["10","0001","111001","1","0"]
                4
                3
                """
                if mm < 0 or nn < 0:
                    return float("-inf")
                if kk == len(strs):
                    return 0
                z, o = xy[kk]
                return max(1 + dp(mm - z, nn - o, kk + 1), dp(mm, nn, kk + 1))

            return dp(m, n, 0)

        return dbabichev_knapsack()


sl = Solution()
print(sl.findMaxForm(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
