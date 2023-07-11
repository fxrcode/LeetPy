"""
Weekly Contest 269 (Nov 27, 2021)
"""

from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn_id = nums.index(min(nums))
        mx_id = nums.index(max(nums))
        N = len(nums)

        if mn_id == mx_id:
            return 1

        l = min(mn_id, mx_id)
        r = max(mn_id, mx_id)
        del_lr = l + 1 + N - r
        del_l = r + 1
        del_r = N - l
        return min(del_lr, del_l, del_r)
