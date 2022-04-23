'''
Top Interview Questions

tag: Easy,
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        def OldCodingFarmer():
            """
            Runtime: 40 ms, faster than 77.32% of Python3 online submissions for Delete Node in a Linked List.

            T: O(1)
            """
            node.val = node.next.val
            node.next = node.next.next

        def fxr():
            """
            Runtime: 71 ms, faster than 13.52% of Python3 online submissions for Delete Node in a Linked List.

            T: O(N)
            """
            pre = None
            while node.next:
                node.val = node.next.val
                pre = node
                node = node.next
            pre.next = None
