'''
https://leetcode.com/explore/learn/card/n-ary-tree/131/recursion/919/
Leetcode Explore N-ary Tree: Recursion
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).
'''
# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # XXX: Use object var rather global var, otherwise you need to use nonlocal in func...
        self.lv = 0

        def probe(root: Node, level: int) -> int:
            """
            Top-down is preorder and has 2 part.
            1st: in each recursion level, we visit the node first to come up with some values
            2nd: pass these values to its children recursively

            Your runtime beats 93.35 % of python3 submissions.

            probe name: https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/243896/python-bottom-up-and-top-down
            https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/290793/Python-Top-down-Approach-and-Bottom-up-Approach            """
            if not root:
                return
            # so leaf, we can get this path's depth, and WWE to update global max depth (use self.lv rather global var)
            if not root.children:
                self.lv = max(self.lv, level)
            for kid in root.children:
                probe(kid, level+1)

        # probe(root, 1)
        # return self.lv

        def bottomup(root: Node) -> int:
            """
            Bottom-up: is post-order
            It means in each recursion level, we firstly call recursion for all children nodes, then come up with the answer
            according to the return values and the value of the root node itself.

            NIL root check is base case check rather visit, since visit means to add it to pre/in/postorder result list.
            https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45550/C%2B%2B-Iterative-Recursive-and-Morris-Traversal
            """
            if not root:
                return 0
            mx_dep = 0
            if root.children:
                for kid in root.children:
                    # BUG: mx_dep = max(mx_dep, bottomup(kid)+1)
                    # So I still made mistake by confusing top-down and bottom  up: the top-down is like probe, from root (level 1) to drill-down to lower level, so need recur(kid)+1
                    mx_dep = max(mx_dep, bottomup(kid))

            # while bottom-up is post-order, means get the max-depth of kid. so the root's max-depth = max(kid tree depth) + 1!
            return mx_dep+1

        return bottomup(root)
