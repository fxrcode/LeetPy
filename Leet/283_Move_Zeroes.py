"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, skills
Lookback:
- practice!!!

https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
leetcode explore: Array 101. In-place operations
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1174/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""


from typing import List


class Solution:
    def moveZerosToRight(self, A: List[int]) -> None:
        """
        Runtime: 295 ms, faster than 32.13% of Python3 online submissions for Move Zeroes.

        XXX: so partition is stable!
        """
        nz = -1
        # loop invariant: [0:nz] != 0
        for i, a in enumerate(A):
            if a != 0:
                nz += 1
                A[i], A[nz] = A[nz], A[i]
        print(A)

    def moveZerosToLeft(self, arr: List[int]) -> None:
        z = 0
        # loop-invariant: [0:cout] = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[i], arr[z] = arr[z], arr[i]
                z += 1
        print(arr, z)

    def minSwap_Amazon(self, arr: List[int]) -> None:
        """
        Simplier than the original Leetcode
        Amazon OA: given int array. What's the minmum swap to bring all 0's to left or right?
        eg.[1,0,2,0,0,3,0] if move all 0 to right, costs
        """
        # self.moveZerosToLeft(arr[:])
        # self.moveZerosToRight(arr[:])
        # move non-zero to right
        zeros, swaps = 0, 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == 0:
                zeros += 1
            else:
                swaps += zeros
        print("all non-zeros right:", swaps)

        zeros, swaps = 0, 0
        for i in range(len(arr)):
            if arr[i] == 0:
                zeros += 1
            else:
                swaps += zeros
        print("all non-zeros left:", swaps)


sl = Solution()
sl.moveZerosToRight([0, 1, 0, 3, 12])
sl.moveZerosToRight([1, 0, 2, 3, 0, 4, 5, 0])
# sl.moveZerosToLeft([1, 0, 2, 3, 0, 4, 5, 0])
# sl.minSwap_Amazon([1, 0, 2, 0, 0, 3, 0])
