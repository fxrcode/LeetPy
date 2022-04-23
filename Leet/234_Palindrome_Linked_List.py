"""

Explore Linked List: Classic Problems
https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/

"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """[summary]
        StefanPochmann

        Phase 1: Reverse the first half while finding the middle.
        Phase 2: Compare the reversed first half with the second half.

        https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space/203288
        XXX: Expand rev, rev.next, slow = slow, rev, slow.next in C++ for easier understanding.
        ListNode* tmp = rev;
        rev = slow;
        slow = slow -> next;
        rev -> next = tmp;
        Args:
            head ([type]): [description]

        Returns:
            [type]: [description]
        """
        # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
        rev = None
        # initially slow and fast are the same, starting from head
        slow = fast = head
        while fast and fast.next:
            # fast traverses faster and moves to the end of the list if the length is odd
            fast = fast.next.next

            # XXX: take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next
        # compare the reversed first half with the second half
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        # if equivalent then rev become None, return True; otherwise return False
        return not rev

    def isPalindrome_fxr(self, head: ListNode) -> bool:
        """[summary]
        Runtime: 830 ms, faster than 52.47% of Python3 online submissions for Palindrome Linked List.
        Labuladong example
        """
        if not head:
            return True

        # s,f to find the middle (right lean)
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        mid = s

        right_head = self._reverse(mid)
        while head and right_head:
            if head.val != right_head.val:
                return False
            head = head.next
            right_head = right_head.next
        return True

    def _reverse(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
