"""
tag: Medium, Skills
Lookback:
- not fluent in Linked-list design, need more practice
"""


class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)


class MyLinkedList:
    """
    Runtime: 422 ms, faster than 11.27% of Python3 online submissions for Design Linked List.

    https://leetcode.com/problems/design-linked-list/discuss/1487653/Python-Single-Linked-List-with-dummyHead-Clean-and-Concise
    """

    def __init__(self):
        self.dummy = Node(None)
        self.sz = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.sz:
            return -1
        cur = self.dummy
        for _ in range(index + 1):
            cur = cur.next
        return cur

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.sz, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.sz:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        # add new node between [prev] and [prev.next]
        new = Node(val, prev.next)
        prev.next = new
        self.sz += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.sz:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.sz -= 1


# Your MyLinkedList object will be instantiated and called as such:
ll = MyLinkedList()
ll.addAtHead(1)
ll.addAtTail(3)
ll.addAtIndex(1, 2)
print(ll.get(1))
ll.deleteAtIndex(1)
print(ll.get(1))
