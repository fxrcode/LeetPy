'''
FB tag (easy)
'''

# Definition for a binary tree node.
from typing import List, Optional
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def fxr_bfs():
            """
            Runtime: 81 ms, faster than 19.01% of Python3 online submissions for Average of Levels in Binary Tree.

            """
            dic = defaultdict(int)
            q = deque([root])
            level = 0
            ans = []
            while q:
                qlen = len(q)
                for _ in range(qlen):
                    c = q.popleft()
                    dic[level] += c.val
                    for k in (c.left, c.right):
                        if k:
                            q.append(k)
                ans.append(dic[level] / qlen)
                level += 1

            return ans

        def fxr_dfs():
            """
            Runtime: 91 ms, faster than 10.53% of Python3 online submissions for Average of Levels in Binary Tree.

            XXX: similar inorder dfs as in 1161. Maximum Level Sum of a Binary Tree
            """
            # level -> sum
            dic = defaultdict(list)

            def inorder(r: TreeNode, level):
                if r:
                    inorder(r.left, level + 1)
                    dic[level].append(r.val)
                    inorder(r.right, level + 1)

            inorder(root, 0)

            res = []
            for l in range(len(dic)):
                res.append(sum(dic[l]) / len(dic[l]))
            return res