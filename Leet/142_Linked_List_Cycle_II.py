"""
https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/

Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                f = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        return None
