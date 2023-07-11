"""
https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/143/appendix-height-balanced-bst/1015/
Leetcode Explore Binary Search Tree: Conclusion

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.


NOTE:
* How to Traverse the Tree. DFS: Preorder, Inorder, Postorder; BFS.
* Construct BST from Inorder Traversal: Why the Solution is Not Unique
"""
# Definition for a binary tree node.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(nums, i, j) -> TreeNode:
            """
            Your runtime beats 10.71 % of python3 submissions.

            AC in 1! Because I have clear mind on algs before coding.
            How is this problem recursive? A: use left,right array to build subtree, and mid as cur root and return.
            This is post-order Traversal
            T: O(N), M: O(logn)
            """
            if i > j:
                return None
            if i == j:
                return TreeNode(nums[i])
            mid = (i + j) // 2
            l = dfs(nums, i, mid - 1)
            r = dfs(nums, mid + 1, j)
            root = TreeNode(nums[mid])
            root.left, root.right = l, r
            return root

        return dfs(nums, 0, len(nums) - 1)
