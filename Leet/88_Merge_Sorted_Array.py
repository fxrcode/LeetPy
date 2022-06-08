"""
Tag: Easy, 2ptr, Skills
Lookback:
- practice more in clean code
- daily challenge like 160
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Similar Questions: <- 986. Interval List Intersections
        merge nums1 and nums2, and result stored in nums1.
        Do not return anything, modify nums1 in-place instead.
        """

        def os_clean():
            """
            Crux: the devil is in the details: how to unify logic?
            """
            i, j = m - 1, n - 1
            for p in range(m + n - 1, -1, -1):
                if j < 0:
                    break
                if i >= 0 and nums1[i] > nums2[j]:
                    nums1[p] = nums1[i]
                    i -= 1
                else:
                    nums1[p] = nums2[j]
                    j -= 1
            print(nums1)

        return os_clean()


sl = Solution()
sl.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
