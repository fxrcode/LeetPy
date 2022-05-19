"""
✅ GOOD Tree/Graph
tag: Medium, DFS
Lookback
- reminds me TSP: 847, but not!
- Insight: if general Tree has V nodes => V-1 edges => best cost to visit all in cycle: 2*(V-1)
Similar: 
- 1361, 261, 694
"""

from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def post_dfs():
            """
            Runtime: 829 ms, faster than 61.28% of Python3 online submissions for Minimum Time to Collect All Apples in a Tree.

            https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solution/di-188-chang-zhou-sai-ti-jie-by-suibianfahui-3/

            XXX: why no seen set if edges is tree? No cycle to worry. But here must use bi-directional AL, ow, WA for case below.
                But also make tree->graph, must use seen.
                Does @cache help? Ans: NO! infinite loop still exist if not using seen set.
            """
            AL = defaultdict(list)
            for u, v in edges:
                AL[u].append(v)
                AL[v].append(u)

            def dfs(u):
                seen.add(u)
                appleInMe = hasApple[u]
                for v in AL[u]:
                    if v not in seen:
                        appleInMe |= dfs(v)
                if not appleInMe:
                    AL.pop(u)
                return appleInMe

            seen = set()
            dfs(0)
            return max(0, 2 * (len(AL) - 1))

        return post_dfs()

        def zhuifengshaonian_dfs():
            """
            Runtime: 897 ms, faster than 51.47% of Python3 online submissions for Minimum Time to Collect All Apples in a Tree.

            https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solution/python3-zi-di-xiang-shang-dfs-by-yim-6-aub7/
            """
            AL = defaultdict(list)
            for x, y in edges:
                AL[x].append(y)
                AL[y].append(x)

            def dfs(u) -> bool:
                seen.add(u)
                res = hasApple[u]
                for v in AL[u]:
                    if v not in seen:
                        res |= dfs(v)
                if res:
                    VALID.add(u)
                return res

            VALID = set()
            seen = set()
            dfs(0)
            return max(0, 2 * (len(VALID) - 1))

        # return zhuifengshaonian_dfs()


sl = Solution()
# n = 7
# edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
# hasApple = [False, False, True, False, True, True, False]
# n = 7
# edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
# hasApple = [False, False, True, False, False, True, False]
# n = 7
# edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
# hasApple = [False, False, False, False, False, False, False]
n = 4
edges = [[0, 2], [0, 3], [1, 2]]
hasApple = [False, True, False, False]
print(sl.minTime(n, edges, hasApple))
