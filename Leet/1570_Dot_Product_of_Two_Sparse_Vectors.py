"""
FB tag (medium)
tag: medium, hash
Lookback:
- if you have the index, you can get val. Mark all non-zero value's index
"""

from typing import List


class SparseVector:
    """
    Runtime: 1752 ms, faster than 89.08% of Python3 online submissions for Dot Product of Two Sparse Vectors.

    T: O(n+m) for init, O(min(m,n)) for dotProduct
    """

    def __init__(self, nums: List[int]):
        self.nz = set()
        self.nums = nums
        for i, v in enumerate(nums):
            if v:
                self.nz.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        nz = self.nz.intersection(vec.nz)
        ans = 0
        for i in nz:
            ans += self.nums[i] * vec.nums[i]
        return ans
