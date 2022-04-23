'''
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1387/
Leetcode explore Queue & Stack: Conclusion
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Follow-up: Can you implement the stack using only one queue?


'''
from collections import deque


class MyStack:
    '''
    StefanPochmann: Simple and straight forward: stack and queue is opposite order, so every push reverse!
    '''

    def __init__(self):
        self._queue = deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)


class MyStack_fxr:
    """
    Runtime: 28 ms, faster than 83.23% of Python3 online submissions for Implement Stack using Queues.

    AC in 1st try
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.len = 0
        self.topv = None
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.topv = x
        self.q.append(x)
        self.len += 1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        for _ in range(self.len-1):
            front = self.q.popleft()
            self.topv = front
            self.q.append(front)
        self.len -= 1
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.topv

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
