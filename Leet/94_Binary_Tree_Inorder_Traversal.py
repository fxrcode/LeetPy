"""
https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1383/
Leetcode explore Queue & Stack
https://leetcode.com/explore/learn/card/recursion-ii/503/recursion-to-iteration/2774/
Leetcode explore Recursion II: Recursion to Iteeration

Given the root of a binary tree, return the inorder traversal of its nodes' values.


"""

from typing import List, Optional, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal_Morris(self, root: Optional[TreeNode]) -> List[int]:
        """[summary]
        Geeksforgeeks: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
        And watch Tushar Roy's detailed walk through to fully understand Morris
        He also shows pre-order Morris just 1 line change
        """
        cur = root
        inorder = []
        while cur:
            if not cur.left:
                # yield cur.val
                # XXX: why add cur here?
                inorder.append(cur.val)
                cur = cur.right
            else:
                # find the inorder predecessor of cur
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                # after while, we're sure: pre is rightmost or bridge built
                if not pre.right:
                    # link inorder predecessor to cur
                    pre.right = cur
                    cur = cur.left  # after link, go traverse
                else:
                    # revert the bridge made
                    pre.right = None
                    # XXX: why add cur here?
                    # yield cur.val
                    inorder.append(cur.val)
                    cur = cur.right
        return inorder

    # def inorderTraversal_Morris_Leet_Solution(self, root: Optional[TreeNode]) -> List[int]:
    #     """[summary]
    #     TODO: BUG: THIS solution modify the tree after traversal, still debugggging.
    #     https://leetcode.com/problems/binary-tree-inorder-traversal/solution/

    #     CppCon'17, CppCon 2017: Nicholas Ormrod “Fantastic Algorithms and Where To Find Them”
    #     Nice quick overview of Morris Traversal and its usage in gcc, and learn how FB SWE think.
    #     https://www.youtube.com/watch?v=YA-nB2wjVcI&t=703s

    #     Leetcode Official Solution III: Morris Traversal (1st time seeing it)
    #     Using new data struct: Threaded Binary Tree: "A binary tree is threaded by making all
    #     right child pointers that would normally be null point to the inorder successor of
    #     the node (if it exists), and all left child pointers that would normally be null
    #     point to the inorder predecessor of the node.

    #     Step 1: Initialize current as root
    #     Step 2: While current is not NULL,
    #             If current does not have left child
    #                 a. Add current’s value
    #                 b. Go to the right, i.e., current = current.right
    #             Else
    #                 a. In current's left subtree, make current the right child of the rightmost node
    #                 b. Go to this left child, i.e., current = current.left

    #         1
    #       /   \
    #      2     3
    #     / \   /
    #    4   5 6

    #     """
    #     cur = root
    #     inorder = []
    #     while cur:
    #         if not cur.left:
    #             inorder.append(cur.val)
    #             cur = cur.right
    #         else:
    #             pre = cur.left
    #             while pre.right:
    #                 pre = pre.right
    #             # tmp is the rightmost node
    #             pre.right = cur
    #             tmp = cur
    #             cur = cur.left
    #             # don't forget to unlink 1->2 after the thread link, so as to prevent infinite loop
    #             tmp.left = None
    #     return inorder

    def inorderTraversal_DFS_Stack(self, root: Optional[TreeNode]) -> List[int]:
        """[summary]
        https://leetcode.com/problems/binary-tree-inorder-traversal/solution/
        Leetcode Official Solution II: DFS with explicit stack
        """
        res = []
        stk = []
        cur = root
        while cur or stk:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            res.append(cur.val)
            cur = cur.right
        return res

    def iterative_traversal_Visited(self, root: Optional[TreeNode]) -> List[int]:
        """
        https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31228/Simple-Python-iterative-solution-by-using-a-visited-flag-O(n)-56ms

        Universal stack iterative using visited flag, can be easily modified for pre/in/post order.
        Because normal pre/in order iterative stack is easy, but post order hard.
        This method is easy to understand and memoize.

        XXX: this is good to know, but still need classic iteraative so as to do 173. BST iterator.
        XXX: Actually this 2-color variant DFS derived from CLRS's 3-color-variant DFS!
        https://lucifer.ren/leetcode/thinkings/binary-tree-traversal.html
        """

        def inorder(root: Optional[TreeNode]) -> List[int]:
            WHITE, GRAY = 0, 1
            res, stk = [], [(root, WHITE)]
            while stk:
                cur, visited = stk.pop()
                if cur:
                    if visited:
                        res.append(cur.val)
                    else:
                        # XXX: notice the opposite order to push in stack vs recursion DFS
                        stk.append((cur.right, WHITE))
                        stk.append((cur, GRAY))
                        stk.append((cur.left, WHITE))
            return res

        def preorder(root: Optional[TreeNode]) -> List[int]:
            WHITE, GRAY = 0, 1
            res, stk = [], [(root, WHITE)]
            while stk:
                cur, visited = stk.pop()
                if cur:
                    if visited:
                        res.append(cur.val)
                    else:
                        # XXX: notice the opposite order to push in stack vs recursion DFS
                        stk.append((cur.right, WHITE))
                        stk.append((cur.left, WHITE))
                        stk.append((cur, GRAY))
            return res

        def postorder(root: Optional[TreeNode]) -> List[int]:
            WHITE, GRAY = 0, 1
            res, stk = [], [(root, WHITE)]
            while stk:
                cur, visited = stk.pop()
                if cur:
                    if visited:
                        res.append(cur.val)
                    else:
                        # XXX: notice the opposite order to push in stack vs recursion DFS
                        stk.append((cur, GRAY))
                        stk.append((cur.right, WHITE))
                        stk.append((cur.left, WHITE))
            return res

        print("in:", inorder(root))
        print("pre:", preorder(root))
        print("post:", postorder(root))

    def inorderTraversal_DFS(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: TreeNode, inorder: List[int]) -> None:
            if not root:
                return

            dfs(root.left, inorder)
            inorder.append(root.val)
            dfs(root.right, inorder)

        res = []
        dfs(root, res)
        return res


"""
So dumm init...
si, wu, liu = TreeNode(4), TreeNode(5), TreeNode(6)
er, san = TreeNode(2, si, wu), TreeNode(3, liu)
yi = TreeNode(1, er, san)
"""

# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
# smart tree init
root = TreeNode(
    1, right=TreeNode(3), left=TreeNode(2, left=TreeNode(4), right=TreeNode(5))
)

sl = Solution()
# print(sl.inorderTraversal_Morris_Leet_Solution(root))
print(sl.inorderTraversal_DFS_Stack(root))
print(sl.inorderTraversal_Morris(root))
print(sl.iterative_traversal_Visited(root))
