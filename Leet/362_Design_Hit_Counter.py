"""
tag: Medium, 
Lookback:
- Time window (5min, 1hr, 1day Top k items), can be System design problem
- Got 1 in coinbase Karat phone screen
"""

from bisect import bisect_left, bisect_right
from collections import deque


class HitCounter:
    """
    Approach #2: Using Deque with Pairs

    T: O(1)
    M: O(1)
    """

    def __init__(self):
        self.q = deque()
        self.total = 0

    def hit(self, timestamp: int) -> None:
        if self.q and self.q[-1][0] == timestamp:
            self.q[-1][1] += 1
        else:
            self.q.append([timestamp, 1])
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        while self.q:
            diff = timestamp - self.q[0][0]
            if diff >= 300:
                x = self.q.popleft()
                self.total -= x[1]
            else:
                break
        return self.total


class HitCounter_fxr:
    """
    Runtime: 49 ms, faster than 38.93% of Python3 online submissions for Design Hit Counter.

    """

    def __init__(self):
        self.wind = deque()

    def _pop_old(self, ts):
        while self.wind:
            if ts - 300 + 1 > self.wind[0]:
                self.wind.popleft()
            else:
                break

    def hit(self, timestamp: int) -> None:
        self.wind.append(timestamp)
        self._pop_old(timestamp)

    def getHits(self, timestamp: int) -> int:
        self._pop_old(timestamp)
        lo, hi = timestamp - 300 + 1, timestamp
        """
        range_count_query (common pattern of bisect usage)
        count(lo...hi) = count(<=hi) - count(<lo)
        reminds me of slide-window exact(k) = atMost(k) - atMost(k-1)
        """
        return bisect_right(self.wind, hi) - bisect_left(self.wind, lo)


# Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
print(obj.getHits(4))
obj.hit(300)
print(obj.getHits(300))
print(obj.getHits(301))
