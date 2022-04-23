"""
Daily Challenge (Mar 9, 2022)
tag: medium, linked-list
Lookback:
- linked-list is good to practice skills
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def iwanttopass():
            """
            Runtime: 82 ms, faster than 12.52% of Python3 online submissions for Remove Duplicates from Sorted List II.

            https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/discuss/28398/clean-python-solution-involving-dummy-node
            """
            dummy = ListNode(None, head)
            pre, cur = dummy, head
            while cur:
                if cur.next and cur.val == cur.next.val:
                    val_to_rm = cur.val
                    while cur and cur.val == val_to_rm:
                        cur = cur.next
                    # not cur or cur is start non-dup sublist
                    pre.next = cur
                else:
                    pre, cur = cur, cur.next
            return dummy.next


sl = Solution()
head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))
print(sl.deleteDuplicates(head))
