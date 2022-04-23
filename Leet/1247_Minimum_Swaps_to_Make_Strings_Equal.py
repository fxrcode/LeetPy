"""
Tag: logic
Lookback:
- Googler: @wgpass【脑经急转弯】
"""

from collections import Counter, deque


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        def wg_brainteaser():
            """
            Runtime: 71 ms, faster than 5.26% of Python3 online submissions for Minimum Swaps to Make Strings Equal.

            https://www.bilibili.com/video/BV1TF411v7WA
            """
            xy, yx = 0, 0
            for c1, c2 in zip(s1, s2):
                if c1 == "x" and c2 == "y":
                    xy += 1
                elif c1 == "y" and c2 == "x":
                    yx += 1

            ans = xy // 2 + yx // 2
            mod1, mod2 = xy % 2, yx % 2
            if mod1 == mod2:
                ans += mod1 * 2
                return ans
            else:
                return -1

        return wg_brainteaser()

        def fxr_bfs():
            """
            TLE: 18 / 70 test cases passed.

            ("xyyxxyyyyyyy","xxxyxyxxxxyx")

            """

            def swap(a, b, i, j):
                c, d = a[:i] + b[j] + a[i + 1 :], b[:j] + a[i] + b[j + 1 :]
                return [c, d]

            if any(v & 1 for _, v in Counter((s1 + s2)).items()):
                return -1
            q = deque([(s1, s2, -1, -1)])
            visited = set([(s1, s2)])
            l = len(s1)
            steps = 0
            while q:
                for _ in range(len(q)):
                    a, b, pi, pj = q.popleft()
                    if a == b:
                        return steps
                    for i in range(l):
                        for j in range(l):
                            if pi == i and pj == j or a[i] == b[j]:
                                continue
                            aa, bb = swap(a, b, i, j)
                            if (aa, bb) not in visited:
                                visited.add((aa, bb))
                                q.append((aa, bb, i, j))
                steps += 1
            return -1


sl = Solution()
# print(sl.minimumSwap(s1='xx', s2='yy'))
# print(sl.minimumSwap(s1="xy", s2="yx"))
print(sl.minimumSwap("xyyxxyyyyyyy", "xxxyxyxxxxyx"))
