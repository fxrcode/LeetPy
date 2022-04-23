"""
tag: easy, skills, pointer, logic
Lookback:
- The important is O(1) space!
"""

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        def hiepit():
            """
            Runtime: 45 ms, faster than 54.72% of Python3 online submissions for Check If Two String Arrays are Equivalent.

            https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/discuss/1029676/Python-4-pointer-O(1)-space-Clean-and-Concise

            """
            i1 = l1 = 0
            i2 = l2 = 0
            while l1 < len(word1) or l2 < len(word2):
                if l1 == len(word1) or l2 == len(word2):
                    return False
                if word1[l1][i1] != word2[l2][i2]:
                    return False
                i1, i2 = i1 + 1, i2 + 1
                if i1 == len(word1[l1]):
                    i1, l1 = 0, l1 + 1
                if i2 == len(word2[l2]):
                    i2, l2 = 0, l2 + 1
            return True

        def fxr():
            """
            Runtime: 49 ms, faster than 43.49% of Python3 online submissions for Check If Two String Arrays are Equivalent.

            T: O(2N), M: O(2N)
            """
            return "".join(word1) == "".join(word2)
