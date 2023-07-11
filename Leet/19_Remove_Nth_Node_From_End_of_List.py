"""
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def removeNthFromEnd_StefanPochmann(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """[summary]
        The standard solution, but without a dummy extra node. Instead, I simply handle
        the special case of removing the head right after the fast cursor got
        its head start.
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """[summary]
        Your runtime beats 23.42 % of python3 submissions.
        """
        dummy = ListNode(0)
        dummy.next = head
        s, f = dummy, dummy

        while f and n:
            f = f.next
            n -= 1
        if not f:
            return None

        while f.next:
            s = s.next
            f = f.next

        # exit loop, f is the last node
        s.next = s.next.next
        return dummy.next


sl = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# print(sl.removeNthFromEnd(head, 2))

head = ListNode(1)
# print(sl.removeNthFromEnd(head, 1))

head = ListNode(1, ListNode(2))

# BUG: nah, this will not happen, as the question promise the Nth
# node to remove from the end, so the index must be valid
# print(sl.removeNthFromEnd_StefanPochmann(head, 3))
