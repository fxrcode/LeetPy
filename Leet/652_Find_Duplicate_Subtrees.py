"""
date: 02282023
✅ GOOD Tree DFS + Encoding

https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1127/
Leetcode Explore: Hash Table. Practical Application - Design the Key

Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.

XXX: kevinko1788's preorder recursion with global data vs basic calculator-like deque solution on 297. serialize and deserialize binary tree.
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/396124/Python-very-easy-to-understand-recursive-preorder-with-comments
"""
# Definition for a binary tree node.

from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def findDuplicateSubtrees_global_name_numbering(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        """
        Runtime: 60 ms, faster than 83.35% of Python3 online submissions for Find Duplicate Subtrees.

        Q: WHy so much improvement in T/M?
        XXX: laioffer explanation: https://www.youtube.com/watch?v=LYU3y0-59_k, gives 3 solution.
            3rd solution has both T/M: O(N). because postorder with no string concatenate!
            The use case is in Compiler: Global name numbering
        """
        self.ans = []

        def numbering(
            r: TreeNode, exp2num: dict, exp2freq: dict, globalnum: List[int]
        ) -> int:
            """ """
            if not r:
                return 0
            num_l = numbering(r.left, exp2num, exp2freq, globalnum)
            num_r = numbering(r.right, exp2num, exp2freq, globalnum)
            exp = (r.val, num_l, num_r)
            num_root = exp2num.get(exp, -1)
            if num_root == -1:
                num_root = globalnum[0]
                globalnum[0] += 1
                exp2num[exp] = num_root
            # !QQQ: don't know why laioffer use this dict
            #  node2num[root] = num_root
            exp2freq[exp] += 1
            if exp2freq[exp] == 2:
                self.ans.append(r)
            return num_root

        e2n, exp2freq = {}, defaultdict(int)
        globalnum = [1]
        numbering(root, e2n, exp2freq, globalnum)
        return self.ans

    def findDuplicateSubtrees_postorder_serial(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        """
        Your runtime beats 36.57 % of python3 submissions.
        XXX: The above time complexity is O(n^2). We can improve this to O(n) by replacing full serializations with serial ids instead.
            laioffer explanation: https://www.youtube.com/watch?v=LYU3y0-59_k, because join cur,left,right cost O(N), while preorder is O(N) => O(N^2) time.

        https://leetcode.com/problems/find-duplicate-subtrees/discuss/106011/Java-Concise-Postorder-Traversal-Solution
        """
        d = defaultdict(list)
        ans = []

        def postorder(root: Optional[TreeNode], d) -> str:
            """
            https://leetcode.com/problems/find-duplicate-subtrees/discuss/106011/Java-Concise-Postorder-Traversal-Solution/213062
            The way to traverse the whole tree is postorder.
            The way to construct serial is preorder.
            """
            if not root:
                return "x"
            pre_l = postorder(root.left, d)
            pre_r = postorder(root.right, d)
            # XXX: string concat's T is O(len)
            serial = ",".join([str(root.val), pre_l, pre_r])
            d[serial].append(root)
            # XXX: if len(d[pre]) > 1: # if I do this, I need to save root into set(), then convert to list as final ans!
            if len(d[serial]) == 2:
                ans.append(root)
            return serial

        postorder(root, d)
        return list(ans)

    def findDuplicateSubtrees_fxr(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        """
        Runtime: 2174 ms, faster than 5.01% of Python3 online submissions for Find Duplicate Subtrees.

        AC in 1, but so slooooooooooooooooooooooow
        """

        def bfs(root: TreeNode) -> List[int]:
            q = deque([root])
            ser = []
            while q:
                qlen = len(q)
                for _ in range(qlen):
                    cur = q.popleft()
                    # handle cur
                    if not cur:
                        ser.append("#")
                    else:
                        ser.append(str(cur.val))
                        q.append(cur.left)
                        q.append(cur.right)

                # step + 1
            return ser

        def dfs(root: TreeNode, treed):
            if not root:
                return
            b = bfs(root)
            bs = ",".join(b)
            treed[bs].append(root)

            # left/right sub recur
            dfs(root.left, treed)
            dfs(root.right, treed)

        treed = defaultdict(list)
        dfs(root, treed)
        res = []
        for v in treed.values():
            if len(v) > 1:
                res.append(v[0])
        return res


# root = TreeNode(1, left=TreeNode(2, left=TreeNode(4)),
#                 right=TreeNode(3, left=TreeNode(2, left=TreeNode(4)),
#                                right=TreeNode(4)))
# root = TreeNode(2, left=TreeNode(1), right=TreeNode(1))
root = TreeNode(
    2, left=TreeNode(20, left=TreeNode(3)), right=TreeNode(20, left=TreeNode(3))
)

sl = Solution()
print(sl.findDuplicateSubtrees_global_name_numbering(root))
