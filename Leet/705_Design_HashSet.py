"""
Tag: Medium, Hash, Design
Lookback:
- 9chap MOD=33, big prime for keyspace
https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/
Leetcode Explore: Hash Table. Design a Hash Table
"""


class MyHashSet:
    """
    Runtime: 214 ms, faster than 76.20% of Python3 online submissions for Design HashSet.

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

    def add(self, key: int) -> None:
        h = self._hash(key)
        if not key in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key: int) -> bool:
        h = self._hash(key)
        return key in self.buckets[h]
