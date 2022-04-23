'''
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1178/
Leetcode Explore: Hash Table. Practical Application - HashMap

https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1029/
Leetcode Explore: Binary Search - Conclusion

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Follow up:
1) What if the given array is already sorted? How would you optimize your algorithm?
2) What if nums1's size is small compared to nums2's size? Which algorithm is better?
3) What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

'''


from typing import List
from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 36 ms, faster than 99.30% of Python3 online submissions for Intersection of Two Arrays II.

        thinking about algs by optimizing complexity. Say, M: O(N+M) -> O(1). We can sort and then 2 pointers.
        """
        res = []
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:  # ==
                res.append(nums1[i])
                i += 1
                j += 1
        return res

    def intersect_sol_dict(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Your runtime beats 89.14 % of python3 submissions.

        https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82247/Three-Python-Solutions
        Much cleaner code to use dict!
        """
        counts = {}
        res = []
        for n in nums1:
            counts = counts.get(n, 0) + 1
        for n in nums2:
            if n in counts and counts[n] > 0:
                res.append(n)
                counts[n] -= 1
        return res

    def intersect_fxr(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 98 ms, faster than 9.12% of Python3 online submissions for Intersection of Two Arrays II.
        AC in 1.
        XXX: But so sloooooooooooooooow! Code smalles due to not KISS.
        M: O(N+M), T: O(N+M)
        """
        d1, d2 = defaultdict(int), defaultdict(int)
        for n in nums1:
            d1[n] += 1
        for n in nums2:
            d2[n] += 1
        res = []
        if len(d2) < len(d1):
            d1, d2 = d2, d1
        for n in d1:
            if n in d2:
                res.extend([n]*min(d1[n], d2[n]))

        return res


sl = Solution()
n1 = [4, 9, 4, 5]
n2 = [9, 4, 9, 8, 4]
print(sl.intersect(n1, n2))
