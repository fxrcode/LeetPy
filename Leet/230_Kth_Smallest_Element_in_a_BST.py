"""
Tag: Medium, BST
Lookback:
- classic usage of BST iterator

https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
* like LRU, augment hashmap with doubly-linked-list
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def os_iter():
            """
            Runtime: 68 ms, faster than 55.88% of Python3 online submissions for Kth Smallest Element in a BST.
            T: O(N), M: O(H)
            """
            stk = []
            T = root
            while True:
                while T:
                    # BUG: stk.append(T.left)
                    stk.append(T)
                    T = T.left
                topmost = stk.pop()
                k -= 1
                if not k:
                    return topmost.val
                T = topmost.right

        def pochmann():
            """
            Runtime: 36 ms, faster than 99.53% of Python3 online submissions for Kth Smallest Element in a BST.

            XXX: StephanPochmann's 173. BST Iterator template
            """
            visit = root
            stk = []
            while visit or stk:
                while visit:
                    stk.append(visit)
                    visit = visit.left
                nex = stk.pop()
                visit = nex.right
                # do something with nex
                k -= 1
                if k == 0:
                    return nex.val
