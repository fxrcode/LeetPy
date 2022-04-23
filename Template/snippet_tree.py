"""
Curated common snippet in Leetcode
Focus on post-order dfs (D&C)
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        """
        from 1597, good for debugging
        """
        if not self:
            return ""
        l, r = "", ""
        if self.left:
            l = repr(self.left)
        if self.right:
            r = repr(self.right)
        return f"{l}.{self.val}.{r}"


class Solution:
    @staticmethod
    def checkLeafNode(node: TreeNode):
        if TreeNode:
            if not (node.left or node.right):
                print("1022. Sum of Root To Leaf Binary Numbers")

    @staticmethod
    def checkEitherNode(node: TreeNode):
        if node:
            if (not node.left) ^ (not node.right):
                print("1469. Find All The Lonely Nodes")

    @staticmethod
    def build_tree(s):
        """
        s: deque(list)
        from 1612: to build tree from Leetcode input data (list)
        297. Serialize and Deserialize Binary Tree
        """

        def n(v):
            if v:
                return TreeNode(v)

        if not s:
            return None
        root = n(s.popleft())
        bfs = deque([root])
        while bfs:
            cur = bfs.popleft()
            if s:
                cur.left = n(s.popleft())
            if s:
                cur.right = n(s.popleft())
            if cur.left:
                bfs.append(cur.left)
            if cur.right:
                bfs.append(cur.right)
        return root

    """
    @staticmethod
    def build_tree(s):
        def n(i):
            if i < len(s):
                if s[i]:
                    return TreeNode(s[i])

        if not s:
            return None
        root = TreeNode(s[0])
        i = 1
        bfs = deque([root])
        while bfs:
            cur = bfs.popleft()
            cur.left = n(i)
            cur.right = n(i + 1)
            i += 2
            if cur.left:
                bfs.append(cur.left)
            if cur.right:
                bfs.append(cur.right)
        return root
    """

    def isBalancedBinaryTree():
        # 110.
        pass

    def maxHeight():
        pass

    def minHeight():
        pass

    def diameter():
        # WeRide
        pass

    def isCompleteTree():
        # 958
        pass

    def leaves():
        # 872
        pass

    def isvalidbst():
        pass

    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count_general(r: TreeNode) -> int:
            """
            general dfs to count any binary tree
            """
            if not r:
                return 0
            return 1 + count_general(r.left) + count_general(r.right)

        def count_full(r: TreeNode) -> int:
            """
            Count nodes of Full binary Tree
            """
            h = 0
            while r:
                r = r.left
                h += 1
            return 2**h - 1

        def count_complete(root: TreeNode) -> int:
            """
            https://labuladong.github.io/algo/2/18/32/
            count nodes of Complete Binary Tree
            T: O((logN)^2)
            """
            l, r = root, root
            hl, hr = 0, 0
            while l:
                l = l.left
                hl += 1
            while r:
                r = r.right
                hr += 1
            if hl == hr:
                return 2**hl - 1
            return 1 + count_complete(root.left) + count_complete(root.right)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        257. Binary Tree Paths
        """

        def dfs(node: TreeNode):
            if not node:
                return []
            res = [str(node.val) + "->" + path for path in dfs(node.left)]
            res += [str(node.val) + "->" + path for path in dfs(node.right)]
            return res or [str(node.val)]  # if empty return leaf itself

        return dfs(root)

    def lca(self, root: TreeNode, p, q) -> TreeNode:
        def dfs(node: TreeNode, p, q):
            if node in {None, p, q}:
                return node
            l, r = (dfs(kid, p, q) for kid in (node.left, node.right))
            return root if l and r else l or r

    def root2node(self, root: TreeNode, target: int):
        """
        2096. Step-By-Step Directions From a Binary Tree Node to Another
        """

        def dfs(node: TreeNode, path: list(int)):
            if node.val == target:
                return True
            if node.left and dfs(node.left, path):
                path.append("L")
            elif node.right and dfs(node.right, path):
                path.append("R")
            return len(path) > 0


li = [10, 5, 15, 1, 8, None, 7]
root = Solution.build_tree(deque(li))
print(root)
