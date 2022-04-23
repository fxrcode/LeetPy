"""
tag: easy
Lookback:

"""

from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        def fxr():
            # Runtime: 32 ms, faster than 95.37% of Python3 online submissions for Check If String Is a Prefix of Array.
            j = 0
            for w in words:
                if not s[j:].startswith(w):
                    return False
                j += len(w)
                if j == len(s):
                    return True
            return False
