"""
tag: Medium, Linked-list, skills
Lookback:
- slow/fast pointer trick to get last-K node
- to swap node <=> swap nodes' val!
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def os3():
            """
            Runtime: 1625 ms, faster than 29.15% of Python3 online submissions for Swapping Nodes in a Linked List.

            https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1009800/C%2B%2BJP3-One-Pass
            """
            nonlocal k
            n1, n2, p = None, None, head
            while p is not None:
                k -= 1
                if n2:
                    n2 = n2.next
                if k == 0:
                    n1 = p
                    n2 = head
                p = p.next
            n1.val, n2.val = n2.val, n1.val
            return head

        def fxr():
            # Runtime: 1861 ms, faster than 16.27% of Python3 online submissions for Swapping Nodes in a Linked List.
            dummy = ListNode(None, head)

            def jump(j) -> ListNode:
                pre, cur = dummy, head
                for i in range(j):
                    pre, cur = cur, cur.next
                return cur

            def sz(head):
                l = 0
                while head:
                    head = head.next
                    l += 1
                return l

            kth = jump(k - 1)
            lastkth = jump(sz(head) - k)
            kth.val, lastkth.val = lastkth.val, kth.val
            return dummy.next
