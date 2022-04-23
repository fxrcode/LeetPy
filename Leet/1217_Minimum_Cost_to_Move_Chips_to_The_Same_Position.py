'''

Daily Challenge (Dec 7)
Similar to Jingying's mock (Dec 7, 2021)
XXX: when you try to find pattern of problem, try position 0, last, avg, or the given positions!!!
    Don't stuck at one guess
'''

from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        def os_smart():
            """
            Runtime: 32 ms, faster than 72.09% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.

            Lessons Learnt->
            Coding is more about the approach you think in first 10 minutes.
            It more about thinking about the problem rather than following the fixed style of coding
            The problem is really good to test somebody's logic.
            """
            odd, even = 0, 0
            for p in position:
                if p % 2 == 0:
                    even += 1
                else:
                    odd += 1
            return min(even, odd)

        def fxr_brute():
            """
            Runtime: 56 ms, faster than 9.30% of Python3 online submissions for Minimum Cost to Move Chips to The Same Position.

            """
            ans = float('inf')
            for t in position:
                cost = 0
                for s in position:
                    if abs(s-t) % 2 == 0:
                        cost += 0
                    else:
                        cost += 1
                ans = min(ans, cost)
                # print(t, ans)
            return ans
