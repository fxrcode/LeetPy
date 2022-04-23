"""
https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/
Explore Linked List Conclusion
tag: medium, dfs
Lookback
- why 2 steps if you can do in 1 step? (no need to copy node in 1st phase, then copy random in 2nd phase)
- but create d[u]=u2 once you done copy so dfs will not be infinite loop
"""
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        def os_dfs():
            """
            Runtime: 32 ms, faster than 97.30% of Python3 online submissions for Copy List with Random Pointer.

            !Crux: must update dict before clone next & random
            """
            d = {}

            def dfs(u: Node):
                if not u:
                    return None
                if u in d:
                    return d[u]
                u2 = Node(u.val, None, None)
                d[u] = u2
                u2.next = dfs(u.next)
                u2.random = dfs(u.random)
                return u2

            return dfs(head)

        def pochmann():
            """[summary]
            https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
            Use interweaving, to store mapping old->new in-place. Just like DNA replicate itself
            StefanPochmann implementation.
            Your runtime beats 5.40 % of python3 submissions.

            """
            node = head
            # 1st loop: interweaving, insert copy right after origin node
            while node:
                copy = Node(node.val)
                copy.next = node.next
                node.next = copy
                node = copy.next

            # 2nd loop, set each copy's random
            node = head
            while node:
                node.next.random = node.random.next if node.random else None
                # jump A's copy to B
                node = node.next.next

            # 3rd loop, extract copied DNA sequence out!
            node = head
            copy = head_copy = head.next if head else None
            while node:
                node.next = node = copy.next
                copy.next = copy = node.next if node else None
            return head_copy

        def fxr():
            """[summary]
            Runtime: 36 ms, faster than 70.08% of Python3 online submissions for Copy List with Random Pointer.
            AC in 1st try
            """
            tail = dummy = Node(None)
            old2new = {}
            # 1st round: deep copy new node, build singly linked list
            while head:
                # XXX: be clear on var meaning, so not confuse
                new_node = old2new[head] = Node(head.val)
                tail.next = new_node
                if head.random:
                    new_node.random = head.random

                head = head.next
                tail = tail.next

            # 2nd round: assign random with old2new map
            tail = dummy.next
            while tail:
                if tail.random:
                    tail.random = old2new[tail.random]
                tail = tail.next
            return dummy.next
