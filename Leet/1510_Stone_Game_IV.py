"""
✅ GOOD DFS (game)
✅ GOOD Zermelo's theorem
Daily Challenge (Jan 21)
Tag: Hard, Game theory, DFS
"""
from functools import cache
from math import isqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        def fxr():
            """
            Runtime: 3516 ms, faster than 22.60% of Python3 online submissions for Stone Game IV.

            T: O(N* sqrt(N))
            """

            @cache
            def dfs(remain):
                """
                dfs(remain): represents whether the current player must win with `remain` stones remaining.
                """
                if remain == 0:
                    return False
                # if remain == isqrt(remain)**2:
                #     return True
                for i in range(1, isqrt(remain) + 1):
                    # !if there is any chance to make the opponent lose the game in the next round,
                    #  !then the current player will win.
                    if not dfs(remain - i**2):
                        return True
                return False

            return dfs(n)

        return fxr()


sl = Solution()
for n in [13]:  # [1, 2, 4, 13, 23, 24]:
    print(sl.winnerSquareGame(n))
