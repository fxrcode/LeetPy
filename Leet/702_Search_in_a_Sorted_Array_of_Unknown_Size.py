'''
https://leetcode.com/explore/learn/card/binary-search/136/template-analysis/1061/
Leetcode Explore: Binary Search - Template Analysis

This is an interactive problem.

You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call get(i) that:
'''

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """


class ArrayReader:
    def get(self, index: int) -> int:
        pass


class Solution:
    def search_sol(self, reader, target):
        """
        Runtime: 68 ms, faster than 12.10% of Python3 online submissions for Search in a Sorted Array of Unknown Size.

        XXX: this l,r bound init search is cleaner than mine.
        """
        if reader.get(0) == target:
            return 0

        # search boundary
        l, r = 0, 1
        while reader.get(r) < target:
            l = r
            r = r * 2

        while l < r:
            mid = (l+r)//2
            if reader.get(mid) >= target:
                r = mid
            else:
                l = mid + 1
        return -1 if reader.get(l) != target else l

    def search_fxr(self, reader, target):
        """
        Your runtime beats 9.53 % of python3 submissions.

        """
        INV = 2**31-1
        l = r = 0
        while reader.get(r) != INV and reader.get(r) < target:
            l = r
            r = 1 if r == 0 else r * 2

        while l < r:
            mid = (l+r)//2
            if reader.get(mid) >= target:
                r = mid
            else:
                l = mid + 1
        if reader.get(l) == target:
            return l
        return -1
