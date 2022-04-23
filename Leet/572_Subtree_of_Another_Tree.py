"""
✅ GOOD Tree DFS (2 layer), KISS
✅ GOOD Tree Encoding (Merkle hashing)
tag: medium, dfs
Lookback:
- Wisdompeak: sol1 dfs; sol2 KMP (6th eg in KMP series)
Similar:
- 1367, careful on TLE & WA!
- 437. Path Sum III
🌸 Huahua Tree List

https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions
"""
from hashlib import sha256
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def hiepit():
            """
            Runtime: 158 ms, faster than 57.91% of Python3 online submissions for Subtree of Another Tree.

            Common snippet: KISS
            """

            def is_same(r, s):
                if r and s:
                    return r.val == s.val and is_same(r.left, s.left) and is_same(r.right, s.right)
                return r == s

            def dfs(r, s):
                if not r:
                    return False
                if is_same(r, s):
                    return True
                return dfs(r.left, s) or dfs(r.right, s)

            return dfs(root, subRoot)

        return hiepit()

        def awice_merkle(r, sub):
            """
            Runtime: 92 ms, faster than 92.83% of Python3 online submissions for Subtree of Another Tree.

            """

            def hash_(x):
                S = sha256()
                # S.update(bytes(x, encoding='utf-8'))
                # S.update(x)
                S.update(x.encode("utf-8"))
                return S.hexdigest()

            def merkle(node):
                if not node:
                    return "#"
                # post-order DFS
                m_left = merkle(node.left)
                m_right = merkle(node.right)
                node.merkle = hash_(m_left + str(node.val) + m_right)
                return node.merkle

            merkle(r)
            merkle(sub)

            def dfs(node):
                if not node:
                    return False
                return node.merkle == sub.merkle or dfs(node.left) or dfs(node.right)

            return dfs(r)

        def awice_dfs(r, sub):
            """
            Runtime: 164 ms, faster than 41.60% of Python3 online submissions for Subtree of Another Tree.

            root=[1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]
            subRoot=[1,null,1,null,1,null,1,null,1,null,1,2]
            """

            def is_match(s, t):
                if not s and not t:
                    return True
                if not s or not t:
                    return False
                if s.val == t.val:
                    return is_match(s.left, t.left) and is_match(s.right, t.right)

            if is_match(r, sub):
                return True
            if not r:
                return False
            # BUG: So I still don't understand 2-layer DFS
            # return is_match(root.left, subRoot) or is_match(root.right, subRoot)
            return awice_dfs(r.left, sub) or awice_dfs(r.right, sub)

        # return awice_dfs(root, subRoot)
        return awice_merkle(root, subRoot)

        """
        WRONG again for simple Tree DFS
        root: [3,4,5,1,null,2]
        subRoot: [3,1,2]
        def predfs(root: TreeNode, subRoot: TreeNode) -> bool:
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False

            ans = False
            if root.val == subRoot.val:
                ans |= predfs(root.left, subRoot.left) and \
                    predfs(root.right, subRoot.right)
            ans |= predfs(root.left, subRoot) or predfs(root.right, subRoot)
            return ans
        return predfs(root, subRoot)
        """


# root = TreeNode(3, left=TreeNode(4, left=TreeNode(1), right=TreeNode(2)), right=TreeNode(5))
# subRoot = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
root = TreeNode(3, left=TreeNode(4, left=TreeNode(1)), right=TreeNode(5, left=TreeNode(2)))
subRoot = TreeNode(3, left=TreeNode(1), right=TreeNode(2))
sl = Solution()
print(sl.isSubtree(root, subRoot))
