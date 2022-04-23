"""
tag: Easy, set
Lookback:
- AC in 1min.
"""

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        def fxr():
            return min(len(candyType) // 2, len(set(candyType)))
