"""
每日一题打卡群 (12/6/2021)
"""
from typing import List
from collections import defaultdict


class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        def idontknoooo_presuffix():
            """
            Runtime: 903 ms, faster than 6.52% of Python3 online submissions for Binary Searchable Numbers in an Unsorted Array.

            https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/discuss/1398483/Python-3-or-Prefix-Array-Two-Pass-Quick-Sort-or-Explanation
            T: O(N)
            """
            ans, n = 0, len(nums)
            prefix = [False] * n
            cur_mx, cur_mn = nums[0], nums[-1]
            for i in range(n):
                prefix[i] = cur_mx <= nums[i]
                cur_mx = max(cur_mx, nums[i])
            for i in range(n - 1, -1, -1):
                found = prefix[i] & (cur_mn >= nums[i])
                ans += found
                cur_mn = min(cur_mn, nums[i])
            return ans

        def binarySearchableNumbers_FollowUp(self, nums: List[int]) -> int:
            """
            [Python 3] Follow-up in O(n)
            REF: https://leetcode.com/problems/binary-searchable-numbers-in-an-unsorted-array/discuss/1398841/Python-3-Follow-up-in-O(n)
            """
            n = len(nums)
            inf = 1e6
            lt = lambda a, b: a < b
            gt = lambda a, b: a > b

            def generate_next(it, cond, ret):
                stk = []
                for idx in it:
                    while stk and cond(nums[idx], nums[stk[-1]]):
                        ret[stk.pop()] = idx
                    stk.append(idx)
                return ret

            next_smaller = generate_next(range(n), lt, [inf] * n)
            prev_larger = generate_next(reversed(range(n)), gt, [-inf] * n)

            value_indices = defaultdict(list)

            for i, x in enumerate(nums):
                value_indices[x].append(i)

            def guaranteed(x, indices):

                # Lxxx
                if prev_larger[indices[0]] >= 0:
                    return False

                # xxxSLxxx
                for i, j in zip(indices, indices[1:]):
                    if next_smaller[i] < prev_larger[j]:
                        return False

                # xxxS
                if next_smaller[indices[-1]] < n:
                    return False

                return True

            return sum(map(guaranteed, value_indices.keys(), value_indices.values()))
