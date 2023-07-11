"""
Daily Challenge (Feb 15, 2022)
Introduction to Algorithms
Recursion I
https://leetcode.com/explore/featured/card/recursion-i/250/principle-of-recursion/1681/
"""

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """[summary]
        Runtime: 44 ms, faster than 46.12% of Python3 online submissions for Swap Nodes in Pairs.

        @NeetCode: https://www.youtube.com/watch?v=o811TZLAWOo
        His algs is clear
        """
        dummy = ListNode(None, head)
        prev, cur = dummy, head

        while cur and cur.next:
            # save ptrs
            nxtPair = cur.next.next
            sec = cur.next

            # reverse this pair
            sec.next = cur
            cur.next = nxtPair
            prev.next = sec

            # update ptrs
            prev = cur
            cur = nxtPair

        return dummy.next

    def swapPairs_recurive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur_me(head: Optional[ListNode]) -> Optional[ListNode]:
            """[summary]
            my impl in 1st try, got some here-and-there bugs on pointers, conditions...
            """
            if not head or not head.next:
                return head
            # reverse head,head.next, and connect to recur(head.next.next)
            second = head.next
            sub_head = recur_me(second.next)

            second.next = head
            head.next = sub_head
            return second

        def recur(n: Optional[ListNode]) -> Optional[ListNode]:
            """[summary]
            Runtime: 31 ms, faster than 83.80% of Python3 online submissions for Swap Nodes in Pairs.

            yuzhoujr: Iterative & Recursive
            https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode
            """
            if not n or not n.next:
                return n
            hnn = n.next.next
            # XXX. WTF. you can swap nodes as numbers?!
            # All the expressions to the right of the assignment operator are evaluated before any of the assignments are made.
            n, n.next = n.next, n
            n.next.next = recur(hnn)
            return n

        return recur(head)


sl = Solution()
h = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))


def pl(h: ListNode):
    while h:
        print(h.val)
        h = h.next


pl(sl.swapPairs_recurive(h))
