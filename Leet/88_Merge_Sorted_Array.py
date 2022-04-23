from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Similar Questions: <- 986. Interval List Intersections
        merge nums1 and nums2, and result stored in nums1.
        Do not return anything, modify nums1 in-place instead.

        Args:
            nums1 (List[int]): [non-desc order], size= m+n, the rest n is filled with 0
            m (int): [# elements]
            nums2 (List[int]): [non-desc order]
            n (int): [# elements]
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

sl = Solution()
sl.merge(nums1, m, nums2, n)
print(nums1)
