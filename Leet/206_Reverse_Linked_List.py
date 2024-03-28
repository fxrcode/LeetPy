"""
Tag: Easy, linked-list
Lookback:
- iter vs recur (backward thinking)

Introduction to Algorithms
Recursion I
https://leetcode.com/explore/featured/card/recursion-i/251/scenario-i-recurrence-relation/2378/
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 65 ms, faster than 22.25% of Python3 online submissions for Reverse Linked List.

        NeetCode linked-list playlist
        """
        # dummy = ListNode(None)
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            # cur = cur.next
            cur = nxt

        return prev

    def reverseListRecur(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 68 ms, faster than 17.40% of Python3 online submissions for Reverse Linked List.

        NeetCode linked-list playlist
        """

        def traverse(head: ListNode) -> Optional[ListNode]:
            if not head or not head.next:
                return head
            p = traverse(head.next)
            head.next.next = head
            head.next = None
            return p

        return traverse(head)
