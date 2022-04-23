'''
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1226/
Explore Linked List: Conclusion

Given a Circular Linked List node, which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.
'''
# Definition for a Node.


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        """
        Your runtime beats 61.71 % of python3 submissions.

        XXX: 2 pointers for singly linked list common, since no predecent pointer. So we keep prev,cur.
        XXX: the tricky part of this problem is to sort out different cases that our algorithm should deal
            with within the loop, and then design a `CONCISE` logic to handle them sound and properly.
            Here we break it down into three general cases.



        """
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node

        prev, cur = head, head.next
        to_insert = False

        while True:
            if prev.val <= cur.val:
                # case I: insert between min/max
                if prev.val <= insertVal <= cur.val:
                    to_insert = True
            elif prev.val > cur.val:
                # now we at tail (prev)
                # case II: larger than max or less than min
                if insertVal >= prev.val or insertVal <= cur.val:
                    to_insert = True

            if to_insert:
                prev.next = Node(insertVal, cur)
                return head

            prev, cur = cur, cur.next
            # loop condition
            if prev == head:
                break

            # BUG: prev, cur = cur, cur.next
            # Even bugs when copying official solution, if I put this after loop condition, then it break at beginning!
            #   cuz prev == head at beginning!
        # case III: didn't insert during the loop: so all uniform value
        prev.next = Node(insertVal, cur)
        return head

    def insert_fxr_WA(self, head: 'Node', insertVal: int) -> 'Node':
        """
        TLE for [1] <- 0
        """
        x_node = Node(insertVal)
        if not head:
            x_node.next = x_node
            return x_node
        pre, cur = None, head
        # hint: find minimum node first
        while not pre or pre.val <= cur.val:
            pre = cur
            cur = cur.next
            if cur == head:
                break

        # now min: cur, max: pre
        while True:
            # case 1: insert < min
            # case 2: insert > max
            if insertVal <= cur.val and insertVal >= pre.val:
                pre.next = x_node
                x_node.next = cur
                break

            # case 3: insert in mid
            if pre.val < insertVal < cur.val:
                pre.next = x_node
                x_node.next = cur
                break

            # print(f'continue: {pre.val}, {cur.val}')

            pre = cur
            cur = cur.next
        return head
