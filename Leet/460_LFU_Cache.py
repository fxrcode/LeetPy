'''
✅ GOOD Design
HARDER than LRU

https://stackoverflow.com/questions/34305003/difference-between-dictionary-and-ordereddict
From 3.8+, orderedDict is no need any more! Dict = OrderedDict!
'''

from collections import defaultdict


class Node:
    def __init__(self, key, val, frq) -> None:
        self.k = key
        self.v = val
        self.f = frq

    def __repr__(self) -> str:
        return ','.join([str(self.k), str(self.v), str(self.f)])


class LFUCache:
    """
    Runtime: 1228 ms, faster than 15.11% of Python3 online submissions for LFU Cache.

    careful on 0-capcacity
    ["LFUCache","put","get"]
    [[0],[0,0],[0]]
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.k2n = dict()
        self.f2n = defaultdict(dict)
        self.mnf = None  # mnf: min freq

    def get(self, key: int) -> int:
        if key not in self.k2n:
            return -1
        node = self.k2n[key]
        # cuz node has been "get", its frequency would go up
        # remove its old pair in freq2node
        del self.f2n[node.f][key]

        # further check whether old node.freq is empty in freq2node
        if not self.f2n[node.f]:
            del self.f2n[node.f]

        # update freq
        node.f += 1
        self.f2n[node.f][key] = node

        # update min_freq
        if not self.f2n[self.mnf]:
            self.mnf += 1
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.k2n:
            self.k2n[key].v = value
            # update key/freq and f2n
            _ = self.get(key)
            return

        # already reached capacity
        if len(self.k2n) == self.cap:
            # evict LRU
            d = self.f2n[self.mnf]
            node = d[next(iter(d))]
            del d[node.k]
            del self.k2n[node.k]

        # add new key/val node
        self.f2n[1][key] = self.k2n[key] = Node(key, value, 1)
        self.mnf = 1
        return

    ''' BUGGGGY
    def get(self, key: int) -> int:
        if key not in self.k2n:
            return -1
        node = self.k2n[key]
        print(self.f2n, node)
        self.f2n[node.f].pop(key)
        node.f += 1
        self.f2n[node.f][key] = node

        if not self.f2n[self.mnf]:
            self.mnf += 1
        return node.v

    def put(self, key: int, value: int) -> None:
        if key in self.k2n:
            self.k2n.pop(key)
        else:
            if len(self.k2n) == self.cap:
                d = self.f2n[self.mnf]
                del d[next(iter(d))]
        # finally put
        node = Node(key, value, 1)
        self.k2n[key] = node
        self.f2n[1][key] = node
        self.mnf = 1
    '''
