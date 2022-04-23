"""
tag: easy
Lookback:

"""

from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        def fxr():
            # Runtime: 34 ms, faster than 92.92% of Python3 online submissions for Unique Number of Occurrences.
            f = Counter(arr).values()
            return len(f) == len(set(f))
