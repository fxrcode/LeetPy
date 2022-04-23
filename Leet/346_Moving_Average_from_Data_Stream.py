"""
tag: easy, circular-buffer
Lookback
- Review! Review! Review!
- I still stuck in my last thought, didn't learn from OS

[ ] REDO
https://leetcode.com/explore/learn/card/queue-stack/228/first-in-first-out-data-structure/1368/
Leetcode explore Queue & Stack
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
"""
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.win = deque()
        self.win_sum = 0
        self.sz = size
        self.cnt = 0
        # circular queue and head
        self.circ = [0] * size
        self.head = 0

    def next_sol_circular(self, val: int) -> float:
        """
        Official solution gives circular queue template. Just use self.head to get tail
        XXX: essence: single formula: tail = (head+1)%size
        """
        self.cnt += 1
        tail = (self.head + 1) % self.sz
        self.win_sum = self.win_sum - self.circ[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.sz
        self.circ[self.head] = val
        return self.win_sum / min(self.cnt, self.sz)

    def next_sol_deque(self, val: int) -> float:
        # same logic as next_fxr but cleaner code
        # XXX: common snippet: min(sz, cnt), or max(0, i-k) in contains duplicates III
        self.cnt += 1
        self.win.append(val)
        # 0 generalized the win_sum update
        tail = self.win.popleft() if self.cnt > self.sz else 0
        self.win_sum = self.win_sum - tail + val
        return self.win_sum / min(self.sz, self.cnt)

    def next_fxr(self, val: int) -> float:
        """
        Your runtime beats 63.34 % of python3 submissions.
        T: O(1)
        """
        self.win.append(val)
        if self.cnt == self.sz:
            self.win_sum = self.win_sum - self.win.popleft() + val
        else:
            self.cnt += 1
            self.win_sum += val
        return self.win_sum / self.cnt

    def next_1(self, val: int) -> float:
        """
        Your runtime beats 5.95 % of python3 submissions
        T: O(2N) due to sum() and len()
        """
        self.win.append(val)
        if len(self.win) > self.sz:
            self.win.popleft()
        return sum(self.win) / len(self.win)
