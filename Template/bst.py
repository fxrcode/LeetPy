'''
BST & Iterator are related. Same as recursion is related to Tree/Graph
https://leetcode.com/problems/binary-search-tree-iterator/discuss/52647/Nice-Comparison-(and-short-Solution)
Example:
* 173. Binary Search Tree Iterator
* 230. Kth Smallest Element in a BST

'''


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    visit = root
    stk = []
    while visit and stk:
        while visit:
            stk.append(visit)
            visit = visit.left
        next = stk.pop()
        visit = next.right
        # do something with next
        k -= 1
        if k == 0:
            return next.val


def inorder_traver(root: TreeNode):
    visit = root
    stk = []
    while visit or stk:
        while visit:
            stk.append(visit)
            visit = visit.left
        next = stk.pop()
        visit = next.right
        print(next.val)
