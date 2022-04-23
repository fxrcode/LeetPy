"""
Tag: Medium, Hash, Design
Lookback:
- 9chap MOD=33, big prime for keyspace
https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/
Leetcode Explore: Hash Table. Design a Hash Table
"""


class MyHashMap:
    """
    Runtime: 312 ms, faster than 65.78% of Python3 online submissions for Design HashMap.
    Simpler than LRU/LFU. You should design high level functions, and reuse it.
    """

    def __init__(self):
        self.keyspace = 1999
        self.rad = 33
        self.buckets = [[] for _ in range(self.keyspace)]

    def _hash(self, n):
        d, q = self.rad, self.keyspace
        h = 0
        while n:
            n, v = divmod(n, 10)
            h = (h * d + v) % q
        return h

    def put(self, key: int, value: int) -> None:
        h = self._hash(key)
        self.remove(key)
        self.buckets[h].append((key, value))

    def get(self, key: int) -> int:
        h = self._hash(key)
        for k, v in self.buckets[h]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        h = self._hash(key)
        for k, v in self.buckets[h]:
            if k == key:
                self.buckets[h].remove((k, v))


obj = MyHashMap()
obj.put((1, 1))
obj.put((2, 2))
obj.get(1)
obj.get(3)
obj.put((2, 1))
