"""
Tag: Easy, Logic
Lookback:
- similar logic to #277
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

"""


from random import randint
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def boyce_moore():
            """
            Runtime: 164 ms, faster than 83.12% of Python3 online submissions for Majority Element.

            REF: OS Boyer-Moore Voting Algorithm
            """
            count = 0
            candidate = None
            for n in nums:
                if count == 0:
                    candidate = n
                count += 1 if n == candidate else -1
            return candidate

        def fxr_qselect():
            def swap(nums, i1, i2):
                nums[i1], nums[i2] = nums[i2], nums[i1]

            def partition(lo, hi):
                # loop invariant: [:k] < pivot, [k] == pivot, [k+1:] > pivot
                swap(nums, randint(lo, hi), hi)
                p = nums[hi]
                l = lo - 1
                for i in range(lo, hi):
                    if nums[i] < p:
                        l += 1
                        swap(nums, l, i)
                swap(nums, l + 1, hi)
                return l + 1

            def qselect(k, l, r):
                if l == r:
                    return nums[l]
                pi = partition(l, r)
                if pi == k:
                    return nums[k]
                elif pi < k:
                    return qselect(k, pi + 1, r)
                else:
                    return qselect(k, l, pi - 1)

            return qselect(len(nums) // 2, 0, len(nums) - 1)

        return fxr_qselect()


sl = Solution()
print(sl.majorityElement([3, 3]))
print(sl.majorityElement([3, 2, 3]))
print(sl.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2]))
