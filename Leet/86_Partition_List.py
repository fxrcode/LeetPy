"""
Tag: Medium, Linked-list
Lookback:
- Daily (07222022)
- Need to be careful when re-arrange node! ow, you got cycle!
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def dbabichev():
            """
            Runtime: 48 ms, faster than 64.32% of Python3 online submissions for Partition List.

            """
            d1 = ListNode(-1)
            d2 = ListNode(-1)
            p1, p2 = d1, d2
            while head:
                if head.val < x:
                    p1.next = head
                    p1 = p1.next
                else:
                    p2.next = head
                    p2 = p2.next
                head = head.next

            p1.next = d2.next
            p2.next = None
            return d1.next

        def fxr_WA():
            l = ListNode(None)
            ge = ListNode(None)
            ld, ged = l, ge
            n = head
            while n:
                if n.val < x:
                    l.next = n
                    l = l.next
                else:
                    ge.next = n
                    ge = ge.next
                n = n.next
            """
            WA: need to careful when re-arrange node! ow, you got cycle!
            FIX: ge.next = None
            """

            if l:
                l.next = ged.next
            if ld.next:
                return ld.next
            return ged.next
