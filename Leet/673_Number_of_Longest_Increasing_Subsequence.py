"""
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 9: DP on String

[ ] REDO: simplify logic/code
"""
from collections import defaultdict
from heapq import heappop, heappush
from typing import List

"""
class Mxheap:
    def __init__(self) -> None:
        self.heap = []

    def push(self, tu):
        mxlen, cnt = tu
        neg_tu = [-mxlen, cnt]
        heappush(self.heap, neg_tu)

    def pop(self):
        neg_maxlen, cnt = heappop(self.heap)
        return [-neg_maxlen, cnt]

    def top(self):
        neg_maxlen, cnt = self.heap[0]
        return -neg_maxlen

    def empty(self):
        return len(self.heap) == 0
"""


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        def os_dp():
            """
            based upon #300 (LIS)
            T: O(N^2)
            """

        def fxr():
            """
            Runtime: 1400 ms, faster than 50.41% of Python3 online submissions for Number of Longest Increasing Subsequence.


            AC in 1 (30min)

            metacognition:
            * It's LIS! LIS is O(n^2).
            * Dummy use of LIS to find length, then query each subsequence for that length?? Seems not, since subsequence is exponential
            * review LIS, we need to get largest T[k] that k < i. so we can cnt how mnay largest T[k]!
            * was thinking to create maxheap to get top T[j] with same maxlen, so O(N) for heapify, but too complicate
            """

            T = defaultdict(lambda: [1, 1])
            T[-1] = [0, 0]
            m = len(nums)
            for i in range(1, m):
                Tjs = []
                # BUG: always mistakenly wrote `range(i-1)`! NO! j is less than i so range(i)!!!
                for j in range(i):
                    if nums[i] > nums[j]:
                        Tjs.append(T[j])
                if not Tjs:
                    continue
                Tjs.sort(key=lambda tu: -tu[0])
                # print(i, j, Tjs)
                mxlen, cnt = Tjs[0][0], 0
                for tu in Tjs:
                    if tu[0] == mxlen:
                        cnt += tu[1]
                    else:
                        break
                T[i] = [mxlen + 1, cnt]

            mxlis = max([T[i] for i in range(m)], key=lambda tu: (tu[0]))
            # print(T)
            # return mxlis[1]
            total = sum([tu[1] for tu in T.values() if tu[0] == mxlis[0]])
            # print(mxlis, total)
            return total

        return fxr()


sl = Solution()
sl.findNumberOfLIS(nums=[1, 3, 5, 4, 7])
sl.findNumberOfLIS(nums=[2, 2, 2, 2, 2])
