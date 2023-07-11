"""
✅ GOOD Tree DFS/BFS
TuSimple list
tag: medium, DFS, BFS

Lookback
+ BFS queue can store tuple (node, parent)  # similar to normal (node,level)
+ DFS with return can use to mutate tree

[ ] REDO
"""

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        def alanlzl_dfs():
            """
            Runtime: 208 ms, faster than 59.08% of Python3 online submissions for Correct a Binary Tree.

            REF: https://leetcode.com/problems/correct-a-binary-tree/discuss/940555/Python-Simply-traverse-from-right-DFS-or-BFS-O(N)-O(N)
            T: O(N)
            """
            seen = set()

            def dfs(r: TreeNode):
                if not r or (r.right and r.right in seen):
                    return None
                seen.add(r)
                r.right = dfs(r.right)
                r.left = dfs(r.left)
                return r

            return dfs(root)

        def hiepit_bfs():
            """
            Runtime: 188 ms, faster than 76.95% of Python3 online submissions for Correct a Binary Tree.

            REF: https://leetcode.com/problems/correct-a-binary-tree/discuss/1312334/Python-BFS-Level-Order-Traverse-Picture-explain-Clean-and-Concise

            XXX: enhanced BFS queue by saving tuple (node, parent)
            """
            q = deque([(root, None)])
            seen = set()
            while q:
                for _ in range(len(q)):
                    r, fa = q.popleft()
                    seen.add(r)
                    if r.right:
                        if r.right in seen:
                            if fa.left == r:
                                fa.left = None
                            else:
                                fa.right = None
                        else:
                            q.append((r.right, r))
                    if r.left:
                        q.append((r.left, r))
            return root
