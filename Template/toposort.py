"""

DFS vs BFS
4 type of basic Topo-sort question:
- a. find any topo-order
- b. is topo-order exist?
- c. find ALL topo-order (DFS)
- d. check if topo-order is unique (maximum 1 node in queue at all time)

Questions:
- 268
- 802
"""

from collections import defaultdict, deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return str(self.val)


class ClrsTopoSort:
    """
    https://github.com/stevenhalim/cpbook-code/blob/master/ch4/traversal/toposort.py
    """

    def toposort(self, V: int, AL: list[list[int]]):
        """
        Runtime: 104 ms, faster than 43.92% of Python3 online submissions for Course Schedule II.

        XXX: no need of visited set, since CLRS depends on dfn (aka color)
        """
        WHITE, GRAY, BLACK = 0, 1, 2
        cyclic = False
        dfn = defaultdict(int)
        ts = []

        def dfs(u):
            nonlocal cyclic
            if cyclic:
                return

            # !mark visiting here, rather before dfs. ow, we need to mark it in for u in range(V) as well.
            dfn[u] = GRAY
            for v in AL[u]:
                if dfn[v] == WHITE:
                    dfs(v)
                elif dfn[v] == GRAY:
                    cyclic = True
            dfn[u] = BLACK
            ts.append(u)

        for u in range(V):
            if dfn[u] == WHITE:
                dfs(u)
        if cyclic:
            return []
        return ts[::-1]


class BfsTopoSort:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        BEST topo-sort template for leetcode
        Runtime: 139 ms, faster than 57.89% of Python3 online submissions for Course Schedule II.

        T: O(E+V)
        """
        AL = defaultdict(list)
        DEG = {u: 0 for u in range(numCourses)}
        for c, p in prerequisites:
            AL[p].append(c)
            DEG[c] += 1
        m = numCourses
        q = deque([i for i in range(m) if DEG[i] == 0])
        ts = []
        while q:
            u = q.popleft()
            ts.append(u)
            if len(ts) == m:
                return ts
            for v in AL[u]:
                DEG[v] -= 1
                if DEG[v] == 0:
                    q.append(v)
        return []

    def bfs(self, start_node: Node):
        """BFS used queue + dist map
        Use case
        ---
        * topological sorting
        * if puzzle has keyword: connection components
        * level order traversal
        * shortest path in Simple Graph
        * Given transform rule, find minimum steps to transform from init to target state

        Complexity
        ---
        Time: O(E+V)
        Space: O(V)
        """
        # needs queue for BFS
        # and dist map to mark visited and SSSP
        q = deque([start_node])
        dist = {start_node: 0}

        while q:
            node = q.popleft()
            if self.is_target(node):
                return "Found target"
            for neig in node.neighbors:
                if neig in dist:
                    continue
                q.append(neig)
                dist[neig] = dist[neig] + 1

        # if we need to find shortest dist from start_nodde to ALL other nodes
        return dist

        # if we need all Connected nodes
        return dist.keys

        # if we need SSSP from start to end node
        return dist[end_node]

    def topo_sort(self, nodes: List[Node]):
        """Use BFS + in-degrees to topological sort
        it also do cycle check
        """
        # calcuate in-degrees
        indegrees = self.calc_indegrees(nodes)

        # init queue with all nodes with 0 in-degree
        # XXX: till today I found topo-sort's init is ALL 0 in-degree nodes in q.
        #       similar idea used in 542. 01 Matrix: https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
        q = deque([n for n in nodes if indegrees[n] == 0])

        # BFS to process all nodes: decrease indegrees
        topo_order = []
        while q:
            node = q.popleft()
            topo_order.append(node)
            for neig in node.neighbors:
                indegrees[neig] -= 1
                if indegrees[neig] == 0:
                    q.append(neig)

        # check if cycle, cool!
        if len(topo_order) != len(nodes):
            return False, "no topo order due to cycle!"
        return topo_order

    def calc_indegrees(self, nodes: List[Node]):
        counter = {node: 0 for node in nodes}
        for node in nodes:
            for neig in node.neighbors:
                counter[neig] += 1
        return counter

    def is_target(self, node: Node):
        """dummy endpoint check"""
        if node.val == 42:
            return True
        return False


sl = BfsTopoSort()
n0, n1, n2, n3 = Node(0), Node(1), Node(2), Node(3)
n0.neighbors = [n1]
n1.neighbors = [n2]
n2.neighbors = [n3]
n3.neighbors = [n1]

print(sl.topo_sort([n0, n1, n2, n3]))
