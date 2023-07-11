"""
Weekly Contest 268 (Nov 20, 2021)
I solved first 2 problems, skip 3rd without trying since I thought its Segment Tree.
Spent last 1hr on this 4th problem.

Top-1	uwi  	score:18	time: 0:12:21
---
Q4. Total Accepted: 470
"""
from functools import cache


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def codemonkey113(n):
            def to_base_b(v10, b):
                if v10 == 0:
                    return "0"
                d = []
                while v10:
                    d.append(str(v10 % b))
                    v10 //= b
                return "".join(d[::-1])

            @cache
            def F(d, zero) -> list[str]:
                """
                DFS to get all base10 d-digits mirror numbers (in str format)
                """
                if d == 0:
                    return []
                if d == 1:
                    return (
                        [str(i) for i in range(10)]
                        if zero
                        else [str(i) for i in range(1, 10)]
                    )
                elif d == 2:
                    res = [str(i) for i in range(11, 100, 11)]
                    if zero:
                        res = ["00"] + res
                    return res
                else:
                    combos = []
                    choices = (
                        [str(i) for i in range(10)]
                        if zero
                        else [str(i) for i in range(1, 10)]
                    )
                    for c in choices:
                        for mid in F(d - 2, True):
                            combos.append("{}{}{}".format(c, mid, c))
                    return combos

            d = 1
            res = 0
            while n:
                for a10 in F(d, False):
                    if n == 0:
                        return res
                    try_ = to_base_b(int(a10), k)
                    if try_[::-1] == try_:
                        res += int(a10)
                        n -= 1
                d += 1
            return res

        def fxr_WA():
            def back(l, r, stop, path, res, length):
                if l > r:
                    res.append(path[:])
                    return False
                if stop:
                    return True

                for i in range(k):
                    if r == length - 1:
                        if i == 0:
                            continue
                    path[l] = str(i)
                    path[r] = str(i)
                    back(l + 1, r - 1, stop, path, res, length)

                    path[l] = "x"
                    path[r] = "x"

            res = []
            # back(0,3, list('xxxx'), res, 4)
            # back(0,1, list('xx'), res, 2)
            # print(res)

            def check(s, k):
                v10 = 0
                for i in range(len(s)):
                    v10 = v10 * k + int(s[i])
                # print(v10)
                if v10 % 11 == v10 and v10 != 10:
                    print(v10, "".join(s))
                    return v10
                else:
                    return 0

            cand = []
            cnt = n
            for length in range(1, 10):
                res = []
                back(0, length - 1, cnt == 0, ["x"] * length, res, length)
                for v in res:
                    val = check(v, k)
                    print(val)
                    if val:
                        # cnt -= 1
                        cand.append(val)
                        if cnt == 0:
                            break
            return sum(cand)

            # print(check(list('1011'), 2))

        return codemonkey113(n)


sl = Solution()
print(sl.kMirror(k=3, n=7))
print(sl.kMirror(k=7, n=17))
