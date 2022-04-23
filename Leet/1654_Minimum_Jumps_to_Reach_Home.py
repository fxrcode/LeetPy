"""
✅ GOOD Logic (BFS/DFS)
Kevin

tag: medium
Lookback
- Bezout's Identity is what I'm thinking of ![](../pics/1654-bezout.png)
- Piecewise analysis from leetcode-cn
- BFS/DFS visited set deep dive

Similar:
991: Broken Calculator
"""

from collections import deque
from math import gcd
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        def CaptainTec():
            """
            Runtime: 154 ms, faster than 50.86% of Python3 online submissions for Minimum Jumps to Reach Home.

            https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/solution/python3-bfs-he-dfsjie-fa-by-captaintec/
            """
            vis = set(forbidden)
            key = -1
            UPPER = max(forbidden + [x]) + a + b

            def dfs(p, cnt, back):
                nonlocal key
                if key < 0 and 0 <= p <= UPPER:  # # 6000是往右探索的最大值，x最大为2000
                    if p == x:  # 第一次遍历到 x时的次数即为结果，暂存结果，不再递归
                        key = cnt
                        return
                    if p + a not in vis:
                        vis.add(p + a)  # 防止无限递归，比如 a = b 时，不加限制，就会出现无限递归
                        dfs(p + a, cnt + 1, 0)
                    if p - b not in vis and back != 1:  # 若back为1说明上次就是往后跳的
                        dfs(p - b, cnt + 1, 1)

            dfs(0, 0, 0)
            return key

        def SKX():
            """
            Runtime: 254 ms, faster than 17.38% of Python3 online submissions for Minimum Jumps to Reach Home.

            https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/solution/yao-zhu-yi-zu-ji-ji-he-zhong-bu-jin-ying-yv8t/
            """
            bad = set(forbidden)
            footprint = set()
            upper = max(forbidden + [x]) + a + b
            res = [1e6]

            def dfs(p, cnt, prev):
                """
                prev: last direction. True=backed, False=not backed
                """
                if not 0 <= p <= upper:
                    return
                if p in bad:
                    return
                if (p, prev) in footprint:
                    return
                if p == x:
                    res[0] = min(res[0], cnt)
                    return

                footprint.add((p, prev))

                dfs(p + a, cnt + 1, False)
                if not prev:
                    dfs(p - b, cnt + 1, True)

            dfs(0, 0, True)
            dfs(0, 0, False)
            return -1 if res[0] == 1e6 else res[0]

        def fxr_bfs():
            """
            Runtime: 100 ms, faster than 85.19% of Python3 online submissions for Minimum Jumps to Reach Home.

            https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/solution/python3-bfs-he-dfsjie-fa-by-captaintec/
            https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/solution/dao-jia-de-zui-shao-tiao-yue-ci-shu-zui-duan-lu-zh/

            """
            if x % gcd(a, b) != 0:
                return -1
            q = deque([(0, False, 0)])
            vis = set(forbidden)
            UPPER = max(forbidden + [x]) + a + 2 * b
            print(UPPER)
            # UPPER = 6000

            while q:
                pos, backed, jumps = q.popleft()
                if pos == x:
                    return jumps

                pa, pb = pos + a, pos - b
                if pa < UPPER and pa not in vis:
                    q.append((pa, False, jumps + 1))
                    vis.add(pa)
                if not backed and pb > 0 and pb not in vis:
                    q.append((pb, True, jumps + 1))
            return -1

        # return CaptainTec()
        # return SKX()
        return fxr_bfs()


sl = Solution()
# print(sl.minimumJumps(forbidden=[14, 4, 18, 1, 15], a=3, b=15, x=9))
# print(sl.minimumJumps(forbidden=[8, 3, 16, 6, 12, 20], a=15, b=13, x=11))
# print(sl.minimumJumps(forbidden=[1, 6, 2, 14, 5, 17, 4], a=16, b=9, x=7))
# print(sl.minimumJumps([], a=3, b=1, x=4))
forbidden = [
    162,
    118,
    178,
    152,
    167,
    100,
    40,
    74,
    199,
    186,
    26,
    73,
    200,
    127,
    30,
    124,
    193,
    84,
    184,
    36,
    103,
    149,
    153,
    9,
    54,
    154,
    133,
    95,
    45,
    198,
    79,
    157,
    64,
    122,
    59,
    71,
    48,
    177,
    82,
    35,
    14,
    176,
    16,
    108,
    111,
    6,
    168,
    31,
    134,
    164,
    136,
    72,
    98,
]
a, b, x = 29, 98, 80
print(sl.minimumJumps(forbidden, a, b, x))
