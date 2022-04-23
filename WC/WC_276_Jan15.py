'''
WC 276
'''
from collections import defaultdict, deque
from typing import List
from functools import cache
from heapq import heapify, heappop, heappush


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i:i + k])
        if len(ans[-1]) < k:
            ans[-1] += fill * (k - len(ans[-1]))
        return ans

    def minMoves1(self, target: int, maxDoubles: int) -> int:
        @cache
        def dp(i, left):
            # print(i, left)
            if i == target:
                return 0
            if target % 2 == 0 and i == target // 2 and left > 0:
                return 1
            if i == target - 1:
                return 1

            ans = 0
            jump = dp(i + 1, left)
            if i * 2 <= target and left > 0:
                jump = min(jump, dp(i * 2, left - 1))
            # print(i, left, jump + 1)
            return ans + jump + 1

        return dp(1, maxDoubles)

    def minMoves(self, target: int, maxDoubles: int) -> int:
        jump = 0
        left = maxDoubles
        while target > 1:
            if left == 0:
                jump += target - 1
                break
            if target % 2 == 0 and left:
                target //= 2
                left -= 1
            else:
                target -= 1
            jump += 1
        return jump

    def mostPoints(self, questions: List[List[int]]) -> int:
        ans = defaultdict(int)
        lookup = defaultdict()

        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            return max(dp(i + 1),
                       dp(i + questions[i][1] + 1) + questions[i][0])

        return dp(0)

    def maxRunTime_WA(self, n: int, batteries: List[int]) -> int:
        """
        Failed in 12, [11, 89, 16, 32, 70, 67, 35, 35, 31, 24, 41, 29, 6, 53, 78, 83]
        """
        def mx_push(pq, v):
            heappush(pq, -v)

        def mx_pop(pq):
            return -heappop(pq)

        pq = []  # n top battery

        for b in batteries:
            mx_push(pq, b)

        time = 0
        while True:
            if len(pq) < n:
                return time
            outn = []
            for _ in range(n):
                outn.append(mx_pop(pq))
            min_n = outn[-1]
            use = 1
            use = max(use, min_n - 1)

            time += use
            for b in outn:
                if b - use <= 0:
                    continue
                mx_push(pq, b - use)
        print(time)
        return time


sl = Solution()
# print(sl.divideString(s="abcdefghi", k=3, fill="x"))
# print(sl.divideString(s="abcdefghij", k=3, fill="x"))

# print(sl.minMoves(target=5, maxDoubles=0))
# print(sl.minMoves(target=19, maxDoubles=2))
# print(sl.minMoves(target=10, maxDoubles=4))
# print(sl.minMoves(766972377, 92))
# print(sl.minMoves(656101987, 1))

# print(sl.mostPoints(questions=[[3, 2], [4, 3], [4, 4], [2, 5]]))
# print(sl.mostPoints(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]))

# print(sl.maxRunTime(n=2, batteries=[3, 3, 3]))
# print(sl.maxRunTime(n=2, batteries=[1, 1, 1, 1]))
print(
    sl.maxRunTime(
        12, [11, 89, 16, 32, 70, 67, 35, 35, 31, 24, 41, 29, 6, 53, 78, 83]))
