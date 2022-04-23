"""
Weekly Premium
tag: medium, dfs
similar: 
- 133. clone graph (undirected)
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: "Node") -> "Node":
        def fxr():
            """
            Runtime: 147 ms, faster than 20.88% of Python3 online submissions for Clone N-ary Tree.

            T: O(N)
            """
            mp = {}  # clone & prevent forever loop

            def dfs(r: Node) -> Node:
                if not r:
                    return None
                if r in mp:
                    return mp[r]
                mp[r] = Node(r.val)
                for kid in r.children:
                    mp[r].children.append(dfs(kid))
                return mp[r]

            return dfs(root)
