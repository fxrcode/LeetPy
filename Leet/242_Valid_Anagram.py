"""
https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def fxr():
            """
            Runtime: 44 ms, faster than 82.39% of Python3 online submissions for Valid Anagram.

            T: O(nlogn), M: O(n)
            """
            sl = list(s)
            tl = list(t)
            sl.sort()
            tl.sort()
            return sl == tl
