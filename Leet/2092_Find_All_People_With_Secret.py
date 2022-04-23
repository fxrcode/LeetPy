'''
Weekly Contest 269 (Nov 27, 2021)

[ ] TODO: not AC yet!
'''

from typing import List
from collections import defaultdict


class UF:
    """
    https://github.com/stevenhalim/cpbook-code/blob/master/ch2/ourown/unionfind_ds.py
    CP4's Most concise UF, supports numdisjoint, and sizes. Used for Kruskal or Hard Graph Partition problems.
    And it's identical to https://leetcode.com/problems/largest-component-size-by-common-factor/solution/
    """

    def __init__(self, n) -> None:
        self.p = list(range(n))
        self.ranks = [0]*n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, i) -> int:
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, i, j) -> int:
        x, y = map(self.find, [i, j])
        if x == y:
            return x
        if self.ranks[x] > self.ranks[y]:
            x, y = y, x
        self.p[x] = y
        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        self.sizes[y] += self.sizes[x]
        self.numdisjoint -= 1
        return y

    def sizeof_set(self, i):
        return self.sizes[self.find(i)]

    def size(self, x):
        return self.sizes[self.find(x)]

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def findAllPeople_WA(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # meetings.sort(key=lambda tu: tu[2])
        times = []
        time_to_ppl = defaultdict(set)
        for a, b, t in meetings:
            time_to_ppl[t].add((a, b))
            times.append(t)
        times.sort()

        dsu = UF(n)
        dsu.union(0, firstPerson)
        # for a, b, t in meetings:
        #     if dsu.find(a) == dsu.find(0) or dsu.find(b) == dsu.find(0):
        #         dsu.union(a, b)
        for t in times:
            to_remove = set()
            for a, b in time_to_ppl[t]:
                if dsu.connected(a, 0) or dsu.connected(b, 0):
                    dsu.union(0, a)
                    dsu.union(0, b)
                    to_remove.add((a, b))

            for a, b in time_to_ppl[t]:
                if (a, b) in to_remove:
                    continue
                if dsu.connected(a, 0) or dsu.connected(b, 0):
                    dsu.union(0, a)
                    dsu.union(0, b)

        res = set([0, firstPerson])
        for i in range(n):
            if dsu.find(i) == dsu.find(0):
                res.add(i)
        return list(res)
