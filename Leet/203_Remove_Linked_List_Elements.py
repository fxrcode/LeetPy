"""
Explore: Linked List. Classic Problems
https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""

# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """[summary]
        Your runtime beats 52.89 % of python3 submissions.
        Due to Cognitive inertia, I created pre, cur as I did in Iterative reverse linked list. But here we don't need cur node.
        """
        dummy = ListNode(-val, head)
        pre = dummy

        while pre.next:
            # action
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return dummy.next
