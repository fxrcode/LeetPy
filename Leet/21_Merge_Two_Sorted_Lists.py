"""
tag: easy, linked-list

Lookback
- snippet of linked-list
- eg. 148. Sort List
- exploit each problem by dissect it w/ different tackles and algs (bfs vs dfs, iter vs recur, simulate vs re-state, forward vs backward, math vs backtrack, etc)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def os_recur():
            """
            Runtime: 63 ms, faster than 30.18% of Python3 online submissions for Merge Two Sorted Lists.

            """

            def dfs(p, q):
                if not p:
                    return q
                elif not q:
                    return p
                elif p.val < q.val:
                    p.next = dfs(p.next, q)
                    return p
                else:
                    q.next = dfs(p, q.next)
                    return q

            return dfs(l1, l2)

        def fxr():
            """
            Runtime: 40 ms, faster than 80.87% of Python3 online submissions for Merge Two Sorted Lists.

            T: O(N)
            """
            p = dummy = ListNode(None)
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = l1
                    l1 = l1.next
                else:
                    p.next = l2
                    l2 = l2.next
                p = p.next
            p.next = l1 or l2
            return dummy.next
