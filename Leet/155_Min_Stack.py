'''
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1360/
Explore-Queue-Stack: Stack LIFO

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

'''
# BUG: Careful on INF, I saw Floyd&Dijkstra bili used 0x3f3f3f3f, and INF=1e9. But it fialed for max_int.
INF = float('inf')


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        Runtime: 98 ms, faster than 33.01% of Python3 online submissions for Min Stack.
        AC in 1st time, referred 'show hint#1'

        """
        self.stk = []

    def push(self, val: int) -> None:
        self.stk.append((val, min(val, self.getMin())))

    def pop(self) -> None:
        cur, cur_min = self.stk.pop()

    def top(self) -> int:
        cur, cur_min = self.stk[-1]
        return cur

    def getMin(self) -> int:
        if self.stk:
            cur, cur_min = self.stk[-1]
            return cur_min
        return INF

        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(val)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
