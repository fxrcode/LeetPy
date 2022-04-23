'''
Weekly Special (Nov 22)

✅ GOOD Data Structure Design

Lookback:
- OrderedDict, next(iter(od))
'''

from email.policy import default
from typing import List
from collections import deque, OrderedDict


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


d = {1: None, 3: None, 5: None}

it = iter(d)

for i in range(5):
    v = next(it, 'EOF')
    print(i, v)


class FirstUnique:
    """
    OS: best solution: O(1) for add/showFirstUnique
    Used OrderedDict, next/iter

    Runtime: 1765 ms, faster than 12.33% of Python3 online submissions for First Unique Number.

    """
    def __init__(self, nums: List[int]):
        self.q = OrderedDict()
        self.is_uniq = {}
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        if self.q:
            # XXX: We don't want to actually *remove* the value.
            # Seeing as OrderedDict has no "get first" method, the way that we can get
            # the first value is to create an iterator, and then get the "next" value
            # from that. Note that this is O(1).
            return next(iter(self.q))
        return -1

    def add(self, value: int) -> None:
        # case 1: we need to add v into q, and mark it unique
        if value not in self.is_uniq:
            self.is_uniq[value] = True
            self.q[value] = None
        # case 2: we need to mark it duplicate, then remove it from queue
        elif self.is_uniq[value]:
            self.is_uniq[value] = False
            self.q.pop(value)
        # case 3: do nothing!


class FirstUnique_os_dict:
    """
    Runtime: 868 ms, faster than 59.35% of Python3 online submissions for First Unique Number.
    Memory Usage: 57.4 MB, less than 43.65% of Python3 online submissions for First Unique Number.

    init: O(K)
    add: O(1)
    showFirstUnique: O(1) amortized!

    M: O(N)
    """
    def __init__(self, nums=List[int]) -> None:
        self.q = deque(nums)
        self.is_uniq = {}
        # common in data structure leet: reuse func!!!
        # XXX: if func has no return, use simple loop rather map!!! list(map(self.add, nums))
        for v in nums:
            self.add(v)

    def showFirstUnique(self) -> int:
        while self.q and not self.is_uniq[self.q[0]]:
            # !Interview Tip: Practice Overriding Your Brains "Assume" Mode!
            # XXX: cuz the problem only cares about first unique, and the q ACT as a global index!
            #   so you can of-course remove it after processing! This optimized later query since q reduce!
            #   btw, is_uniq stays the same when q pop because the REAL queue remains the same, so unique state is same.
            self.q.popleft()
        if self.q:
            return self.q[0]
        return -1

    def add(self, value) -> None:
        if value not in self.is_uniq:
            self.q.append(value)
            self.is_uniq[value] = True
        else:
            self.is_uniq[value] = False


class FirstUnique_fxr_complicate:
    """
    Runtime: 1361 ms, faster than 22.17% of Python3 online submissions for First Unique Number.
    Memory Usage: 83.1 MB, less than 15.01% of Python3 online submissions for First Unique Number.

    AC in 2nd.
    """
    def _dedup(self, v):
        if v in self.uniq:
            self.uniq.remove(v)
            self.dup.add(v)
        else:
            self.uniq.add(v)

    def __init__(self, nums: List[int]):
        dummy = t = ListNode(None)
        self.uniq = set()
        self.dup = set()
        for n in nums:
            t.next = ListNode(n)
            t = t.next
            self._dedup(n)

        self.first = dummy
        self.tail = t

    def showFirstUnique(self) -> int:
        if not self.uniq:
            return -1
        p = self.first
        if not p.val:
            p = p.next

        while p and p.val in self.dup:
            p = p.next
        if not p:
            # XXX: if not set first here, then TLE in case 15/20.
            self.first = self.tail
            return -1
        self.first = p
        return p.val

    def add(self, value: int) -> None:
        self.tail.next = ListNode(value)
        self.tail = self.tail.next
        self._dedup(value)


# Your FirstUnique object will be instantiated and called as such:
# fu = FirstUnique(nums=[2, 3, 5])
# # fu = FirstUnique_fxr_complicate(nums=[7, 7, 7, 7])
# print(fu.showFirstUnique())
# print(fu.showFirstUnique())
# fu.add(3)
# print(fu.showFirstUnique())
# fu.add(2)
# print(fu.showFirstUnique())
# fu.add(17)
# print(fu.showFirstUnique())
