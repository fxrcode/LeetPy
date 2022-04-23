"""
DFS & Backtrack is the same logically.
XXX: But DFS is for explict graph, while backtrack is for implicit graph (decision tree)

TODO: classic DFS's usage: connectivity, cycle detection (3-color-variant), Hierholzer
"""
import pprint
from collections import defaultdict
from typing import List
'''
# dfs in DPV book
def dfs(G, u):
    seen.add(u)
    for v in G[u]:
        if v not in seen:
            dfs(G, v)
'''


class TreeNode:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root: TreeNode):

    def logic(root):
        # XXX: here's the specific logic in each problem
        # eg. 437. Path Sum III
        pass

    if not root:
        return
    logic(root)
    for kid in root.children:
        preorder(kid)


def CC(G: defaultdict(set)):
    """
    eg. 721. Accounts Merge

    """

    def dfs(CC, u):
        seen.add(u)
        CC.append(u)
        for v in G[u]:
            if v not in seen:
                dfs(CC, v)

    seen = set()
    CCs = []
    for n in G:
        if n in seen:
            continue
        CC = []
        dfs(CC, n)
        CCs.append(CC)
    return CCs


def validPath(G: defaultdict(set), start: int, target: int) -> bool:
    """
    eg. 1971. Find if Path Exists in Graph

    XXX: Don't use backtracking (I got TLE).
    Cuz backtrack try all the path due to un-choose, while dfs only traverse whole tree once!
    """

    def dfs(cur, seen) -> bool:
        if cur == target:
            return True

        # process current node
        seen.add(cur)

        # traverse
        for neig in G[cur]:
            if neig not in seen:
                # dfs(neig, seen)
                if dfs(neig, seen):
                    return True
        return False


def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    XXX: 1st time learning CLRS 3-color-variant DFS for cycle detection
    1059. All Paths from Source lead to Destination

    REF: OS (synonyms for official solution)
    DFS: O(V+E)
    """
    GRAY, BLACK = 1, 2
    G = defaultdict(set)
    for v, w in edges:
        G[v].add(w)
    states = [None] * n

    def lead_to_dest(cur, states):
        if states[cur]:
            # if gray, then cycle detected => False
            return states[cur] == BLACK

        if len(G[cur]) == 0:
            # if leaf node but not destination => False
            return cur == destination

        # process cur node
        states[cur] = GRAY

        for neig in G[cur]:
            if not lead_to_dest(neig, states):
                return False

        # finished process this node, mark BLACK
        states[cur] = BLACK
        return True

    return lead_to_dest(source, states)


def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    """
    802. Find Eventual Safe States

    nice 3-color variant DFS in topo-sort
    """

    W, G, B = 0, 1, 2
    colr = defaultdict(int)

    def dfs(u):
        if colr[u] != W:
            return colr[u] == B

        colr[u] = G
        for v in graph[u]:
            if colr[v] == B:
                continue
            if colr[v] == G or not dfs(v):
                return False
        colr[u] = B
        return True

    return list(filter(dfs, range(len(graph))))


def findItinerary_Hierholzer(tickets: List[List[str]]) -> List[str]:
    """[summary]
    Eulerian Path
    # 332. Reconstruct Itinerary, 2097. Valid Arrangement of Pairs
    Lookback: post-order DFS, each edge only once, rather normal DFS use visited(nodes) that each node visited once.
    """
    AL = defaultdict(list)
    for f, t in tickets:
        AL[f].append(t)
    for key in AL:
        AL[key] = sorted(AL[key], reverse=True)
    pprint.pprint(AL)

    route = []

    def dfs(u):
        while AL[u]:
            v = AL[u].pop()
            dfs(v)
        route.append(u)

    dfs('A')
    print(route)
    return route[::-1]


T = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['B', 'E'], ['E', 'B']]
print(findItinerary_Hierholzer(T))
