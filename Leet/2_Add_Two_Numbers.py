"""
tag: easy, linked-list
Lookback:
- dummy = end= ListNode(None)
- chained assignment good eg. `L = L[1] = [42, None]`; `end.next = end = ListNode(1)`
- Similar: 445
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def pochmann():
            """
            Runtime: 121 ms, faster than 23.21% of Python3 online submissions for Add Two Numbers.

            https://leetcode.com/problems/add-two-numbers/discuss/1102/Python-for-the-win
            XXX: gem of neat pythonic impl
            """
            addends = l1, l2
            dummy = end = ListNode(None)
            carry = 0
            while addends or carry:
                carry += sum(a.val for a in addends)
                addends = [a.next for a in addends if a.next]
                carry, d = divmod(carry, 10)
                end.next = end = ListNode(d)
            return dummy.next
