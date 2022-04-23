'''
Weekly Contest 270 (Dec 4, 2021)

Q2: Medium
'''

# Definition for singly-linked list.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head and not head.next:
            return None

        prev = ListNode(None, head)
        slow = fast = head
        # XXX: this is where I confused, when to stop? what is middle: floor(n//2)
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head
