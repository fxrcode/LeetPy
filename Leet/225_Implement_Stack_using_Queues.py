"""
Tag: Easy, DS
Lookback:
- draw the steps, and have clear logic, before coding!
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1387/
Leetcode explore Queue & Stack: Conclusion
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Follow-up: Can you implement the stack using only one queue?
"""
from collections import deque


class MyStack:
    """
    StefanPochmann: Simple and straight forward: stack and queue is opposite order, so every push reverse!
    T: push O(N), others O(1)
    """

    def __init__(self):
        self.q = deque()

    def push(self, x):
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not len(self.q)


class MyStack_double_q:
    """
    Runtime: 41 ms, faster than 50.80% of Python3 online submissions for Implement Stack using Queues.
    T: pop O(N), others O(1)

    XXX: careful on top
    """

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.t = None

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.t = x

    def pop(self) -> int:
        for _ in range(len(self.q1) - 1):
            self.t = self.q1.popleft()
            self.q2.append(self.t)
        ret = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return ret

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return len(self.q1) == 0


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
        for _ in range(self.len - 1):
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
