"""
tag: Medium, Sort
Lookback:
- when sort list in range, use counting sort
- careful in aux list size
"""

from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        def os_counting():
            """
            Runtime: 1599 ms, faster than 43.87% of Python3 online submissions for Minimize Product Sum of Two Arrays.

            T: O(N)
            """
            counter1, counter2 = [0] * 101, [0] * 101
            m, n = len(nums1), len(counter1)

            # fill buckets
            for i in range(m):
                counter1[nums1[i]] += 1
                counter2[nums2[i]] += 1

            # meet in the middle and multiply at each end
            p1, p2, prod_sum = 0, n - 1, 0
            while 0 < p2 and p1 < n:
                while p1 < n and not counter1[p1]:
                    p1 += 1
                while 0 < p2 and not counter2[p2]:
                    p2 -= 1
                if 0 < p2 and p1 < n and counter1[p1] and counter2[p2]:
                    occ = min(counter1[p1], counter2[p2])
                    prod_sum += occ * p1 * p2
                    counter1[p1] -= occ
                    counter2[p2] -= occ
            return prod_sum

        return os_counting()

        def fxr():
            """
            Runtime: 1507 ms, faster than 53.38% of Python3 online submissions for Minimize Product Sum of Two Arrays.

            """
            nums1.sort(reverse=True)
            nums2.sort()
            sm = 0
            for i in range(len(nums1)):
                sm += nums1[i] * nums2[i]
            return sm

        return fxr()


sl = Solution()
print(sl.minProductSum(nums1=[5, 3, 4, 2], nums2=[4, 2, 2, 5]))
print(sl.minProductSum(nums1=[2, 1, 4, 5, 7], nums2=[3, 2, 4, 8, 6]))
