"""
tag: easy, skills
Lookback:
- loop/condition, pointer, and indexing is the basic logic.
Similar:
- 828 (Hard)
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        def fxr():
            """
            Runtime: 57 ms, faster than 16.12% of Python3 online submissions for Length of Last Word.

            T: O(N), M: O(1)
            """
            end, beg = -1, -1
            for i in range(len(s) - 1, -1, -1):
                if s[i] != " " and end == -1:
                    end = i
                if end != -1 and s[i] == " ":
                    beg = i
                    return end - beg
            return end + 1
