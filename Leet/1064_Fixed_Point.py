'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        def fxr_binary():
            """
            Your runtime beats 100.00 % of python3 submissions.

            AC in 1 with 100% beats!

            lee215 Easy prove A[x]-x is non-decending
            A[i] < A[i + 1]
            => A[i] <= A[i + 1] - 1
            ==> A[i] - i <= A[i + 1] - i - 1

            """
            # XXX: careful! I always forgot r = len(arr)-1! missing the '-1'
            l, r = 0, len(arr)-1
            while l < r:
                mid = (l+r)//2
                if arr[mid] - mid >= 0:
                    r = mid
                else:
                    l = mid + 1
            if arr[l] != l:
                return -1
            return l

        def fxr_brute():
            for i, v in enumerate(arr):
                if i == v:
                    return i
            return -1

        return fxr_binary()


sl = Solution()
print(sl.fixedPoint(arr=[-10, -5, 0, 3, 7]))
print(sl.fixedPoint(arr=[0, 2, 5, 8, 17]))
print(sl.fixedPoint(arr=[-10, -5, 3, 4, 7, 9]))
print(sl.fixedPoint([-10]))
