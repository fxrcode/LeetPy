"""
Daily Challenge (Feb 23, 2022)
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

tag: medium, recursion
similar:
- Palindrome Linked List
- 21. Merge Two Sorted Lists

Lookback
- Classic Divide & Conquer idea: merge-sort. 
- Common trick: mid_point of linked-list.
- Why quick-sort not working in linked-list? A: no O(1) randomized pivot.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        REF: OS & https://leetcode.com/problems/sort-list/discuss/46710/Clean-python-code
        """

        def mergesort(head: Optional[ListNode]) -> Optional[ListNode]:
            def _middle(head: ListNode):
                """
                Linked-list snippet. Return len//2 node as mid
                XXX: don't forget to unlink prev.
                """
                pre, s, f = None, head, head
                while f and f.next:
                    pre, s, f = s, s.next, f.next.next
                pre.next = None
                return s

            def _merge(l1: ListNode, l2: ListNode) -> ListNode:
                """
                linked-list snippet: merge 2 sorted list.
                """
                ptr = dummy = ListNode(None)
                while l1 and l2:
                    # while both l1&l2, loop invariant: tail points to min(l1,l2)
                    if l1.val < l2.val:
                        ptr.next = l1
                        l1 = l1.next
                    else:
                        ptr.next = l2
                        l2 = l2.next
                    ptr = ptr.next
                ptr.next = l1 or l2
                return dummy.next

            if not head or not head.next:
                return head

            mid = _middle(head)
            sl1 = mergesort(head)
            sl2 = mergesort(mid)
            return _merge(sl1, sl2)

        return mergesort(head)

    def sortList_fxr(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 496 ms, faster than 48.22% of Python3 online submissions for Sort List.

        AC in 1, but took long time to debug
            * middle (which to return?)
            * sort_list base case? merge
        """

        def middle(head: ListNode) -> ListNode:
            if not head:
                return None
            s, f = head, head
            while f and f.next and f.next.next:
                s = s.next
                f = f.next.next
            # out loop
            sn = s.next
            s.next = None
            return sn

        def sort_list(head: ListNode) -> ListNode:
            if not head:
                return None

            if not head.next:
                return head

            mid = middle(head)
            h1 = sort_list(head)
            h2 = sort_list(mid)

            dummy = ListNode(-1)
            dummy2 = dummy
            while h1 and h2:
                if h1.val <= h2.val:
                    dummy.next = h1
                    h1 = h1.next
                    dummy = dummy.next
                else:
                    dummy.next = h2
                    h2 = h2.next
                    dummy = dummy.next

            # out loop: h1/h2 at least 1 is none
            dummy.next = h1 or h2
            return dummy2.next


# root = ListNode(4, ListNode(2))
root = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sl = Solution()
sl.sortList(root)
