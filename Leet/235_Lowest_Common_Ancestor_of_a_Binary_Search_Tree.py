"""

https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1012/
Leetcode Explore Binary Search Tree: Conclusion

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def lca_sol(cur: TreeNode) -> TreeNode:
            if cur.val > max(p.val, q.val):
                return lca_sol(cur.left)
            elif cur.val < min(p.val, q.val):
                return lca_sol(cur.right)
            # BUG: WTF!?! I've made mistake 3 times!?!
            # return root

            # XXX: THIS is the key thing I didn't come up with
            return cur

        def lca_bst(cur: TreeNode) -> TreeNode:
            """
            Your runtime beats 46.30 % of python3 submissions.

            prune using BST: cur compare with (p,q)
            """
            if not cur:
                return None
            if cur == p or cur == q:
                return cur
            if cur.val < p.val and cur.val < q.val:
                return lca_bst(cur.right)
            elif cur.val > p.val and cur.val > q.val:
                return lca_bst(cur.left)
            # regular logic
            l, r = lca_bst(cur.left), lca_bst(cur.right)
            if l and r:
                return cur
            return l if l else r

        def lca(cur: TreeNode) -> TreeNode:
            """
            Your runtime beats 6.45 % of python3 submissions.

            """
            if not cur:
                return None
            if cur == p or cur == q:
                return cur
            l = lca(cur.left)
            r = lca(cur.right)
            if l and r:
                # BUG: return root
                # careful on naming!
                return cur
            return l if l else r

        return lca_bst(root)
