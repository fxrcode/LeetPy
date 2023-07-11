"""
Weekly Contest 285 (mar 19, 2022)

Lookback:
- Sucks: only 1/4
- but learned how to get path from topdown DP
- I knew Q2 === 735. Asteroid Collision, but still messy in logic...
"""
from functools import cache
from typing import List


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        res = [0] * len(aliceArrows)

        @cache
        def dp(i, left):
            if i == len(aliceArrows):
                return 0
            if left <= 0:
                return 0
            loss = dp(i + 1, left)
            win = 0
            if left > aliceArrows[i]:
                win = dp(i + 1, left - aliceArrows[i] - 1) + i
            points = max(win, loss)
            if points == win:
                res[i] = aliceArrows[i] + 1
                print(i, res[i])
            # else:
            #     res[i] = 0
            return points

        mxbob = dp(0, numArrows)
        print(res)
        return mxbob

    def countCollisions(self, directions: str) -> int:
        stk = []
        coll = 0
        for c in directions:
            if not stk:
                stk.append(c)
                continue
            while stk:
                if stk[-1] == "R":
                    if c == "S":
                        stk.pop()
                        coll += 1
                        stk.append("S")
                    if c == "L":
                        stk.pop()
                        coll += 2
                        stk.append("S")
                    if c == "R":
                        stk.append("R")
                elif stk[-1] == "L":
                    if c == "S":
                        stk.pop()
                        stk.append("S")
                    if c == "L":
                        stk.pop()
                    if c == "R":
                        stk.pop()
                        stk.append("R")
                else:
                    if c == "S":
                        pass
                    if c == "L":
                        coll += 1
                    if c == "R":
                        stk.pop()
                        stk.append("R")
        print(stk)
        return coll

    def countHillValley(self, nums: List[int]) -> int:
        up, down = False, False
        hill, valley = 0, 0
        for p, q in zip(nums, nums[1:]):
            if p - q < 0:
                up = True
                if down == True:
                    valley += 1
                    down = False
            elif p - q > 0:
                down = True
                if up == True:
                    hill += 1
                    up = False
            else:
                continue
        return hill + valley


sl = Solution()
# print(sl.countHillValley(nums=[2, 4, 1, 1, 6, 5]))
# print(sl.countHillValley(nums=[6, 6, 5, 5, 4, 1]))
# print(sl.countCollisions(directions="RLRSLL"))
print(
    sl.maximumBobPoints(numArrows=9, aliceArrows=[1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0])
)
# print(sl.maximumBobPoints(numArrows=3, aliceArrows=[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2]))
# print(sl.maximumBobPoints(numArrows=4, aliceArrows=[1, 0, 1, 2]))
