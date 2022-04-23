"""
✅ GOOD Graph DFS vs Backtrack
✅ GOOD Graph BFS

tag: medium, dfs, backtrack, bfs, graph
Lookback:
- basic skills of graph traversal

https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3849/
Leetcode Explore Graph: DFS
https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3853/
Leetcode Explore Graph: BFS

Daily Challenge (Nov 28)

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
"""


from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def bt(cur, path, res):
            """
            Runtime: 104 ms, faster than 87.71% of Python3 online submissions for All Paths From Source to Target.

            lee215. T: O(2^N)
            """
            if cur == len(graph) - 1:
                res.append(path[:])
                return
            for neig in graph[cur]:
                bt(neig, path + [neig], res)

        res = []
        # so you use backtrack, then you start from init node, so you should init its state: node 0, path: [0]
        bt(0, [0], res)
        return res

        def bfs():
            """
            Runtime: 104 ms, faster than 53.84% of Python3 online submissions for All Paths From Source to Target.

            REF: https://leetcode.com/problems/all-paths-from-source-to-target/discuss/1008179/Python-DFS-and-BFS
            augment BFS can do all paths, so you should consider it as general search.
            """
            q = deque([(0, [0])])
            res = []

            while q:
                cur, path = q.popleft()
                if cur == len(graph) - 1:
                    res.append(path[:])
                for neig in graph[cur]:
                    q.append([neig, path + [neig]])
            return res

        def bt_fxr(cur, visited, path, res):
            """
            Your runtime beats 33.53 % of python3 submissions.

            XXX: my 1st backtrack impl .
            Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1.
            So no need of visited.
            """
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for neig in graph[cur]:
                    if neig not in visited:
                        visited.add(neig)
                        bt_fxr(neig, visited, path + [neig], res)
                        visited.remove(neig)

        """
        WA: regular dfs only traverse whole graph once, so O(V+E), same as BFS
        def dfs(cur, visited, path, res):
            print(cur, visited, path, res)
            if cur == len(graph)-1:
                res.append(path+[cur])
                return
            visited.add(cur)
            for neig in graph[cur]:
                if neig not in visited:
                    dfs(neig, visited, path + [cur], res)
        """


sl = Solution()
print(sl.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
# print(sl.allPathsSourceTarget(graph=[[1], [3, 2, 4], [3], [4], []]))
# print(sl.allPathsSourceTarget(graph=[[1, 2], [2], []]))
