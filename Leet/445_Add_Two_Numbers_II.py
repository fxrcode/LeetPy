"""
tag: linked-list, medium
Lookback:
- #2 & #206
"""
from math import log
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def os1_reverse():
            """
            Runtime: 82 ms, faster than 71.96% of Python3 online submissions for Add Two Numbers II.

            """

            def rev(head: ListNode):
                pre, cur = None, head
                while cur:
                    nxt = cur.next
                    cur.next = pre
                    pre = cur
                    cur = nxt
                return pre

            def pochmann_2(l1, l2):
                addends = l1, l2
                carry = 0
                dummy = end = ListNode(None)
                while addends or carry:
                    carry += sum(l.val for l in addends)
                    addends = [l.next for l in addends if l.next]
                    carry, d = divmod(carry, 10)
                    end.next = end = ListNode(d)
                return dummy.next

            return rev(pochmann_2(rev(l1), rev(l2)))

        def fxr():
            # Runtime: 86 ms, faster than 67.28% of Python3 online submissions for Add Two Numbers II.
            def l2n(l):
                n = 0
                while l:
                    n = n * 10 + l.val
                    l = l.next
                return n

            def n2l(n):
                dummy = end = ListNode(None)
                for v in str(n):
                    end.next = end = ListNode(v)
                return dummy.next

            return n2l(sum(map(l2n, [l1, l2])))
