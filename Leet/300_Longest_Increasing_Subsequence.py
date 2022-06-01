"""
✅ GOOD DP (LIS)
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 8: DP on String

similar:
- LIS in Disguise: 2111. Minimum Operations to Make the Array K-Increasing
- 673
- 354 (2D LIS)

"""
from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def fxr_dp():
            """
            Runtime: 4448 ms, faster than 14.31% of Python3 online submissions for Longest Increasing Subsequence.

            # https://stackoverflow.com/questions/30356892/defaultdict-with-default-value-1

            [ ] REDO. Must be familiar with classic DP! LCS/LIS/EditDist/Tiling/SSSP/Coin/SubsetSum
            O: T(n^2)
            """
            # T, m = defaultdict(lambda: 1), len(nums)
            m = len(nums)
            T = {i: 1 for i in range(m)}
            for i in range(1, m):
                for j in range(i):
                    if nums[i] > nums[j]:
                        T[i] = max(T[i], T[j] + 1)
                # T[i] = max([T[j] for j in range(i) if nums[i] > nums[j]] + [0]) + 1
            print(T)
            return max(T.values())

        def os_patience():
            """
            Runtime: 64 ms, faster than 96.47% of Python3 online submissions for Longest Increasing Subsequence.

            Check cos423's LIS to understand Patience solitaire
            https://www.cs.princeton.edu/courses/archive/spring18/cos423/lectures/LongestIncreasingSubsequence-2x2.pdf

            T: O(nlogn)
            """
            sub = []
            for n in nums:
                i = bisect_left(sub, n)
                # if n is greater than any element in sub
                if i == len(sub):
                    sub.append(n)

                # ow, replace the first elem in sub >= n
                else:
                    sub[i] = n
            return len(sub)

        return os_patience()


sl = Solution()
# print(sl.lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
# print(sl.lengthOfLIS(nums=[0, 1, 0, 3, 2, 3]))
print(sl.lengthOfLIS(nums=[7, 7, 7, 7, 7]))
