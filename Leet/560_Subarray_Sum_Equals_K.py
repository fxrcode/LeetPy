"""
Daily Challenge (Feb 9, 2022)
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

437. Path Sum III's OS : Prefix Sum technique介绍的入门题
tag: medium, prefix-sum, hash
"""

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Your runtime beats 68.05 % of python3 submissions.

        REF: https://leetcode.com/problems/path-sum-iii/solution/
        As a prerequisite for 437. Path Sum III's prefix-sum.
        """
        count = cur_sum = 0
        h = defaultdict(int)

        for n in nums:
            cur_sum += n
            # situation 1: subarray from beginning
            if cur_sum == k:
                count += 1

            # situation 2: subarray in the middle of array, rather start from beginning
            count += h[cur_sum - k]

            # add the current sum
            h[cur_sum] += 1
        return count
