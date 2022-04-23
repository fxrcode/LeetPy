"""
tag: easy
Lookback:
similar:
1419. Minimum Frogs Croaking
"""


from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def fxr():
            # Runtime: 32 ms, faster than 93.34% of Python3 online submissions for Maximum Number of Balloons.
            C = Counter(text)
            return min(C["b"], C["a"], C["l"] // 2, C["o"] // 2, C["n"])
