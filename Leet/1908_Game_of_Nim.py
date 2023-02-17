"""

✅ GOOD Game DFS
tag: Medium, Brainteaser, DFS, Game
Lookback:
+ game theory DFS (decision tree), me must win === any(other loss)
"""

from functools import cache
from typing import List


class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        def ye15():
            # bitmask DP
            # XXX: I'd prefer hmz74's sorted tuple, so there's more chance of memo
            pass

        def hmz74():
            """
            Runtime: 198 ms, faster than 75.00% of Python3 online submissions for Game of Nim.

            memo DFS, with sorted tuple
            https://leetcode.com/problems/game-of-nim/discuss/1318191/Python-3%3A-memoization-with-sorted-tuple
            https://leetcode.com/problems/game-of-nim/discuss/1310391/Python3-memoization-short-code-with-comment(encode-to-string)
            """

            @cache
            def dfs(piles):
                # state has no relation to order: [1,2,3]  = [2, 3,1] = ...
                if sum(piles) == 0:
                    # Lose if no pile to remove
                    return False

                lpiles = list(piles)
                for i in range(len(lpiles)):
                    for x in range(1, lpiles[i] + 1):
                        lpiles[i] -= x
                        # XXX: For each pile try to remove any number, if any can cause the opponent lose, then win.
                        if not dfs(tuple(sorted(lpiles))):
                            return True
                        ## backtracking
                        lpiles[i] += x
                return False

            # make [1,2,3] to '123'
            return dfs(tuple(sorted(piles)))

        def sprague_grundy():
            """
            Runtime: 28 ms, faster than 97.73% of Python3 online submissions for Game of Nim.

            Game theory (2 state FSM)
            """
            xor = piles[0]
            for i in range(1, len(piles)):
                xor ^= piles[i]
            if xor == 0:
                return False
            return True
