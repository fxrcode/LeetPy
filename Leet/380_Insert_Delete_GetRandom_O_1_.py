"""
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1141/
Leetcode Explore: Hash Table. Conclusion

Implement the RandomizedSet class:


"""
from random import choice


class RandomizedSet:
    """
    Your runtime beats 94.24 % of python3 submissions.

    REF: huahua https://www.youtube.com/watch?v=y240Qh9H9uk
    """

    def __init__(self):
        self.v2i = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val in self.v2i:
            return False
        self.l.append(val)
        self.v2i[val] = len(self.l) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.v2i:
            return False
        pos = self.v2i[val]
        last_val = self.l[-1]
        # swap val with the last item. No need to swap, just overwrite!
        self.l[pos] = last_val
        self.v2i[last_val] = pos
        # remove the last item
        self.v2i.pop(val)
        self.l.pop()
        return True

        """
        ri = self.v2i[val]
        self.v2i[self.l[-1]] = ri
        self.l[-1], self.l[ri] = self.l[ri], self.l[-1]
        # remove last val's mapping and item in list
        del self.v2i[self.l[-1]]
        self.l.pop()
        return True
        """

    def getRandom(self) -> int:
        # self.s.
        # XXX: no idea. How to access any value?
        #       Ans: list support random access by index!
        return choice(self.l)


"""
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
"""
