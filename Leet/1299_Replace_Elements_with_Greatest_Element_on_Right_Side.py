"""
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
leetcode explore: Array 101. In-place operations

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""


from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        AC in 1st try
        Your runtime beats 93.20 % of python3 submissions.
        """
        mx = -1  # represents the max on the right
        for i in range(len(arr) - 1, -1, -1):
            tmp_ai = arr[i]
            arr[i] = mx
            mx = max(mx, tmp_ai)
        return arr


sl = Solution()
print(sl.replaceElements([17, 18, 5, 4, 6, 1]))
