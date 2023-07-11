"""
Weekly Contest (Feb 26, 2022)
3/4 in 30min.
"""

from collections import Counter, deque
from typing import List


class Solution:
    def minimumFinishTime(
        self, tires: List[List[int]], changeTime: int, numLaps: int
    ) -> int:
        def bfs():
            q = deque([(i, 1, f, numLaps - 1) for i, (f, r) in enumerate(tires)])
            seen = set(q)
            while q:
                # print(q)
                for _ in range(len(q)):
                    if q[0][3] == 0:
                        return min(q, key=lambda x: x[2])[2]
                    t, x, tot, laps = q.popleft()
                    # print('popleft:', (t, x, tot, laps))
                    candidates = []
                    for i, (f, r) in enumerate(tires):
                        if i == t:
                            st = (t, x + 1, tot + f * pow(r, (x)), laps - 1)
                            candidates.append(st)
                        st = (i, 1, tot + changeTime + f, laps - 1)
                        candidates.append(st)
                    # opt = min(candidates, key=lambda x: x[2])
                    # print('opt:', opt)
                    for st in candidates:
                        if st not in seen:
                            q.append(st)

        return bfs()

        # def dfs(t, x, total, laps):
        #     print(t, x, total, laps)
        #     nonlocal opt
        #     if laps == 0:
        #         opt = min(opt, total)
        #         return

        #     for i, (f, r) in enumerate(tires):
        #         dfs(i, x + 1, total + f * pow(r, (x)), laps - 1)
        #         dfs(i, 1, total + changeTime + f, laps - 1)

        # opt = float('inf')
        # for i, (f, r) in enumerate(tires):
        #     dfs(i, 1, f, numLaps - 1)
        # return opt

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, totalTrips * max(time)
        print(l, r)
        while l < r:
            mid = (l + r) // 2
            count = sum(mid // b for b in time)
            # print(mid, count)
            if count >= totalTrips:
                r = mid
            else:
                l = mid + 1
        return l

    def minSteps(self, s: str, t: str) -> int:
        CS, CT = Counter(s), Counter(t)
        C = CS.copy()  # WTF
        for k, v in CT.items():
            if k not in C:
                C[k] = v
            else:
                C[k] = max(C[k], v)
        print(C)
        print(CS)
        print(C - CS)
        print(C - CT)
        return ((C - CS).total()) + ((C - CT).total())

    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(w.startswith(pref) for w in words)


sl = Solution()
# print(sl.prefixCount(words=["pay", "attention", "practice", "attend"], pref="at"))
# print(sl.prefixCount(words=["leetcode", "win", "loops", "success"], pref="code"))
# print(sl.minSteps(s="leetcode", t="coats"))

# print(sl.minimumTime(time=[1, 2, 3], totalTrips=5))
# print(sl.minimumTime(time=[2], totalTrips=1))
# print(sl.minimumTime(time=[5, 10, 10], totalTrips=9))

# print(sl.minimumFinishTime(tires=[[2, 3], [3, 4]], changeTime=5, numLaps=4))
print(sl.minimumFinishTime(tires=[[1, 10], [2, 2], [3, 4]], changeTime=6, numLaps=5))
print(sl.minimumFinishTime([[99, 7]], 85, 95))
