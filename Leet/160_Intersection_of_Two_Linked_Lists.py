"""
✅ GOOD linked-list (Logic)
Tag: Easy, Linked-list, Skills
Lookback:
- a+c+b == b+c+a
    * similar to 1071: s1+s2 == s2+s1: (m+n)*X == (n+m)*X
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def os_best():
            """[summary]
            Runtime: 168 ms, faster than 83.30% of Python3 online submissions for Intersection of Two Linked Lists.

            https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!
            The logic is simple, both pointer will walk through A+B+C steps. So they'll meet at intersection.
            suppose A=a+c; B = b+c;
            ==> A+B=a+c+b +c
            ==> B+A=b+c+a +c
            now, run the same length=(a+c+b), and get the intersection node
            """
            a, b = headA, headB
            if not a or not b:
                return None
            while a != b:
                a = headB if not a else a.next
                b = headA if not b else b.next
            return a

        def fxr_link_cycle():
            """[summary]
            Runtime: 255 ms, faster than 6.71% of Python3 online submissions for Intersection of Two Linked Lists.
            # traverse list1 to end, then connect tail to list2 head. Then the problem becomes finding cycle!
            # XXX: Intersected at '8', ERROR: linked structure was modified.
            """
            cur = headA
            while cur.next:
                cur = cur.next
            # cur.next = None, so cur is the tail
            cur.next = headB

            # now we can do findCycleEntry
            s, f = headA, headA
            while f and f.next:
                s = s.next
                f = f.next.next
                if s == f:
                    f = headA
                    while s != f:
                        s = s.next
                        f = f.next
                    # exit loop for s == f
                    # XXX: need to restore both link list structure
                    cur.next = None
                    return s

            # XXX: need to restore both link list structure
            cur.next = None
            return None
