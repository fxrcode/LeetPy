"""
✅ GOOD Greedy
tag: medium, Greedy
Lookback:
- Greedy os
"""

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def os_greedy():
            costs.sort(key=lambda x: x[0] - x[1])
            n = len(costs) // 2
            total = 0

            for i in range(n):
                total += costs[i][0] + costs[i + n][1]
            return total

        return os_greedy()


sl = Solution()
print(sl.twoCitySchedCost(costs=[[10, 20], [30, 200], [400, 50], [30, 20]]))
