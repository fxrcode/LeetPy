"""
https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
Leetcode explore Array 101: Searching for items in array

Given an array of integers arr, return true if and only if it is a valid mountain array.

"""


from typing import List


class Solution:
    def validMountainArray_official_sol(self, arr: List[int]) -> bool:
        """
        Official solution is simple and 1-pass
        """
        n = len(arr)
        i = 0
        # climb up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        # peek can't be the first or the last
        if i == 0 or i == n - 1:
            return False
        # climb down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        return i == n - 1

    def validMountainArray_lee215(self, arr: List[int]) -> bool:
        """
        lee215 is always the best: https://leetcode.com/problems/valid-mountain-array/discuss/194900/C%2B%2BJavaPython-Climb-Mountain
        Your runtime beats 76.52 % of python3 submissions.
        XXX: CRUX: let 2 ppl climb from both ends, they'll meet at the peak!
        """
        i, j, n = 0, len(arr) - 1, len(arr)
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        while j > 0 and arr[j] < arr[j - 1]:
            j -= 1
        return 0 < i == j < n - 1

    def validMountainArray_fxr(self, arr: List[int]) -> bool:
        """
        Runtime: 224 ms, faster than 30.39% of Python3 online submissions for Valid Mountain Array.
        AC in 1st try
        Slow due to O(N) to find peak, then O(K) to climb up, and O(N-K) to climb down, so T:O(2N)
        """
        pi = 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            if arr[i + 1] > arr[pi]:
                pi = i + 1
        if pi == 0 or pi == len(arr) - 1:
            return False
        for i in range(pi):
            if arr[i] > arr[i + 1]:
                return False
        for i in range(pi, len(arr) - 1):
            if arr[i] < arr[i + 1]:
                return False
        return True

    """
    BUG: failed [0,3,2,1]
    def validMountainArray(self, arr: List[int]) -> bool:
        up = True
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
            if up:
                if arr[i] < arr[i+1]:
                    continue
                else:
                    up = False
            else:
                if arr[i] > arr[i+1]:
                    continue
                else:
                    return False
        return False
    """
