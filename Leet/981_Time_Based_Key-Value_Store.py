"""
tag: Medium, Bisect
Lookback:
- Google interview
- I always refer to cpython when I need to remember binary search:
https://github.com/python/cpython/blob/3.9/Lib/bisect.py#L15-L35
"""
from bisect import bisect_right
from collections import defaultdict


class TimeMap:
    """
    Runtime: 1099 ms, faster than 30.00% of Python3 online submissions for Time Based Key-Value Store.

    """

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ltv = self.kv[key]
        i = bisect_right(ltv, timestamp, key=lambda x: x[0])
        return ltv[i - 1][0] if i - 1 >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
