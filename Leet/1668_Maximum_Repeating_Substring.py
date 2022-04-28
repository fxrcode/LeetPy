"""
Tag: Easy
Lookback:
- start from brute-force: MVP
- then find algs to speed up
"""


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        def fxr():
            """
            Runtime: 20 ms, faster than 99.41% of Python3 online submissions for Maximum Repeating Substring.

            T: O(N^2)
            """
            if len(sequence) < len(word):
                return 0
            k = 1
            while word * k in sequence:
                k += 1
            return k - 1

        return fxr()
