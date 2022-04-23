"""
https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75


"""
from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        def os_dp():
            """
            Runtime: 32 ms, faster than 77.23% of Python3 online submissions for Decode Ways.

            https://leetcode-cn.com/problems/decode-ways/solution/jie-ma-fang-fa-by-leetcode-solution-p8np/
            https://leetcode-cn.com/problems/decode-ways/solution/gong-shui-san-xie-gen-ju-shu-ju-fan-wei-ug3dd/
            XXX: this is hat of 70. Climbing Stairs
            """
            n = len(s)
            # F = [1] + [0]*n
            F = [1, 0, 0]

            for i in range(1, n+1):
                # XXX: must init F[i%3] = 0 since 2 cases can be neither/single/both valid!
                F[i % 3] = 0
                if s[i-1:i] != '0':
                    F[i % 3] = F[(i-1) % 3]
                if i-2 >= 0 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
                    F[i % 3] += F[(i-2) % 3]
            print(F)
            return F[n % 3]

        def os_memo():
            """
            Runtime: 28 ms, faster than 91.66% of Python3 online submissions for Decode Ways.

            XXX: OS find self-similar, and overlapping subproblems, so memoize dfs
            """
            @cache
            def dfs(idx):
                if idx == len(s):
                    return 1

                if s[idx] == '0':
                    return 0

                if idx == len(s)-1:
                    return 1

                ans = dfs(idx+1)
                if int(s[idx:idx+2]) < 27:
                    ans += dfs(idx+2)
                return ans
            return dfs(0)

        def fxr():
            """
            23 / 269 test cases passed.
            TLE: "111111111111111111111111111111111111111111111"

            1st thought: all decodes: so backtrack for all valid subsets
            """
            s2n = {str(i): i for i in range(1, 26+1)}

            def bt(idx, path, res):
                # no more decision to make
                if idx == len(s):
                    res.append(path[:])
                    return

                # recursive case, we have a decision to make
                # BUG: we can't skip! for i in range(start, len(s)):
                # select 1
                if s[idx] in s2n:
                    bt(idx+1, path+[s2n[s[idx]]], res)

                # select 2
                if idx+1 < len(s) and s[idx:idx+1+1] in s2n:
                    bt(idx+2, path+[s2n[s[idx:idx+2]]], res)

            res = []
            bt(0, [], res)
            return res

        # return fxr()
        # return os_memo()
        return os_dp()


sl = Solution()
print(sl.numDecodings('12'))
print(sl.numDecodings('226'))
print(sl.numDecodings('06'))
print(sl.numDecodings('11106'))
print(sl.numDecodings('111111111111111111111111111111111111111111111'))
