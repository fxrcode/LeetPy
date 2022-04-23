'''
https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1040/
Leetcode Explore: Binary Search - More Practice
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''


from typing import List

INF = 1e9


class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        """
        Runtime: 96 ms, faster than 59.89% of Python3 online submissions for Median of Two Sorted Arrays.

        XXX: Neetcode analysis thinking flow and coding are so intuitive and good!

        """
        m, n = len(A), len(B)
        if m > n:
            return self.findMedianSortedArrays(B, A)
        total = m+n
        half = total // 2

        l, r = 0, m-1
        # while l < r:
        while True:
            i = (l+r)//2    # A mid
            j = half-(i+1)-1  # B pointer

            A_left = A[i] if i >= 0 else -INF
            A_right = A[i+1] if (i+1) < m else INF
            B_left = B[j] if j >= 0 else -INF
            B_right = B[j+1] if (j+1) < n else INF

            # correctly partitioned!
            if A_left <= B_right and B_left <= A_right:
                # odd
                if total % 2:
                    return min(A_right, B_right)
                # even
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

            elif A_left > B_right:
                r = i - 1
            else:  # Neet video @10:50
                l = i + 1


sl = Solution()
print(sl.findMedianSortedArrays(A=[1, 3], B=[2]))
print(sl.findMedianSortedArrays(A=[1, 3], B=[2, 4]))
