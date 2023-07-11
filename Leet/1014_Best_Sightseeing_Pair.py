"""
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
"""


from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        def jinjiren():
            """
            Runtime: 472 ms, faster than 77.26% of Python3 online submissions for Best Sightseeing Pair.

            REF: https://leetcode.com/problems/best-sightseeing-pair/discuss/264400/Python3-easy-to-understand-solution-in-one-pass.
            XXX: the only constraint is i < j. Restate score: (A[i]+i)+(A[j]-j)
                we can group by and so as reduce to best time to buy stock
            """
            res = 0
            best_i = 0

            for i, v in enumerate(values):
                # here v-i is actually the `A[j]-j` in formula
                res = max(res, best_i + v - i)
                # update optimal `A[i]+i`
                best_i = max(best_i, v + i)
            return res

        return jinjiren()


sl = Solution()
print(sl.maxScoreSightseeingPair([1, 2]))
print(sl.maxScoreSightseeingPair(values=[8, 1, 5, 2, 6]))
