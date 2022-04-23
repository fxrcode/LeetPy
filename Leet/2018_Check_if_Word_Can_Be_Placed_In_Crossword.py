"""
❌📌 REDO Str
Tag: Medium, Skills, Str
Lookback:
- I missed important condition: There must not be any empty cells ' ' or other lowercase letters directly at 
    left/right if match horizontal or above/below if match vertical
"""

from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def silvia42():
            """
            Runtime: 1517 ms, faster than 83.45% of Python3 online submissions for Check if Word Can Be Placed In Crossword.

            https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/discuss/1486285/Python-3-working-with-strings
            """
            words = [word, word[::-1]]
            n = len(word)
            for B in board, zip(*board):
                for row in B:
                    q = "".join(row).split("#")
                    for w in words:
                        for s in q:
                            if len(s) == n and all(ss in (" ", ww) for ss, ww in zip(s, w)):
                                return True
            return False

        return silvia42()
