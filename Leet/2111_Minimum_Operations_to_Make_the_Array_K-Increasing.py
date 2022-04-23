'''
Weekly Contest 272 (Dec 18, 2021)

Q4: LIS in Disguise

Lookback:
- LIS variant: Longest Non-Decreasing Subsequence

similar:
- 300. Longest Increasing Subsequence
- 1909.Remove One Element to Make the Array Strictly Increasing
'''

from typing import List
from bisect import bisect_right


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def klis():
            """
            Runtime: 1060 ms, faster than 93.38% of Python3 online submissions for Minimum Operations to Make the Array K-Increasing.

            Longest Non-Decreasing Subsequence
            https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/discuss/1635013/C%2B%2BPython-Longest-Non-Decreasing-Subsequence-Clean-and-Concise
            """
            ops = 0
            for ki in range(k):
                lis = []
                cnt = 0
                for i in range(ki, len(arr), k):
                    cnt += 1
                    x = arr[i]
                    if not lis or lis[-1] <= x:
                        lis.append(x)
                    else:
                        j = bisect_right(lis, x)
                        lis[j] = x
                ops += cnt - len(lis)
            return ops

        return klis()


sl = Solution()
print(sl.kIncreasing(arr=[5, 4, 3, 2, 1], k=1))
print(sl.kIncreasing(arr=[4, 1, 5, 2, 6, 2], k=2))
print(sl.kIncreasing(arr=[4, 1, 5, 2, 6, 2], k=3))
