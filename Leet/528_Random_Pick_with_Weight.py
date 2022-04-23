"""
✅ GOOD Probability
FB tag (medium, Top50)
tag: math, logic
Lookback:
- - code is simple, but logic/math is hard.
- similar: 1920. a = b*q+r (#41)

[ ] REDO
XXX: This is actually a very practical problem which appears often in the scenario
    where we need to do sampling over a set of data.

Nowadays, people talk a lot about machine learning algorithms.
    As many would reckon, one of the basic operations involved in training a machine learning algorithm (e.g. Decision Tree)
    is to sample a batch of data and feed them into the model, rather than taking the entire data set.
"""
from bisect import bisect, bisect_left
from collections import defaultdict
from itertools import accumulate
from random import randint
from typing import List


class TwoLiner:
    # https://leetcode.com/problems/random-pick-with-weight/discuss/154475/Python-1-liners-using-builtin-functions
    def __init__(self, w):
        self.w = list(accumulate(w))

    def pickIndex(self):
        return bisect.bisect_left(self.w, randint(1, self.w[-1]))


class Solution:
    """
    Runtime: 228 ms, faster than 88.69% of Python3
    Memory Usage: 18.6 MB, less than 96.03% of Python3

    https://labuladong.github.io/algo/2/21/64/

    """

    def __init__(self, w: List[int]):
        # T: O(N), M: O(N)
        self.P = [0] * (len(w) + 1)
        for i in range(len(w)):
            self.P[i + 1] = self.P[i] + w[i]

    def pickIndex(self) -> int:
        # T: O(logN)
        r = randint(1, self.P[-1])
        i = bisect.bisect_left(self.P, r)
        return i - 1


def play(x):
    pre = [1, 4, 6, 7]
    i = bisect_left(pre, x)
    if i == len(pre):
        print("all < x")
    else:
        print(pre[i])


# play(5)
# play(0)
# play(7)

sl = Solution(w=[1, 3, 2, 1])
d = defaultdict(int)
print(sl.pickIndex())

MONTE = 100000
for _ in range(MONTE):
    d[sl.pickIndex()] += 1

kv = sorted(d.items(), key=lambda kv: (kv[0]))

for k, v in kv:
    print(k, v / MONTE)
