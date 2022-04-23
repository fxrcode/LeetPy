"""
tag: Medium, Hash
Lookback:
- bad in counting & combinations
"""

from collections import Counter
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def tbvho():
            """
            Runtime: 512 ms, faster than 59.41% of Python3 online submissions for Number of Ways Where Square of Number Is Equal to Product of Two Numbers.

            https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/discuss/831642/Python3-or-Using-Counter
            """
            F1, F2 = Counter([n**2 for n in nums1]), Counter([n**2 for n in nums2])

            def aggregateType(nums, F):
                total = 0
                for i in range(len(nums)):
                    for j in range(i + 1, len(nums)):
                        target = nums[i] * nums[j]
                        total += F[target]
                return total

            return aggregateType(nums1, F2) + aggregateType(nums2, F1)

        return tbvho()

        """
        def fxr_WA():
            F1, F2 = Counter(nums1), Counter(nums2)
            typ1, typ2 = 0, 0

            def calc(F1, F2):
                cnt = 0
                for a in F1:
                    for b in F2:
                        if a * a % b == 0 and a * a // b in F2:
                            if a == b:
                                print(a, b)
                                cnt += F1[a] * F2[b] * (F2[b] - 1) // 2
                            else:
                                print(a, b)
                                cnt += F1[a] * F2[b] * F2[a * a // b] // 2
                return cnt

            typ1 = calc(F1, F2)
            typ2 = calc(F2, F1)
            print(typ1, typ2)
            return typ1 + typ2
        """


sl = Solution()
# print(sl.numTriplets(nums1=[7, 4], nums2=[5, 2, 8, 9]))
# print(sl.numTriplets(nums1=[1, 1], nums2=[1, 1, 1]))
print(sl.numTriplets(nums1=[7, 7, 8, 3], nums2=[1, 2, 9, 7]))
