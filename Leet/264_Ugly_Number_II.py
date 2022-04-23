"""
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        def happygirlzt(n):
            """
            Runtime: 128 ms, faster than 93.31% of Python3 online submissions for Ugly Number II.

            """
            dp = [0]*1690
            dp[0] = 1
            i2, i3, i5 = 0, 0, 0
            for i in range(1, n):
                # XXX: 花了点时间来理解这里：因为ugly number都是由 smaller ugly & [2,3,5]构成。所以用pointer的思想。
                tmp2, tmp3, tmp5 = 2*dp[i2], 3*dp[i3], 5*dp[i5]
                mn = min(tmp2, tmp3, tmp5)
                dp[i] = mn
                if dp[i] == tmp2:
                    i2 += 1
                if dp[i] == tmp3:
                    i3 += 1
                if dp[i] == tmp5:
                    i5 += 1
            ans = dp[n-1]
            print(ans)
            return ans

        def fxr_brute(n):
            def isugly(x):
                if n <= 0:
                    return False
                for p in [2, 3, 5]:
                    while x % p == 0:
                        x //= p
                return x == 1

            def isugly_fxr(x):
                # BAD coding...
                while x:
                    if x == 1:
                        return True
                    for u in [2, 3, 5]:
                        if x % u == 0:
                            x //= u
                            break
                    else:
                        return False

            def dummy():
                i = 1
                x = 1
                while i <= n:
                    if isugly(x):
                        i += 1
                        if i == n:
                            print(i, x)
                    x += 1

            dummy()

        # return fxr_brute(n)
        return happygirlzt(n)


sl = Solution()
sl.nthUglyNumber(12)
sl.nthUglyNumber(100)
sl.nthUglyNumber(1000)
