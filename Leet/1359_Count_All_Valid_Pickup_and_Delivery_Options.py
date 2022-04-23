"""
Daily Challenge (Mar 6, 2022)
tag: Hard, DP, Combinatonics
Lookback
- yiingziqing123: 不愧是小学奥数题 doordash一看就是中国老板小学的时候奥数学多了
- Good problem: you can tackle it w/ various routes/algs (math vs backtrack vs dp)
    - in backtrack, you can view in diff point (me brute force vs os abstract (unpicked, undelivered))
    - in math, you can interprete in various aspects (lee215 vs leet-cn's paul, gry vs os probability)

"""
from functools import cache

MOD = 10**9 + 7


class Solution:
    def countOrders(self, n: int) -> int:
        def gry_cn_math():
            """
            https://leetcode-cn.com/problems/count-all-valid-pickup-and-delivery-options/solution/shu-xue-jie-fa-6xing-by-gry-m21p/
            XXX: another point of view, most elegant!
                reminds me <从An到An+1> for the formula of f(n-1) => f(n)
            """
            if n == 1:
                return 1
            ans = 1
            for i in range(2, n + 1):
                ans = ans * (i * 2 - 1) * i % MOD
            return ans

        return gry_cn_math()

        def paul_cn_math():
            """
            Runtime: 66 ms, faster than 30.15% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
            https://leetcode-cn.com/problems/count-all-valid-pickup-and-delivery-options/solution/zu-he-shu-xue-ti-by-paulzfm/
            T: O(N)
            """
            total = 1
            for i in range(2, n + 1):
                spots = 2 * (i - 1) + 1
                # C(n,1): placements of connected (P_k, D_k); C(n,2): placements of separated (P_k, D_k)
                # C(n,1)=spots; C(n,2) = spots*(spots-1)//2
                choices = spots + spots * (spots - 1) // 2
                total = (total * choices) % MOD
            return total

        def os_topdown():
            @cache
            def dp(unpicked, undelivered):
                if unpicked == undelivered == 0:
                    return 1
                if unpicked < 0 or undelivered < 0 or unpicked > undelivered:
                    return 0
                # count all choices of picking up an order
                ans = unpicked * dp(unpicked - 1, undelivered)
                ans %= MOD

                """
                Q: why choices = (undelivered - unpicked), rather (undelivered)?
                Ans: restriction of picked before deliver!
                eg. unpicked: AB, undelivered: abcde, so we can one from (cde) to deliver. 
                    Cuz we need to wait for AB picked before deliver ab!
                """
                # !count all choices of delivering a PICKED order
                ans += (undelivered - unpicked) * dp(unpicked, undelivered - 1)
                ans %= MOD
                return ans

            return dp(n, n)

        # return os_topdown()

        def fxr_TLE():
            """
            prior Approach 1: Recursion with Memoization (Top-Down DP)
            !OP asked for "count" rather all "answers", we should DP rather backtrack, in order to speedup!

            """

            def bt(seen, path):
                if len(seen) == n * 2:
                    res.add(tuple(path))
                    return
                for pi in range(-n, 0):
                    if pi not in seen:
                        seen.add(pi)
                        bt(seen, path + [pi])
                        seen.remove(pi)
                for dj in range(1, n + 1):
                    if dj not in seen and -dj in seen:
                        seen.add(dj)
                        bt(seen, path + [dj])
                        seen.remove(dj)

            res = set()
            # P, D = list(range(-n, 0)), list(range(1, n + 1))
            bt(set(), [])
            # print(res)
            return len(res)


sl = Solution()
# print(sl.countOrders(n=1))
# print(sl.countOrders(n=2))
# print(sl.countOrders(n=3))
print(sl.countOrders(n=10))  # STUCK
