"""
✅ GOOD DFS (Pre-order)
Tag: Medium, DFS, Tree
Lookback
- How to analyze: which DFS to use: pre vs in vs post? Ans: local view.

https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/994/
Leetcode explore Binary Tree: Conclusion
https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3895/
Leetcode Explore Graph: BFS
"""

# Definition for a Node.

from collections import deque


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def connect_bfs(self, root: "Node") -> "Node":
        """
        Runtime: 73 ms, faster than 39.73% of Python3 online submissions for Populating Next Right Pointers in Each Node.

        T: O(E+V)
        """

        def bfs():
            q = deque([root])
            visited = set([root])

            while q:
                qlen = len(q)
                pre = None
                for _ in range(qlen):
                    cur = q.popleft()
                    # same level
                    # do the next link
                    if pre:
                        pre.next = cur
                        # print(pre, cur)
                    pre = cur

                    for kid in [cur.left, cur.right]:
                        if kid and kid not in visited:
                            q.append(kid)
                            visited.add(kid)

        if not root:
            return root
        bfs()
        return root

    def connect(self, root: "Node") -> "Node":
        """
        Runtime: 60 ms, faster than 85.01% of Python3 online submissions for Populating Next Right Pointers in Each Node.

        XXX: Huahua's analysis is so GOOOD. For tree, 90% recursion. Two crux for Tree recursion analysis:
        1. analyze to pick the right order: pre/in/post recursion?
        2. local view analysis

        Notes:
        * just need to draw 3 level of tree to analyze.
        * We check subtree a for local view. easily we can connect b->c. But how to connect c->e? we need to get d from a.
        * since we analyzed b->c is connected via rec(a), so a->d is done by rec(p). 
        * Therefore We need to do rec(p) before rec(a), so it's preorder rather inorder.
                p
              /   \
            /      \
           a   ->   d
         /  \      / \
        b -> c -> e   f
        """
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
        """
        BUG: My first try, no clear thought...
        def td(n1: Node, n2: Node) -> None:
            if n1:
                n1.next = n2
                if n1.right:
                    n1.right.right = n2.left
            td(n1.left, n1.right)
            td(n2.left, n2.right)
        td(root.left, root.right)
        return root
        """


root = Node(1, left=Node(2), right=Node(3))

sl = Solution()
sl.connect_bfs(root)
