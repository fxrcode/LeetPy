"""
📌✅ GOOD DP (backward-thinking: DFS vs forward-thinking: BFS)
tag: Hard, Graph, DP, DFS, BFS, bit
Lookback
- TSP, Shortest Hamilton Cycle
- analyze state => subproblem => relate formula => backward thinking => bitmask DP
- actually, BFS is faster, and intuitive for shortest path problem
- multi-source BFS
- 1st time: state is a tuple!
- 1st time: Floyd-Warshall for shortest dist between ANY two vertex
Daily Challenge (Feb 25, 2022)
"""
from collections import deque
from functools import cache
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def os_bfs():
            """
            Runtime: 209 ms, faster than 83.88% of Python3 online submissions for Shortest Path Visiting All Nodes.

            forward thinking & faster than top-down DP
            https://leetcode-cn.com/problems/shortest-path-visiting-all-nodes/solution/gtalgorithm-tu-jie-fa-ba-hardbian-cheng-v5knb/
            """
            n = len(graph)

            # 1.初始化队列及标记数组，存入起点
            q = deque(
                (i, 1 << i, 0) for i in range(n)
            )  # 三个属性分别为 idx, mask, dist；存入起点，起始距离0，标记
            vis = {(i, 1 << i) for i in range(n)}  # 节点编号及当前状态

            # 开始搜索
            while q:
                u, mask, dist = q.popleft()  # 弹出队头元素
                if mask == (1 << n) - 1:  # 找到答案，返回结果
                    return dist
                # 扩展
                for x in graph[u]:
                    nextmask = mask | (1 << x)
                    if (x, nextmask) not in vis:
                        q.append((x, nextmask, dist + 1))
                        vis.add((x, nextmask))

            return 0

        def larry_dfs():
            """
            Runtime: 1089 ms, faster than 11.75% of Python3 online submissions for Shortest Path Visiting All Nodes.

            """
            N = len(graph)
            INF = 10**10
            dist = [[INF] * N for _ in range(N)]

            # ? WHY modeled as directed?
            for u in range(N):
                dist[u][u] = 0
                for v in graph[u]:
                    dist[u][v] = 1

            # Floyd-Warshall's ASSP
            for k in range(N):
                for i in range(N):
                    for j in range(N):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

            @cache
            def dp(node, visited):
                if visited == (1 << N) - 1:  # end_state
                    return 0
                best = INF
                for i in range(N):
                    if ((1 << i) & visited) == 0:  # unvisited i
                        best = min(best, dp(i, (1 << i) | visited) + dist[node][i])
                return best

            best = INF
            for i in range(N):
                best = min(best, dp(i, (1 << i)))
            return best

        def os_dfs():
            """
            !backward thinking & top-down DP
            Runtime: 704 ms, faster than 30.88% of Python3 online submissions for Shortest Path Visiting All Nodes.

            T: O(2^N*N^2)
            """
            N = len(graph)
            ending_mask = (1 << N) - 1
            cache = {}

            def dp(u, mask):
                state = (u, mask)
                if state in cache:
                    return cache[state]
                print(u, f"{mask:0{N}b}")
                if mask & (mask - 1) == 0:
                    # Brian Kernighan method: turn off rightmost set bit. Common snippet used in RodCut, ReverseLL (Iter/Recur), LIS, Eulerian circuit, 3-color DFS, etc
                    return 0
                cache[state] = float("inf")  # XXX: prevent DFS inf cycle
                for v in graph[u]:
                    if mask & (
                        1 << v
                    ):  # b/c we are backward direction (topo-order: cur dp derived from past dp)
                        visited = dp(v, mask)
                        not_visited = dp(v, mask ^ (1 << u))
                        cache[state] = 1 + min(cache[state], visited, not_visited)
                return cache[state]

            return min(dp(u, ending_mask) for u in range(N))

        return os_dfs()
        # return os_bfs()


sl = Solution()
graph = [[1, 2, 3], [0], [0], [0]]
print(sl.shortestPathLength(graph))
