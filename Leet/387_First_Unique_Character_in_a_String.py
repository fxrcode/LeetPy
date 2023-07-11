"""
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/
Leetcode Explore: Hash Table. Practical Application - HashMap
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
from collections import Counter, defaultdict
from typing import List


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Runtime: 186 ms, faster than 25.02% of Python3 online submissions for First Unique Character in a String.
        """
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

    def firstUniqChar_fxr(self, s: str) -> int:
        """
        Your runtime beats 63.21 % of python3 submissions.

        AC in 1.
        a bit smell due to the trick of -i...
        """
        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] = -i
            else:
                d[c] = i
        for v in sorted(d.values()):
            if v >= 0:
                return v
        return -1


sl = Solution()
ss = ["leetcode", "loveleetcode", "aabb"]
for s in ss:
    print(sl.firstUniqChar(s))
