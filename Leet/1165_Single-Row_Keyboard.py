'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        def fxr_brute():
            """
            Runtime: 44 ms, faster than 87.10% of Python3 online submissions for Single-Row Keyboard.

            """
            c2i = {c: i for i, c in enumerate(keyboard)}
            idx = 0
            time = 0
            for w in word:
                time += abs(idx - c2i[w])
                idx = c2i[w]
            return time
