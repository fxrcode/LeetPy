'''
✅ GOOD Dict

https://stackoverflow.com/questions/34305003/difference-between-dictionary-and-ordereddict
From 3.8+, orderedDict is no need any more! Dict = OrderedDict!

'''


class LRUCache:
    """
    Runtime: 1037 ms, faster than 25.53% of Python3 online submissions for LRU Cache.

    https://leetcode.com/problems/lru-cache/discuss/850110/Python-3.7%2B.-No-need-to-use-OrderedDict.-Simply-use-the-regular-dict
    """

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        v = self.cache.pop(key)
        self.cache[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        else:
            if len(self.cache) == self.cap:
                # BUG: self.cache.popitem() LIFO order, so removes latest elem rather oldest!
                del self.cache[next(iter(self.cache))]
        self.cache[key] = value
