'''

GOOD BFS vs DFS
FB tag (Medium)

'''
from typing import Optional
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def os():
            """
            Runtime: 422 ms, faster than 23.53% of Python3 online submissions for Maximum Level Sum of a Binary Tree.

            T: O(N), M: O(N)
            """
            def inorder(r, level):
                if r:
                    inorder(r.left, level + 1)
                    level_sum[level] += r.val
                    inorder(r.right, level + 1)

            level_sum = defaultdict(int)
            inorder(root, 1)

            # Choose the level with the greatest sum "level_sum[level]" and if
            # there is a tie, then select the smaller level "-level".
            return max(level_sum, key=lambda level: (level_sum[level], -level))

        def fxr():
            """
            Runtime: 496 ms, faster than 12.69% of Python3 online submissions for Maximum Level Sum of a Binary Tree.

            T: O(N)
            M: O(Max(q))
            """
            q = deque([root])
            mx = root.val
            ans = lvl = 1

            while q:
                qlen = len(q)
                res = 0
                for _ in range(qlen):
                    cur = q.popleft()
                    res += cur.val
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                # print(res, lvl)
                if res > mx:
                    mx = res
                    ans = lvl
                lvl += 1
            return ans
