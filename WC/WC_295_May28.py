"""
Weekly Contest 295, May 28 2022
3/4
Q3 WA, acceptance rate = 3%
ranking 888! 1st time < 1k. :)
"""

from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dst = (m - 1, n - 1)
        s = (0, 0)
        pq = []
        heappush(pq, (0, s))
        dist = defaultdict(lambda: 2e9)
        dist[s] = 0
        while pq:
            d, u = heappop(pq)
            if d > dist[u]:
                continue
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i, j = u
                x, y = i + dx, j + dy
                v = (x, y)
                if 0 <= x < m and 0 <= y < n:
                    w = grid[x][y]
                    if dist[u] + w >= dist[v]:
                        continue
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
        return dist[dst]

    def totalSteps(self, nums: List[int]) -> int:
        pre = set()
        l = 0
        ops = 0
        while True:
            # shrink
            i = 0
            j = 1
            cur = set()
            while i < j < len(nums):
                while i < len(nums) and i in pre:
                    i += 1
                j = i + 1
                while j < len(nums) and j in pre:
                    j += 1

                if i < j < len(nums) and nums[i] > nums[j]:
                    cur.add(j)
                i = j + 1
            if len(cur) == 0:
                break
            ops += 1
            pre.update(cur)
            print(pre)
        return ops

    def discountPrices(self, sentence: str, discount: int) -> str:
        res = sentence.split()
        for i, w in enumerate(res):
            num = False
            if len(w) > 1 and w.startswith("$"):
                dot = 0
                for c in w[1:]:
                    if c == ".":
                        dot += 1
                        if dot > 1:
                            break
                    elif not c.isdigit():
                        break
                else:
                    num = True
            if num:
                print(w)
                p = float(w[1:]) * (1 - discount / 100)
                res[i] = f"${p:.2f}"
        return " ".join(res)

    def rearrangeCharacters(self, s: str, target: str) -> int:
        sd, td = Counter(s), Counter(target)
        ans = float("inf")
        for c in td:
            ans = min(ans, sd[c] // td[c])
        return ans


sl = Solution()
assert sl.totalSteps([10, 1, 2, 3, 4, 5, 6, 1, 2, 3]) == 6
# print(sl.totalSteps(nums=[5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]))
# print(sl.totalSteps(nums=[4, 5, 7, 7, 13]))
# print(sl.minimumObstacles(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]]))
# print(sl.minimumObstacles(grid=[[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]))
# print(sl.minimumObstacles(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]]))
# print(
#     sl.discountPrices(
#         sentence="1 2 $3 4 $5 $6 7 8$ $9 $10$",
#         discount=100
#         # sentence="there are $1 $2 and 5$ candies in the shop", discount=50
#     )
# )
# print(sl.rearrangeCharacters(s="ilovecodingonleetcode", target="code"))
# print(sl.rearrangeCharacters(s="abcba", target="abc"))
