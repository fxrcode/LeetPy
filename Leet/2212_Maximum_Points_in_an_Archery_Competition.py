"""
✅ GOOD DP (retrieve path)
tag: medium, DP, dfs
Lookback:
- 1st time retrieve Solution Path in (strictly speak: after) Top-down DP (memo DFS)

[ ] TODO: hiepit updated his post: bitmask DP, etc
"""


from functools import cache
from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def hiepit():
            """
            Don't know how to get solution path from top-down DP

            """

            @cache
            def dp(i, budget):
                if i == len(aliceArrows) or budget <= 0:
                    return 0
                score = dp(i + 1, budget)
                if budget > aliceArrows[i]:  # only then Bob can win in i-th
                    score = max(score, dp(i + 1, budget - aliceArrows[i] - 1) + i)
                    # par[(i, budget)] = (i + 1, budget - aliceArrows[i] - 1)
                return score

            # print(f"Bob max score: {dp(0, numArrows)}")

            """
            return dp(1, numArrows)
            # I stopped here. no idea how to retrieve Solution path
            """
            par = {}
            ans = [0] * len(aliceArrows)
            nonlocal numArrows
            orgNumArrows = numArrows
            k = 0
            # Backtrack
            # fxr: add parent state, REF: https://stackoverflow.com/questions/29447416/printing-the-path-traversed-in-a-dynamic-programming-solution
            while k < len(aliceArrows) and numArrows > 0:
                if numArrows > aliceArrows[k] and dp(k + 1, numArrows - aliceArrows[k] - 1) + k > dp(k + 1, numArrows):  # If Bob win
                    par[(k, numArrows)] = (k + 1, numArrows - aliceArrows[k] - 1)
                    ans[k] = aliceArrows[k] + 1
                    numArrows -= aliceArrows[k] + 1
                else:
                    par[(k, numArrows)] = (k + 1, numArrows)
                k += 1

            remainArrows = orgNumArrows - sum(ans)
            for k in range(len(aliceArrows)):
                if ans[k] > 0:
                    ans[k] += remainArrows  # Distribute remain arrows to any section which Bob win -> No change in the result
                    break

            print(par)
            for i, budget in sorted(par.keys()):
                print(i, budget, par[(i, budget)])
            return ans

        return hiepit()


sl = Solution()
print(sl.maximumBobPoints(numArrows=5, aliceArrows=[1, 0, 1, 3]))
# print(sl.maximumBobPoints(numArrows=3, aliceArrows=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2]))
# print(sl.maximumBobPoints(numArrows=9, aliceArrows=[1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]))
