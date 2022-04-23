"""
tag: easy, skills, math
Lookback:
- please understand the problem before coding!
- bad in logic & skills
- 1st time use reduce()
"""

from collections import Counter
from functools import reduce
from math import gcd
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd_os():
            """
            Runtime: 231 ms, faster than 25.29% of Python3 online submissions for X of a Kind in a Deck of Cards.

            https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/solution/qia-pai-fen-zu-by-leetcode-solution/
            """
            freq = Counter(deck).values()
            return reduce(gcd, freq) >= 2

        """
        def fxr_WA():
            deck.sort()
            i, j = 0, 0
            Xs = []
            while i < len(deck):
                while j < len(deck) and deck[i] == deck[j]:
                    j += 1
                # if current group not >= 2
                if j - i < 2:
                    return False
                X = j - i
                Xs.append(X)
                i = j
            mnX = min(Xs)
            print(Xs)
            return all(x % mnX == 0 for x in Xs)
        """


sl = Solution()
# print(sl.hasGroupsSizeX(deck=[1]))
# print(sl.hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
# print(sl.hasGroupsSizeX(deck=[1, 2, 3, 4, 4, 3, 2, 1]))
# print(sl.hasGroupsSizeX(deck=[1, 1, 1, 2, 2, 2, 3, 3]))
print(sl.hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]))
