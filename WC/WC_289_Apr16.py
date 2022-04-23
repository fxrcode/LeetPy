"""
Apr 16, 2022
2/4
"""


from collections import Counter, defaultdict
from functools import cache
from typing import List


class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        @cache
        def twofive(x):
            t, f = 0, 0

            while x % 5 == 0:
                f += 1
                x //= 5
            while x % 2 == 0:
                t += 1
                x //= 2
            return t, f

        R = defaultdict(lambda: [0, 0])
        C = defaultdict(lambda: [0, 0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                t, f = twofive(grid[r][c])
                rt, rf = R[(r, c - 1)]
                ct, cf = C[(r - 1, c)]
                R[(r, c)] = [rt + t, rf + f]
                C[(r, c)] = [ct + t, cf + f]

        print(R, C)
        t, f = 0, 0
        m, n = len(grid), len(grid[0])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                rt, rf = R[(r, c)]
                ct, cf = C[(r, c)]
                Rt, Rf = R[(r, n - 1)]
                Ct, Cf = C[(m - 1, c)]

                t0, f0 = twofive(grid[r][c])
                # U+L
                tt, ff = rt + ct - t0, rf + cf - f0
                if tt > t and ff > f:
                    t, f = tt, ff

                # U+R
                tt, ff = ct + Rt - rt, cf + Rf - rf
                if tt > t and ff > f:
                    t, f = tt, ff
                # D+L
                tt, ff = Ct - ct + rt, Cf - cf + rf
                if tt > t and ff > f:
                    t, f = tt, ff
                # D+R
                tt, ff = t0 + Ct - ct + Rt - rt, f0 + Cf - cf + Rf - rf
                if tt > t and ff > f:
                    t, f = tt, ff
        # return min(t, f)
        return t, f

    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        ans = 0
        for f in cnt.values():
            if f % 3 == 0:
                ans += f // 3
            elif f % 3 == 1:
                if f == 1:
                    return -1
                else:
                    ans += (f - 4) // 3 + 2
            else:  # == 2
                ans += f // 3 + 1
        return ans

    def digitSum(self, s: str, k: int) -> str:
        tmp = []
        t = list(map(int, s))
        print(t)
        while True:
            if len(t) <= k:
                break
            for i in range(0, len(t), k):
                tmp.append(str(sum(t[i : i + k])))
            t = list(map(int, "".join(tmp)))
            tmp = []
            print(t)
        return "".join(map(str, t))


sl = Solution()


def twofive(x):
    t, f = 0, 0

    if x % 5 == 0:
        for f in range(4, 0, -1):
            if x % (5**f) == 0:
                break
        x //= 5**f
    if x % 2 == 0:
        for t in range(9, 0, -1):
            if x % (2**t) == 0:
                break
    return t, f


# print(twofive(230))
print(
    sl.maxTrailingZeros(
        [
            [437, 230, 648, 905, 744, 416],
            [39, 193, 421, 344, 755, 154],
            [480, 200, 820, 226, 681, 663],
            [658, 65, 689, 621, 398, 608],
            [680, 741, 889, 297, 530, 547],
            [809, 760, 975, 874, 524, 717],
        ]
    )
)
# print(
#     sl.maxTrailingZeros(
#         grid=[[23, 17, 15, 3, 20], [8, 1, 20, 27, 11], [9, 4, 6, 2, 21], [40, 9, 1, 10, 6], [22, 7, 4, 5, 3]]
#     )
# )
# print(sl.maxTrailingZeros(grid=[[4, 3, 2], [7, 6, 1], [8, 8, 8]]))
# print(sl.minimumRounds(tasks=[2, 3, 3]))
# print(sl.minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
# print(sl.digitSum(s="11111222223", k=3))
# print(sl.digitSum(s="00000000", k=3))
