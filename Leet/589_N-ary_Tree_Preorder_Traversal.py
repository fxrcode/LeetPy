'''
https://leetcode.com/explore/learn/card/n-ary-tree/130/traversal/925/
N-ary Tree: Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
'''
# Definition for a Node.


from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        '''
        # Easy Recursive: Your runtime beats 65.59 % of python3 submissions.
        def dfs(root: Node, res: List[int]) -> None:
            if not root:
                return
            res.append(root.val)
            for kid in root.children:
                dfs(kid, res)

        res = []
        dfs(root, res)
        return res
        '''

        res = []
        if not root:
            return res
        stk = [root]
        while stk:
            cur = stk.pop()
            res.append(cur.val)
            for kid in reversed(cur.children):
                stk.append(kid)
        return res
