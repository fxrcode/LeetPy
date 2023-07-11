"""
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1122/
Leetcode Explore: Hash Table. Practical Application - HashSet

Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).
"""
from collections import deque


class Logger:
    """
    Runtime: 231 ms, faster than 15.68% of Python3 online submissions for Logger Rate Limiter.

    Official solution I: using deque and set to keep only recent 10 seconds window, and set to dedup.
    T: O(N), M: O(N)
    """

    def __init__(self):
        self.s = set()
        self.q = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.q:
            msg, ts = self.q[0]
            if timestamp - ts >= 10:
                self.q.popleft()
                self.s.remove(msg)
            else:
                break

        if message not in self.s:
            self.s.add(message)
            self.q.append((message, timestamp))
            return True
        else:
            return False


class Logger_fxr:
    def __init__(self):
        self.rate_lim = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Your runtime beats 32.81 % of python3 submissions.

        XXX: this is problemetic due to no garbage collection and self.rate_lim keeps unique messages!
        """
        if message not in self.rate_lim:
            self.rate_lim[message] = timestamp
            return True
        last_time = self.rate_lim[message]
        if timestamp - self.rate_lim[message] >= 10:
            self.rate_lim[message] = timestamp
            return True
        else:
            return False


"""
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
"""
