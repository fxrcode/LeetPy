"""
✅ classic UF!
Lookback:
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3911/
Leetcode Explore Graph: Disjoint Set Union (DSU)
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.
"""


from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def chrisZhang_dfs():
            def dfs(n, g, visited):
                if visited[n]:
                    return
                visited[n] = 1
                for x in g[n]:
                    dfs(x, g, visited)

            visited = [0] * n
            g = {x: set() for x in range(n)}
            for x, y in edges:
                g[x].add(y)
                g[y].add(x)

            ret = 0
            for i in range(n):
                if not visited[i]:
                    dfs(i, g, visited)
                    ret += 1

            return ret

        def fxr_dsu():
            """
            BUG: T: O(E+VlogV), M: O(V)
            I only implemented path compression. So it's still skewed!
            Check ChrisZhang's neat implement of union by rank!

            AC in 1. Because it's same as 547. Number of Provinces
            """
            uf = {i: i for i in range(n)}

            def find(x):
                if x != uf[x]:
                    uf[x] = find(uf[x])
                return uf[x]

            for x, y in edges:
                fx, fy = find(x), find(y)
                if fx == fy:
                    continue
                uf[fy] = fx

            return sum(i == f for i, f in uf.items())

        def chrisZhang12240():
            """
            Runtime: 178 ms, faster than 19.08% of Python3 online submissions for Number of Connected Components in an Undirected Graph.

            https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/discuss/77638/Python-DFS-BFS-Union-Find-solutions

            XXX: Nice solution. One remark is that this Union-Find algorithm uses Union by rank, otherwise the time complexity is O(log(N)) for each merge.
            Only with both Union by rank and path compression, we have ~O(1) time for each union/find operation, so it gives O(V + E) time in total.
            """
            father, rank = {i: i for i in range(n)}, [0] * n

            def find(x):
                if father[x] != x:
                    father[x] = find(father[x])
                return father[x]

            def union(xy):
                fx, fy = map(find, xy)
                if rank[fx] < rank[fy]:
                    father[fx] = fy
                else:
                    father[fy] = fx
                    if rank[fx] == rank[fy]:
                        rank[fx] += 1

            # Python 3's map function is lazy, unlike Python 2's map.
            # https://stackoverflow.com/questions/19342331/python-map-calling-a-function-not-working
            # map(union, edges)
            for e in edges:
                union(e)
            return sum(i == f for i, f in father.items())

        # return fxr_dsu()
        return chrisZhang12240()


sl = Solution()
print(sl.countComponents(n=5, edges=[[0, 1], [1, 2], [3, 4]]))
