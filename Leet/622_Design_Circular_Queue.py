"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1337/

"""


class MyCircularQueueGeeks:
    # TODO: https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/
    pass


class MyCircularQueueWithSize:
    """[summary]
    Runtime: 68 ms, faster than 77.86% of Python3 online submissions for Design Circular Queue.

    forum: hiepit [Python] Straight Forward - Clean & Concise
    https://leetcode.com/problems/design-circular-queue/discuss/1141853/Python-Straight-Forward-Clean-and-Concise
    """

    def __init__(self, k: int):
        self.cap = k
        self.q = [0 for _ in range(k)]
        self.size = 0
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.cap
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.q[self.front] = None
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # BUG: for rear, the item is at rear-1.
        # Thanks python 0-1 => -1, means the 1st item from end.
        return self.q[self.rear-1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap

        # Your MyCircularQueue object will be instantiated and called as such:
        # obj = MyCircularQueue(k)
        # param_1 = obj.enQueue(value)
        # param_2 = obj.deQueue()
        # param_3 = obj.Front()
        # param_4 = obj.Rear()
        # param_5 = obj.isEmpty()
        # param_6 = obj.isFull()


cq = MyCircularQueueWithSize(3)
print(cq.enQueue(1))
print(cq.enQueue(2))
print(cq.enQueue(3))
print(cq.enQueue(4))
print(cq.Rear())
print(cq.isFull())
print(cq.deQueue())
print(cq.Front())
