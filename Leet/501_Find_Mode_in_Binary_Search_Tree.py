"""
tag: easy
Lookback:
-  mode(s) (i.e., the most frequently occurred element) in sth.
- Followup: O(1) space is medium. 2-pass.
"""

from collections import Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def pochmann_o1():
            # TODO: https://leetcode.com/problems/find-mode-in-binary-search-tree/discuss/98101/Proper-O(1)-space
            pass

        def fxr():
            """
            Runtime: 136 ms, faster than 8.91% of Python3 online submissions for Find Mode in Binary Search Tree.


            """
            f = Counter()

            def ino(T: TreeNode):
                if not T:
                    return
                ino(T.left)
                f[T.val] += 1
                ino(T.right)

            ino(root)
            mxf = max(f.values())
            return [k for k, v in f.items() if v == mxf]
