"""
Daily Challenge (Feb 22, 2022)
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1392/
Leetcode Explore Queue & Stack: DFS
https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3900/
Leetcode Explore Graph: DFS

date: 04082023
tag: medium, DFS
Lookback
- clear mindset rather memoize, do problem as NEW challenge everytime!
"""
from typing import List, Optional


class Node:
    # https://stackoverflow.com/questions/41135033/type-hinting-within-a-class
    # Python uses 'string' for forward references
    def __init__(self, val=0, neighbors=Optional[List["Node"]]):
        self.val = val
        #! learn how leetcode assign neighbors
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        def fxr():
            def dfs(u: Node) -> Node:
                """[summary]
                Runtime: 55 ms, faster than 49.83% of Python3 online submissions for Clone Graph.

                T: O(E)
                """

                if not u:
                    return u
                if u in mp:  # if found, then it must have cloned subgraph
                    return mp[u]
                mp[u] = Node(u.val)
                for v in u.neighbors:
                    mp[u].neighbors.append(dfs(v))
                return mp[u]

            mp = {}
            return dfs(node)

    """
    def cloneGraph_1st_WRONG(self, node: 'Node') -> 'Node':
        mp = {}  # val -> node

        # dfs to traverse and clone cur node
        def dfs(node: Node, visited: Set[int]) -> None:
            visited.add(node.val)
            cloned = Node(node.val)
            mp[node.val] = cloned

            for n in node.neighbors:
                if n.val not in visited:
                    dfs(n, visited)

        dfs(node, set())

        # 2nd dfs to build neighbors
        newRoot = mp[node.val]

        def dfs2(node, visited) -> None:
            visited.add(node.val)
            for n in node.neighbors:
                if n.val not in visited:
                    clonedNode = mp[node.val]
                    clonedNode.neighbors.append(mp[n.val])
                    dfs2(n, visited)

        dfs2(node, set())
        return newRoot
    """
