"""
tag: medium, DP, DFS
Lookback:
- bad in counting & combinations
"""
from functools import cache
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        def fxr():
            """
            Runtime: 376 ms, faster than 92.56% of Python3 online submissions for Binary Trees With Factors.

            """
            arr.sort()
            d = {n: i for i, n in enumerate(arr)}
            MOD = 10**9 + 7

            @cache
            def dp(i):
                root = arr[i]
                cnt = 1
                for x in arr[:i]:
                    if root % x == 0 and root // x in d:
                        """
                        BUG: no need to separate equal vs ineuqal subroots cases!
                        check huahua
                        if x * x == root:
                            cnt += dp(d[x])
                        else:
                        """
                        cnt += dp(d[x]) * dp(d[root // x])
                return cnt % MOD

            return sum(dp(i) for i in range(len(arr))) % MOD

        return fxr()


sl = Solution()
# print(sl.numFactoredBinaryTrees(arr=[2, 4]))
print(sl.numFactoredBinaryTrees(arr=[2, 4, 5, 10]))
