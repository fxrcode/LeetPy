'''
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
'''


from typing import List
from collections import deque


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def fxr(A: list[int]):
            """
            Runtime: 792 ms, faster than 38.59% of Python3 online submissions for Maximum Length of Subarray With Positive Product.

            REF: https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/discuss/820072/EASY-soultion-with-DRY-RUN-JAVA
            AC in 2.
            """
            N = len(A)
            # F means (max_neg, max_pos) including A[i]
            F = [[0, 0] for _ in range(N)]
            if A[0] < 0:
                F[0] = [1, 0]
            if A[0] > 0:
                F[0] = [0, 1]
            ans = F[0][1]

            for i in range(1, N):
                max_neg, max_pos = F[i-1]
                if A[i] == 0:
                    F[i] = [0, 0]
                elif A[i] > 0:
                    F[i][1] = max_pos + 1
                    if max_neg > 0:
                        F[i][0] = max_neg + 1
                else:  # A[i] < 0
                    F[i][0] = max_pos + 1
                    if max_neg > 0:
                        F[i][1] = max_neg + 1

                ans = max(ans, F[i][1])

            print(F)
            return ans

        return fxr(nums)


sl = Solution()
print(sl.getMaxLen(nums=[1, -2, -3, 4]))
print(sl.getMaxLen(nums=[0, 1, -2, -3, -4]))
print(sl.getMaxLen(nums=[-1, -2, -3, 0, 1]))
print(sl.getMaxLen([-1, 2]))
print(sl.getMaxLen(nums=[1, 2, 3, 5, -6, 4, 0, 10]))
'''
def slide_win():
    l, r = 0, 0
    N = len(nums)
    win = deque()
    ans = 0
    neg_cnt = 0
    while r < N:
        c = nums[r]
        r += 1
        win.append(c)
        if c == 0:
            r = r+1
            l = r
            continue
        if c < 0:
            neg_cnt += 1
        while l < r and neg_cnt :
            d = nums[l]
            l += 1
            if d < 0:
                neg_cnt -= 1
'''
