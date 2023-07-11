"""
✅ GOOD Tree (Match)
❌ TLE/WA (WHY?!)
tag: medium, dfs
Lookback:
- Time complexity analysis is IMPORTANT
Similar:
100. Same Tree
572.Subtree-of-Another-Tree
690. Employee Importance
1612. Check If Two Expression Trees are Equivalent

"""

from functools import cache
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def wisdompeak_572():
            """
            Runtime: 101 ms, faster than 93.33% of Python3 online submissions for Linked List in Binary Tree.

            XXX: same as 572. subtree + same (pruning)
            T: O(N^2)
            """

            def is_subpath(h, r):
                if not h:
                    return True
                if not r:
                    return False
                if is_same(h, r):
                    return True
                return is_subpath(h, r.left) or is_subpath(h, r.right)

            def is_same(h, r):
                if not h:
                    return True
                if not r:
                    return False
                if h.val != r.val:
                    return False
                return is_same(h.next, r.left) or is_same(h.next, r.right)

            return is_subpath(head, root)

        return wisdompeak_572()

        def ye15_naive_dp():
            """
            Runtime: 158 ms, faster than 45.66% of Python3 online submissions for Linked List in Binary Tree.


            """

            @cache
            def dp(h, r):
                if not h:
                    return True
                if not r:
                    return False
                if h.val == r.val:
                    return (
                        dp(h.next, r.left)
                        or dp(h.next, r.right)
                        or dp(head, r.left)
                        or dp(head, r.right)
                    )
                else:
                    return dp(head, r.left) or dp(head, r.right)

            return dp(head, root)

        return ye15_naive_dp()

        """
        def fxr_WA_TLE():
            '''
            ❌ root cause: not clear dfs logic meaning!

            https://leetcode.com/problems/linked-list-in-binary-tree/discuss/525814/Python3-A-naive-dp-approach
            TLE: 37 / 67 test cases passed. (without @cache)
            WA: 61 / 67 test cases passed. (after @cache)
            https://leetcode.com/problems/linked-list-in-binary-tree/discuss/525208/Help-Can-somebody-Help-why-this-is-TLE
            head = [1,2] node = [1,3,3,2,2,2,2], it returns True ❌
            because my dfs is: "find a discontinuous subpath in a tree"
            '''

            @cache
            def dfs(h, r):
                if not h:
                    return True
                if not r:
                    return h == None
                found_l = dfs(h.next, r.left)  # BUG: dfs(2,3) = True, due to line 86
                found_r = dfs(h.next, r.right)
                if h.val == r.val and (found_l or found_r):
                    return True
                return dfs(h, r.left) or dfs(h, r.right)

            return dfs(head, root)
        """

        return fxr_WA_TLE()


sl = Solution()
head = ListNode(1, ListNode(2))
root = TreeNode(1, left=TreeNode(3, TreeNode(2)), right=TreeNode(3, TreeNode(2)))
assert sl.isSubPath(head, root) == False
