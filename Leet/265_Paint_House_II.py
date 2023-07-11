"""
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming

Follow up: Could you solve it in O(nk) runtime?
Metacognition: When you analyze a concrete example, the goal is to find pattern/property of this problem,
    but how to make sure this concrete case is generalize enough to show the exact pattern/property?
    eg. Greedy is mostly wrong since the cases you came up is not generalized, so your greedy algs got WA.
"""


from functools import cache
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        def os_onk():
            # TODO: similar to top-3 in stream, notice init min_color = second_min_color = None
            pass

        def os_onk_Kakinohana():
            """
            Runtime: 155 ms, faster than 49.47% of Python3 online submissions for Paint House II.
            https://leetcode.com/problems/paint-house-ii/solution/1033891

            T: O(nk), M: O(k)
            """
            n, k = len(costs), len(costs[0])
            prev_row = costs[0]
            for i in range(1, n):
                cur_row = costs[i]
                min_cost = min(prev_row)
                min_color = prev_row.index(min_cost)
                second_min_cost = min(prev_row[:min_color] + prev_row[min_color + 1 :])
                print(min_cost, min_color, second_min_cost)
                for c in range(k):
                    cur_row[c] += min_cost if c != min_color else second_min_cost
                print(cur_row)
                prev_row = cur_row
            return min(prev_row)

        def fxr_recur():
            """
            Runtime: 254 ms, faster than 14.56% of Python3 online submissions for Paint House II.

            T: O(nk^2), M: O(k)
            """
            k = len(costs[0])

            @cache
            def paint(i, c):
                if i >= len(costs):
                    return 0
                notc = list(range(k))
                notc.remove(c)
                remain = min([paint(i + 1, nc) for nc in notc])
                return remain + costs[i][c]

            return min([paint(0, c) for c in range(k)])

        return os_onk()


sl = Solution()
print(sl.minCostII(costs=[[1, 5, 3], [2, 9, 4]]))
