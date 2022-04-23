'''
https://leetcode.libaoj.in/count-univalue-subtrees.html
https://leetcode.com/problems/count-univalue-subtrees/
https://www.lintcode.com/problem/921/description
Leetcode Explore: Binary Tree - Solve problem recursively

XXX: Google Coding Interview - CS Dojo

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.
Example1

Input:  root = {5,1,5,5,5,#,5}
Output: 4
Explanation:
              5
             / \
            1   5
           / \   \
          5   5   5
Example2

Input:  root = {1,3,2,4,5,#,6}
Output: 3
Explanation:
              1
             / \
            3   2
           / \   \
          4   5   6
'''

# Definition of TreeNode:
from typing import Tuple
from Util import *


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """

    def countUnivalSubtrees_fxr_1013(self, root: TreeNode):
        """
        Your runtime beats 24.00 % of python3 submissions.

        bottom up. T:O(N), M:O(H)
        XXX: check the bug! if uni is false for cur.left, then isuni(cur.right)
                is shortcuted!!!, so self.cnt not update for cur.right!!!
        """
        self.cnt = 0

        def isuni(cur: TreeNode) -> bool:
            if not cur.left and not cur.right:
                self.cnt += 1
                return True

            uni = True
            if cur.left:
                uni_l = isuni(cur.left)
                uni = uni_l and cur.left.val == cur.val and uni
            if cur.right:
                # BUG: uni = uni and isuni(cur.right) and cur.right.val == cur.val
                uni_r = isuni(cur.right)
                uni = uni_r and cur.right.val == cur.val and uni

            self.cnt += uni
            return uni

        if not root:
            return 0
        isuni(root)
        return self.cnt
        '''
        def dfs_fxr_WA(cur: TreeNode) -> int:
            # XXX: One month later (Oct 13), I had the same wrong thought!
            # XXX: takeaway: needs review according to Forgetting curve!

            # recursive find uni subtree same as cur
            if not cur:
                return 0
            cnt_l = dfs_fxr_WA(cur.left)
            cnt_r = dfs_fxr_WA(cur.right)

            cnt_cur = cnt_l + cnt_r
            if not cur.left and not cur.right:
                cnt_cur += 1
            elif cur.left and cur.right:
                if cur.val == cur.left.val == cur.right.val:
                    cnt_cur += 2
            else:
                uni = cur.left or cur.right
                if uni.val == cur.val:
                    cnt_cur += 1

            return cnt_cur
        '''

    def countUnivalSubtrees_CS_Dojo(self, root: TreeNode):
        self.count = 0

        def bottom_up(root: TreeNode) -> bool:
            """
            https://leetcode.libaoj.in/count-univalue-subtrees.html
            Solution I: DFS
            """
            if not root.left and not root.right:
                self.count += 1
                return True

            is_uni = True
            if root.left:
                is_uni = bottom_up(root.left) and is_uni \
                    and root.left.val == root.val
            if root.right:
                is_uni = bottom_up(root.right) and is_uni \
                    and root.right.val == root.val
            self.count += is_uni
            return is_uni

        # bottom_up(root)
        # return self.count

        def cs_dojo(root: TreeNode) -> Tuple[int, bool]:
            """
            beat 80.86%! (submitted in Lintcode)
            CS Dojo: https://www.dailycodingproblem.com/blog/unival-trees/
            Tuple[int, bool]: [(# of non-empty unival substrees, is root a unival?)]
            """
            if not root:
                return 0, True
            left_count, is_left_unival = cs_dojo(root.left)
            right_count, is_right_unival = cs_dojo(root.right)

            is_uni = True
            # check left/right to see if contradict
            if not is_left_unival or not is_right_unival:
                is_uni = False
            if root.left and root.left.val != root.val:
                is_uni = False
            if root.right and root.right.val != root.val:
                is_uni = False
            if is_uni:
                return (left_count + right_count + 1, True)
            else:
                return (left_count + right_count, False)

        total_count, is_uni = cs_dojo(root)
        return total_count
        '''
        BUG: fxr: my init implement, passed 83% test cases
        for t2, my output = 41, but expected 38
        because the logic is wrong: I simply check left/right child, but not left/right subtree for unival check of root!
            1
          /   \
         1     1
              /  \
             4    5

        def bottom_up(root: TreeNode) -> int:
            if not root:
                return 0
            if not root.left and not root.right:
                return 1

            lc = bottom_up(root.left)
            rc = bottom_up(root.right)
            cnt = lc+rc
            if root.left and root.right:
                if root.left.val == root.right.val == root.val:
                    cnt += 1
            else:
                lr = root.left or root.right
                if lr.val == root.val:
                    cnt += 1
            return cnt
        '''


sl = Solution()

t1 = '5,1,5,5,5,#,5'
# t2 = '1,1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1'
for t in [t1]:
    root = Util.deserialize(t)
    print(sl.countUnivalSubtrees(root))
