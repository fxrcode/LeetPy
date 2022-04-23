from typing import List
from heapq import heapify, heappop
from collections import defaultdict


class Solution:
    def checkString(self, s: str) -> bool:
        pass

    def numberOfBeams(self, bank: List[str]) -> int:
        devs = []
        for b in bank:
            ones = 0
            for c in b:
                if c == '1':
                    ones += 1
            devs.append(ones)
        ans = 0
        for i, j in zip(devs, devs[1:]):
            ans += i*j
        return ans

    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        heapify(asteroids)
        while asteroids:
            mn = heappop(asteroids)
            print(mn)
            if mn <= mass:
                mass += mn
            else:
                return False
        return True

    def maximumInvitations(self, favorite: List[int]) -> int:
        AL = {i: [] for i in range(len(favorite))}
        INDEG = {i: 0 for i in range(len(favorite))}
        for i, f in enumerate(favorite):
            AL[i].append(f)
            INDEG[f] += 1

        print(AL)

        WHITE, GRAY, BLACK = 0, 1, 2
        colr = defaultdict(int)
        mx = 0

        def checkmx():
            nonlocal mx
            sumgray = 0
            path = []
            gt2 = 0
            for k, v in colr.items():
                if v == 1:
                    sumgray += 1
                    path.append(k)
                    if INDEG[k] > 1:
                        gt2 = 1

            if sumgray == 2 and gt2:
                sumgray = 3

            print(path)

            mx = max(mx, sumgray)

        def dfs(u, colr):
            if u == 5:
                print('hei')
            colr[u] = GRAY
            for v in AL[u]:
                if colr[v] == 0:
                    dfs(v, colr)
                if colr[v] == 1:
                    checkmx()
                    continue
            colr[u] = BLACK

        for u in AL:
            colr.clear()
            dfs(u, colr)
        return mx


sl = Solution()
# print(sl.asteroidsDestroyed(mass=5, asteroids=[4, 9, 23, 4]))

# print(sl.maximumInvitations(favorite=[2, 2, 1, 2]))
# print(sl.maximumInvitations(favorite=[1, 2, 0]))
# print(sl.maximumInvitations(favorite=[3, 0, 1, 4, 1]))
print(sl.maximumInvitations([1, 0, 0, 2, 1, 4]))
