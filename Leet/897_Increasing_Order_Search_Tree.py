"""
✅ GOOD DFS (multi args, w/ return)
tag: Easy, BST, DFS, FB
Lookback
- Still sucks in DFS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
- clever param pass into dfs base on left vs right
- 1st time diff param for diff dfs
[ ] REDO

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def lee215_dfs():
            """
            Runtime: 24 ms, faster than 98.44% of Python3 online submissions for Increasing Order Search Tree.

            !Local view w/ piecewise analysis!
            https://leetcode.com/problems/increasing-order-search-tree/discuss/165885/C%2B%2BJavaPython-Self-Explained-5-line-O(N)
            T: O(N), M: O(h)
            """

            def dfs(T: TreeNode, next=None) -> TreeNode:
                """
                Args:
                    T (TreeNode): current subtree's root
                    next: the inorder next of Tree's (T) transformed linked-list's tail
                        - why init None? Ans: to unify dfs logic, we can consider root as left-child of None! Therefore root's right subtree's reformed linked-list's tail's next is Next
                Returns:
                    TreeNode: linked-list head
                """
                if not T:
                    return next
                res = dfs(T.left, T)
                T.left = None
                T.right = dfs(T.right, next)
                return res

            return dfs(root)

        return lee215_dfs()

        def dbabichev():
            """
            Runtime: 61 ms, faster than 11.56% of Python3 online submissions for Increasing Order Search Tree.

            https://leetcode.com/problems/increasing-order-search-tree/discuss/958059/Python-Inorder-dfs-explained
            T: O(N), M: O(h)
            """

            def dfs(cur: TreeNode):
                l1, r2 = cur, cur
                if cur.left:
                    l1, l2 = dfs(cur.left)
                    l2.right = cur
                if cur.right:
                    r1, r2 = dfs(cur.right)
                    cur.right = r1
                cur.left = None
                return (l1, r2)

            return dfs(root)[0]

        def os():
            """
            Runtime: 36 ms, faster than 75.75% of Python3 online submissions for Increasing Order Search Tree.

            T:O(N), M: O(H)
            """
            dummy = tail = TreeNode(None)

            def ino(T: TreeNode):
                if T:
                    ino(T.left)
                    T.left = None
                    nonlocal tail
                    tail.right = T
                    tail = T
                    ino(T.right)

            ino(root)
            return dummy.right


root = TreeNode(
    6,
    left=TreeNode(3, right=TreeNode(4, right=TreeNode(5))),
    right=TreeNode(10, left=TreeNode(9, left=TreeNode(8, left=TreeNode(7)))),
)
sl = Solution()
print(sl.increasingBST(root))
