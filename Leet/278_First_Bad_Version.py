"""
https://leetcode.com/explore/learn/card/binary-search/126/template-ii/947/
Leetcode Explore: Binary Search - Template I

You are given an API bool isBadVersion(version) which returns whether version is bad.
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        Your runtime beats 99.17 % of python3 submissions.

        [Python] Powerful Ultimate Binary Search Template. Solved many problems
        https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems

        XXX: Minimize k, s.t. condition(k) is True
        """

        def isBadVersion(i) -> bool:
            pass

        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l
