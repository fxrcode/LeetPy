"""
✅ GOOD Divide & Conquer
tag: Hard, D&C
Lookback:
- how to customize compare func of heapq?
- think deeply about merge-sort
Daily Challenge (Feb 5, 2022)
"""

from heapq import heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def os_dc():
            """
            Runtime: 105 ms, faster than 89.25% of Python3 online submissions for Merge k Sorted Lists.
            same as merge-sort (D&C)
            ! divide & conquer
            """

            def merge(lists):
                sz = len(lists)
                if not sz:
                    return None
                if sz == 1:
                    return lists[0]

                mid = sz // 2
                l, r = map(merge, [lists[:mid], lists[mid:]])
                return merge2lists(l, r)

            def merge2lists(l1, l2):
                dummy = end = ListNode(None)
                while l1 and l2:
                    if l1.val <= l2.val:
                        end.next = l1
                        l1 = l1.next
                    else:
                        end.next = l2
                        l2 = l2.next
                    end = end.next
                end.next = l1 or l2
                return dummy.next

            return merge(lists)

        def fxr_heap():
            """
            Runtime: 114 ms, faster than 72.87% of Python3 online submissions for Merge k Sorted Lists.

            T: O(nlogk)
            """
            dummy = end = ListNode(None)
            q = []
            for n in lists:
                if n:
                    heappush(q, (n.val, id(n), n))
            while q:
                v, _, n = heappop(q)
                end.next = end = n

                if n.next:
                    nn = n.next
                    heappush(q, (nn.val, id(nn), nn))
            return dummy.next

        return fxr_heap()
