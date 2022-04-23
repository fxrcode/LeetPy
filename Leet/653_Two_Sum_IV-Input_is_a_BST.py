'''
FB tag (easy)

BST iterator, yield
REF: https://stackoverflow.com/a/70617027/3984911
The yield keyword is used in enumeration/iteration where the function is expected to return more then one output.

TODO: BST iterator (iterative version) Check 173
'''

from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def hiepit_iterator():
            """
            Runtime: 159 ms, faster than 12.30% of Python3 online submissions for Two Sum IV - Input is a BST.

            T: O(N), M: O(H)
            REF: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/1420711/C%2B%2BJavaPython-3-solutions%3A-HashSet-Stack-Python-yield-Solutions-O(H)-space
            """
            def inorder_itr(r):
                if r:
                    yield from inorder_itr(r.left)
                    yield r.val
                    yield from inorder_itr(r.right)

            def rev_inorder_itr(r):
                if r:
                    yield from rev_inorder_itr(r.right)
                    yield r.val
                    yield from rev_inorder_itr(r.left)

            left_itr, right_itr = inorder_itr(root), rev_inorder_itr(root)
            vi, vj = next(left_itr), next(right_itr)
            while vi < vj:
                if vi + vj == k:
                    return True
                elif vi + vj < k:
                    vi = next(left_itr)
                else:
                    vj = next(right_itr)
            return False

        def os_inorder():
            """
            Runtime: 128 ms, faster than 25.97% of Python3 online submissions for Two Sum IV - Input is a BST.

            """
            def inorder(r):
                if r:
                    inorder(r.left)
                    ino.append(r.val)
                    inorder(r.right)

            ino = []
            inorder(root)
            i, j = 0, len(ino) - 1
            while i < j:
                if ino[i] + ino[j] == k:
                    return True
                if ino[i] + ino[j] < k:
                    i += 1
                else:
                    j -= 1
            return False

        def os_dfs():
            """
            Runtime: 118 ms, faster than 31.82% of Python3 online submissions for Two Sum IV - Input is a BST.

            XXX: if a + b = k, say you haven't meet b when you see a, then you'll see a in seen once you meet b.
            """
            def dfs(r):
                if not r:
                    return False
                if k - r.val in seen:
                    return True
                seen.add(r.val)
                return dfs(r.left) or dfs(r.right)

            seen = set()
            return dfs(root)

        def fxr_dfs():
            """
            Runtime: 127 ms, faster than 26.63% of Python3 online submissions for Two Sum IV - Input is a BST.

            edge case: [1], k=2
            """
            cnt = defaultdict(int)

            def dfs(r):
                if r:
                    cnt[r.val] += 1
                    dfs(r.left)
                    dfs(r.right)

            dfs(root)
            for v in cnt:
                if k - v in cnt:
                    if k == 2 * v:
                        if cnt[v] > 1:
                            return True
                        continue
                    return True
            return False