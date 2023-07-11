"""
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/
Leetcode Explore: Hash Table. Practical Application - HashSet

https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1034/
Leetcode Explore: Binary Search - Conclusion

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


"""


from typing import List


class Solution:
    def intersection_sort(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/intersection-of-two-arrays/discuss/82006/Four-Python-solutions-with-simple-explanation
        M: O(1), T: O(nlogn + mlogm)
        9chap: Think of algs by complexity. Given 1-line pythonic space complex: O(N+M). To optimize it, => O(1), which means 2 pointers.
        XXX: coding basics
        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if len(res) == 0 or nums1[i] != res[-1]:
                    res.append(nums1[i])
                i += 1
                j += 1
        return res

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Your runtime beats 60.18 % of python3 submissions.
        Solution 1 balances time/space well, i.e., O(n + m) time/space, but the sorting approach (solution 4) would be a good option if you want to optimize on space vs time. This is a situation where you want to have a conversation with the interviewer and ask them what is the most important (time/space) to demonstrate that you really understand the problem and realize that in some instances a worse time complexity might be "better" if space is limited.
        AC in 1 loc.
        intersection operator is O(N+M) avg, O(N*M) worst
        """
        return list(set(nums1).intersection(set(nums2)))
