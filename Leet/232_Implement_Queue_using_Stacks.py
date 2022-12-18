"""
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1386/
Leetcode explore Queue & Stack: Conclusion

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
Follow-up: Can you implement the queue such that each operation is amortized O(1)
"""


class MyQueue:
    """
    Runtime: 30 ms, faster than 94.00% of Python3 online submissions for Implement Queue using Stacks.

    """

    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    # Push element x to the back of queue...
    def push(self, x):
        self.in_stk.append(x)

    # Remove the element from the front of the queue and returns it...
    def pop(self):
        self.peek()
        return self.out_stk.pop()

    # Get the front element...
    def peek(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]

    # Return whether the queue is empty...
    def empty(self):
        return not self.in_stk and not self.out_stk


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
