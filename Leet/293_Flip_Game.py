"""
Tag: Easy, String
Lookback:
- to modify str, use slicing concate
"""

from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        def fxr():
            # Runtime: 32 ms, faster than 88.65% of Python3 online submissions for Flip Game.
            res = []
            for i in range(len(currentState) - 1):
                if currentState[i : i + 2] == "++":
                    nxt = currentState[:i] + "--" + currentState[i + 2 :]
                    res.append(nxt)
            return res

        return fxr()


sl = Solution()
print(sl.generatePossibleNextMoves(currentState="++++"))
print(sl.generatePossibleNextMoves(currentState="+"))
