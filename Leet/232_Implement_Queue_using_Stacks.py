'''
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1386/
Leetcode explore Queue & Stack: Conclusion

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Follow-up: Can you implement the queue such that each operation is amortized O(1)
'''


class MyQueue:
    """[summary]
    Your runtime beats 12.40 % of python3 submissions.
    AC in 1st try!

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pu = []
        self.po = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pu.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        res = self.peek()
        self.po.pop()
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.po:
            while self.pu:
                e = self.pu.pop()
                self.po.append(e)
        return self.po[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.pu and not self.po:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
