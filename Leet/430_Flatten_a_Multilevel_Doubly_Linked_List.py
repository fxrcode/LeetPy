"""
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1225/
Explore Linked List Conclusion

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

XXX: Good problem to learn implicit/explict recursion/stack
"""
# Definition for a Node.


from typing import Tuple


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten_stack(self, head: Node) -> Node:
        """[summary]
        https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/154908/Python-easy-solution-using-stack
        XXX: more understand of Stack and Recursion. First learned Queue vs Stack on 9chap BFS.
        Your runtime beats 11.56 % of python3 submissions.

        """
        if not head:
            return
        stk = [head]
        prev = Node(-1)
        while stk:
            root = stk.pop()
            prev.next = root
            root.prev = prev
            prev = root
            if root.next:
                stk.append(root.next)
            if root.child:
                stk.append(root.child)
                root.child = None
        head.prev = None
        return head

    def flatten_recur(self, head: "Node") -> "Node":
        """
        https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/295912/C%2B%2B-Simple-5-line-recursive-solution-(with-diagram)
        Your runtime beats 5.45 % of python3 submissions.
        XXX: learned trick that I don't know before: add new arg: rest
        """

        def recur(head: Node, rest: Node) -> Node:
            if not head:
                return rest
            head.next = self.recur(head.child, self.recur(head.next, rest))
            if head.next:
                head.next.prev = head
            head.child = None
            return head

        return recur(head, None)

        """
        def recur(self, head: Node) -> Node:
            # base
            if not head:
                return None
            if not head.next:
                return head
            # subproblems
            child_tail = self.recur(head.child)
            nxt_tail = self.recur(head.next)

            nxt = head.next
            head.next = head.child
            child_tail.next = nxt
            return nxt_tail
            """
