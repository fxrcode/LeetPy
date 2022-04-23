'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

Jingying: Amazon OA (simpler than LRU), use doubly-list & heap & dict
'''
INF = 1e8


class MaxStack:
    """
    Runtime: 188 ms, faster than 40.28% of Python3 online submissions for Max Stack.

    T: O(N)
    M: O(N)
    """

    def __init__(self):
        self.stk = []

    def push(self, x: int) -> None:
        prev = -INF
        if self.stk:
            prev = self.peekMax()
        self.stk.append((x, max(prev, x)))

    def pop(self) -> int:
        return self.stk.pop()[0]

    def top(self) -> int:
        return self.stk[-1][0]

    def peekMax(self) -> int:
        return self.stk[-1][1]

    def popMax(self) -> int:
        mx = self.peekMax()
        tmp = []
        while self.top() < mx:
            tmp.append(self.pop())
        self.pop()
        while tmp:
            self.push(tmp.pop())
        return mx

    '''
    def popMax_WA(self) -> int:
        # BUG: My 1st attempt, this is WRONG, it should only pop the max item, not all to the max! eg. [5,1]=>[1]!
        # Interview Tip: Practice Overriding Your Brains "Assume" Mode!
        # Why I got this bug? Because I memoize 151. Min Stack, which has getMin rather popMin!
        while self.peekMax() != self.top():
            self.pop()
        return self.pop()
    '''


ms = MaxStack()
ms.push(5)
ms.push(1)
ms.popMax()
ms.peekMax()
