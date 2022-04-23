'''
Daily Challenge (Dec 15)

Thoughts from a Google interviewer
https://leetcode.com/problems/insertion-sort-list/discuss/46429/Thoughts-from-a-Google-interviewer

TODO: iterative
'''

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def fxr(node: ListNode):
            """
            Runtime: 1227 ms, faster than 61.95% of Python3 online submissions for Insertion Sort List.
            not AC until I looked post: Runtime: 1227 ms, faster than 61.95% of Python3 online submissions for Insertion Sort List.
            XXX: Recursion might handle edge cases automatically, so you may still need if/else logic!
            """
            if not node or not node.next:
                return node

            sec = r = fxr(node.next)

            # XXX: this is my missing part, was hesitate to write, since I thought recursion should always handle edge case,
            #       but here seems I have to handle it here.
            if node.val <= r.val:
                node.next = sec
                return node

            node.next = None
            pre = ListNode(None)
            while r:
                if r.val <= node.val:
                    pre = r
                    r = r.next
                else:
                    break
            pre.next = node
            node.next = r
            return sec


head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sl = Solution()
sl.insertionSortList(head)
