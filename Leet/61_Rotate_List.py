"""
✅ GOOD Linked-list (trick: make cycle)
tag: medium
Lookback
- review upon forgetting curve

https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
Explore Linked List Conclusion

Given the head of a linked list, rotate the list to the right by k places.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Runtime: 57 ms, faster than 44.61% of Python3 online submissions for Rotate List.
        OS + animeshsingh1993

        """
        if not head:
            return None
        if not head.next:
            return head

        # close to ring, get len
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        k %= n
        # all in base-0
        # find new tail n-k-1
        # find new head n -k
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        # break ring
        new_tail.next = None
        return new_head
