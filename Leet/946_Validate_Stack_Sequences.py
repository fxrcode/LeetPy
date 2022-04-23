"""
tag: medium
Lookback:
- I used 2 pointers to loop, passed given tests, but WA.
- Logic! Logic! do the simulation smartly.
"""

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        def os_greedy():
            """
            Runtime: 81 ms, faster than 75.04% of Python3 online submissions for Validate Stack Sequences.

            Approach 1: Greedy
            """
            r = 0
            stk = []
            for x in pushed:
                stk.append(x)
                while stk and r < len(popped) and stk[-1] == popped[r]:
                    stk.pop()
                    r += 1
            return r == len(popped)

        return os_greedy()


sl = Solution()
print(sl.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]))
print(sl.validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]))
print(sl.validateStackSequences([2, 1, 0], [1, 2, 0]))
