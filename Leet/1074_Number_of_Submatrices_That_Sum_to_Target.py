"""
Tag: Hard, presum
Lookback:
- daily: 20220718
- Preaquis: 560. Subarray Sum Equals K
- presum: careful index (range, base, etc), base-case {0:1}
"""

from typing import List


class Solution:
    def numSubmatrixSumTarget(self, M: List[List[int]], target: int) -> int:
        def otoc_prefixsum():
            """
            Runtime: 1117 ms, faster than 76.78% of Python3 online submissions for Number of Submatrices That Sum to Target.

            """
            m, n = len(M), len(M[0])
            for x in range(m):
                for y in range(n - 1):
                    M[x][y + 1] += M[x][y]
            res = 0
            for y1 in range(n):
                for y2 in range(y1, n):
                    presum = {0: 1}
                    s = 0
                    for x in range(m):
                        s += M[x][y2] - (M[x][y1 - 1] if y1 > 0 else 0)
                        res += presum.get(s - target, 0)
                        presum[s] = presum.get(s, 0) + 1
            return res

        return otoc_prefixsum()


sl = Solution()
print(sl.numSubmatrixSumTarget(M=[[1, -1], [-1, 1]], target=0))
