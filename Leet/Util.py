from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


SEP, NIL = ',', '#'


class Util:
    @staticmethod
    def deserialize(str: str) -> TreeNode:
        """
        https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
        Leetcode uses level order traversal to serialize binary tree
        """
        if not str:
            return None

        nodes = str.split(',')
        root = TreeNode(nodes[0])
        q = deque([root])

        i = 1
        while i < len(nodes):
            cur = q.popleft()
            left = nodes[i]
            i += 1

            if left != NIL:
                l = TreeNode(left)
                cur.left = l
                q.append(l)

            right = nodes[i]
            i += 1
            if right != NIL:
                r = TreeNode(right)
                cur.right = r
                q.append(r)

        return root


Util.deserialize('1,2,3,#,#,4,5')
