"""
Explore Linked List: Classic Problems
https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1208/

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.


"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """[summary]
        Leetcode Official solution
        Runtime: 58 ms, faster than 13.92% of Python3 online submissions for Odd Even Linked List.

        """
        if not head:
            return None
        # oddList's head/tail: head, odd
        # evenList's head/tail: evenHead, even
        odd = head
        evenHead = even = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # now even or even.next is None
        # corresponds to 1-2-3, and 1-2-3-4
        odd.next = evenHead
        return head

    def oddEvenList_fxr(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """[summary]
        Your runtime beats 30.56 % of python3 submissions.
        My impl is over complicated. Coded 30 min...
        """
        if not head:
            return None
        if not head.next:
            return head

        odd, eve = ListNode(-1), ListNode(-2)
        odd.next = head
        eve.next = head.next

        o, e = odd.next, eve.next
        # XXX: counter = 1, since we just jump between even vs odd, can make it bool.
        # Same as in Bi-direction BFS.
        isOdd = True

        o_tail = None
        while o and e:
            # if counter % 2:
            if isOdd:
                o.next = e.next
                # keep o_pre so that when o is None, we still have record of odd' tail
                o_tail = o
                o = o.next
            else:
                e.next = o.next
                e = e.next
            # counter += 1
            isOdd = not isOdd

        if o:
            o.next = eve.next
        if e:
            o_tail.next = eve.next

        return odd.next
