"""
https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
Leetcode explore: Array 101
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

XXX: many similar questions of in-place shifting values in array. Common use of 2 pointers.
"""


from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        https://leetcode.com/problems/duplicate-zeros/discuss/322576/Python-3-real-in-place-solution
        XXX: Crux is to generalize count of zeros, then shift non-zero once, and zero twice
        """
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    # XXX: move non-zero 1 time, and zero twice because we need duplicate zeros
                    arr[i + zeros] = 0

    def duplicateZeros_fxr(self, arr: List[int]) -> None:
        """
        Runtime: 68 ms, faster than 84.14% of Python3 online submissions for Duplicate Zeros.
        AC in 1st try. But this easy problem took me 25min to code up.
        """
        N = len(arr)
        zeros = 0

        i = N - 1
        while i >= 0 and arr[i] == 0:
            i -= 1
        if i == -1:
            return arr
        # found right most non-zero's index
        for j in range(i):
            if arr[j] == 0:
                zeros += 1
        print(i, zeros)
        for k in range(i, -1, -1):
            if zeros == 0:
                return
            if arr[k] != 0:
                if k + zeros >= N:
                    arr[k] = 0
                else:
                    nk = k + zeros
                    arr[nk] = arr[k]
                    arr[k] = 0
            else:
                zeros -= 1


sl = Solution()
arr = [1, 0, 2, 3, 0, 4, 5, 0]
# arr = [1, 2, 3]
# arr = [0, 1, 0, 0, 2, 0, 3, 0, 0, 0]
sl.duplicateZeros(arr)
print(arr)
