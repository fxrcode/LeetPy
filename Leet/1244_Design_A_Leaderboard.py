"""
Weekly Special (Dec 29, 2021)

✅ GOOD Data Structure Design (SortedContainer)
tag: medium, design
"""


from collections import defaultdict
from heapq import heappop, heappush
from random import randint

from sortedcontainers import SortedDict


class Leaderboard:
    """
    Runtime: 149 ms, faster than 7.79% of Python3 online submissions for Design A Leaderboard.

    T: for design problem, we need to break down Complexity per API!
    addScore: O(logN)
    top: O(K)
    reset: O(logN)
    """

    def __init__(self):
        self.scores = dict()
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            cnt = self.sortedScores.get(-preScore)
            if cnt == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = cnt - 1

            newScore = preScore + score
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1

    def top(self, K: int) -> int:
        end, total = 0, K
        for k, v in self.sortedScores.items():
            cnt = self.sortedScores.get(k)
            for _ in range(min(end, cnt)):
                total += k
                cnt += 1
        return total

    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.sortedScores[playerId]


class Leaderboard_slow:
    def __init__(self):
        self.p2s = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.p2s[playerId] += score

    def top_sort_heap(self, K: int) -> int:
        """
        Runtime: 112 ms, faster than 17.08% of Python3 online submissions for Design A Leaderboard.

        T: O(K + NlogK)
        """
        mink = []
        for k, v in self.p2s.items():
            heappush(mink, (v, k))
            if len(mink) > K:
                heappop(mink)
        return sum(v for v, k in mink)

    def top(self, K):
        """
        Runtime: 120 ms, faster than 14.30% of Python3 online submissions for Design A Leaderboard.

        T:O(N)
        """
        A = [(-v, k) for k, v in self.p2s.items()]

        def partition(l, r):
            o = randint(l, r)
            p = A[o]
            A[o], A[r] = A[r], A[o]

            i = l - 1
            for j in range(l, r):
                if A[j][0] < p[0]:
                    i += 1
                    A[i], A[j] = A[j], A[i]
            i += 1
            A[i], A[r] = A[r], A[i]
            return i

        l, r = 0, len(self.p2s) - 1
        while l < r:
            pi = partition(l, r)
            if pi == K - 1:
                break
            elif pi < K - 1:
                l = pi + 1
            else:
                r = pi

        return sum(-v for v, k in A[:K])

    def reset(self, playerId: int) -> None:
        self.p2s[playerId] = 0
