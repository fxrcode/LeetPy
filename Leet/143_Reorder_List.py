"""
Daily Challenge (Dec 22)

✅ GOOD DFS (Linked-List) [iterative easy, recursion elegant]
XXX: Don't do wordy translate! Do logic restate!

https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def reorderList_zcoder_93(self, head: Optional[ListNode]) -> None:
        """
        Runtime: 88 ms, faster than 88.78% of Python3 online submissions for Reorder List.

        XXX: elegant recursive https://leetcode.com/problems/reorder-list/solution/592998
        REF: https://leetcode.com/problems/reorder-list/discuss/1275393/Python-elegant-recursive-or-straightforward-iterative-approaches
        XXX: hat of 'reverse linked-list via recursion'. so post-order process
        """
        def rec(root: ListNode, cur: ListNode) -> ListNode:
            if not cur:
                return root

            # returned root will always be within the range of first half: [0,len//2], when it backtracked, it returned 0,1,2,3... mid to curr=n-1, n-2,n-3 ...mid-1 where mid=len//2
            postCurrInNewList = rec(root, cur.next)

            # XXX: post-order process
            if not postCurrInNewList:
                return None
            tmp = None
            if postCurrInNewList == cur or postCurrInNewList.next == cur:
                cur.next = None
            else:
                tmp = postCurrInNewList.next
                postCurrInNewList.next = cur
                cur.next = tmp
            return tmp
        return rec(head, head.next)

    def reorderList_os(self, head: Optional[ListNode]) -> None:
        """
        Runtime: 80 ms, faster than 98.53% of Python3 online submissions for Reorder List.

        """
        # step 1. find mid
        if not head:
            return
        s, f = head, head
        while f.next and f.next.next:
            s, f = s.next, f.next.next

        s_nxt = s.next
        s.next = None
        # step 2. reverse 2nd harf
        prev, cur = None, s_nxt
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        # step 3. merge 2 lists
        h1, h2 = head, prev
        while h1 and h2:
            h1_nxt = h1.next
            h1.next = h2
            h2, h1 = h1_nxt, h2
        return head

    def reorderList_fxr(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        BUG: 11 / 12 test cases passed.
        TLE!
        """
        def _mid(head):
            if not head:
                return None
            s, f = head, head
            while f and f.next and f.next.next:
                s, f = s.next, f.next.next
            return s

        def rec(head: ListNode, mid: ListNode) -> ListNode:
            # base:
            if head == mid:
                return head

            prev, cur = None, head

            # re-link
            while cur.next:
                prev, cur = cur, cur.next
            prev.next = None
            sub_head = head.next
            sub_head = rec(sub_head, mid)

            head.next = cur
            cur.next = sub_head
            return head

        return rec(head, _mid(head))


# head = ListNode(1, next=ListNode(2, next=ListNode(3)))
head = ListNode(1, next=ListNode(2, next=ListNode(3,
                                                  next=ListNode(4, next=ListNode(5)))))
sl = Solution()
sl.reorderList_zcoder_93(head)
