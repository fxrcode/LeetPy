"""
tag: medium, slide-window
Lookback
- I didn't fully understand sliding window template before! 4Q to ask in using template
- 1st time f-string f'{expr=}'. <f-strings support = for self-documenting expressions and debugging>
- 1st time `itertools.groupby(iterable,keyfunc)->(key,group)`
"""
from collections import defaultdict
from itertools import groupby

MOD = 10**9 + 7


class Solution:
    def countHomogenous(self, s: str) -> int:
        def fxr():
            """
            Runtime: 678 ms, faster than 5.45% of Python3 online submissions for Count Number of Homogenous Substrings.

            T: O(N)

            Boomed by using set() rather dict() as window, keep debugging for 3 days
            labuladong classical sliding-window template
            """
            l, r = 0, 0
            ans = 0
            win = defaultdict(int)
            while r < len(s):
                c = s[r]
                win[c] += 1
                r += 1
                while len(win) > 1:
                    d = s[l]
                    win[d] -= 1
                    if win[d] == 0:
                        win.pop(d)
                    l += 1

                # !assert: win size == 1
                print(f"{len(win)=}, {win=}, {(l, r)=}, {s[l:r]=}")
                ans += r - l
                ans %= MOD
            return ans

        def lee215_groupby():
            """
            Runtime: 123 ms, faster than 91.03% of Python3 online submissions for Count Number of Homogenous Substrings.

            https://leetcode.com/problems/count-number-of-homogenous-substrings/discuss/1064530/JavaC%2B%2BPython-Straight-Forward

            T: O(N)

            In [63]: for key,grp in groupby(s):
                ...:     print(key,list(grp))
                ...:
                ...:
            a ['a']
            b ['b', 'b']
            c ['c', 'c', 'c']
            a ['a', 'a']
            """
            res = 0
            for c, group in groupby(s):
                n = len(list(group))
                res += n * (n + 1) // 2
            return res % MOD

        def likoujiajia():
            """
            https://leetcode-cn.com/problems/count-number-of-homogenous-substrings/solution/li-kou-jia-jia-hua-dong-chuang-kou-ji-sh-may7/
            """
            l, r = 0, 1
            ans = 0
            cnt = 1
            A = s + "#"
            while r < len(A):
                if A[l] != A[r]:
                    ans += (cnt + 1) * cnt // 2
                    cnt = 1
                    l = r
                else:
                    cnt += 1
                r += 1
            return ans % MOD

        # return fxr()
        # return likoujiajia()
        return lee215_groupby()


sl = Solution()
print(sl.countHomogenous(s="abbcccaa"))
# print(sl.countHomogenous(s="xy"))
# print(sl.countHomogenous(s="zzzzz"))
