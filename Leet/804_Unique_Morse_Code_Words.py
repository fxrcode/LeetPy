"""
tag: easy, hash
Lookback:
- no leetcode use lowercase! Simply use MORSE[ord(c)-ord('a')]!
- Be neat in easy problem
"""

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        def fxr():
            """
            Runtime: 63 ms, faster than 23.00% of Python3 online submissions for Unique Morse Code Words.

            """
            MORSE = [
                ".-",
                "-...",
                "-.-.",
                "-..",
                ".",
                "..-.",
                "--.",
                "....",
                "..",
                ".---",
                "-.-",
                ".-..",
                "--",
                "-.",
                "---",
                ".--.",
                "--.-",
                ".-.",
                "...",
                "-",
                "..-",
                "...-",
                ".--",
                "-..-",
                "-.--",
                "--..",
            ]
            res = set()
            for w in words:
                morse = "".join([MORSE[ord(c) - ord("a")] for c in w])
                res.add(morse)
            return len(res)
