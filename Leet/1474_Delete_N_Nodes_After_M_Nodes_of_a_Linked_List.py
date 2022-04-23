'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170
✅ GOOD Linked-List (traver + delete)
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        def os_iterative():
            dummy = ListNode(None, head)
            p = head
            i = 0
            while p:
                if i < m-1:
                    i += 1
                else:
                    j = 0
                    # XXX: traversal, and delete by relink
                    while j < n and p.next:
                        p.next = p.next.next
                        j += 1
                    i = 0
                p = p.next
            return dummy.next

        def fxr(node: ListNode):
            """
            Runtime: 72 ms, faster than 59.14% of Python3 online submissions for Delete N Nodes After M Nodes of a Linked List.

            AC in 1st
            """
            if not node:
                return None

            mtail = mnhead = node
            for _ in range(m-1):
                mtail = mtail.next
                if not mtail:
                    return node

            for _ in range(m+n):
                mnhead = mnhead.next
                if not mnhead:
                    break

            mtail.next = fxr(mnhead)
            return node

        return fxr(head)
