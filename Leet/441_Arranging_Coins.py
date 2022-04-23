"""
Tag: Easy, bisect, math
Lookback:
- be fast to re-state into bisect
- math is COOL
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        def os_math():
            """
            Math: completing the math technique
            """
            return (int)((2 * n + 0.25) ** 0.5 - 0.5)

        def fxr_bisect():
            # Runtime: 36 ms, faster than 92.49% of Python3 online submissions for Arranging Coins.
            l, r = 0, n + 1
            while l < r:
                mid = (l + r) // 2
                if mid * (mid + 1) // 2 > n:
                    r = mid
                else:
                    l = mid + 1
            return l - 1

        return fxr_bisect()

        def fxr():
            """
            Runtime: 2444 ms, faster than 5.01% of Python3 online submissions for Arranging Coins.

            T: O(N)
            """
            nonlocal n
            r = 1
            comp = 0
            while n:
                if r <= n:
                    comp += 1
                n -= min(r, n)
                r += 1
            return comp


sl = Solution()
print(sl.arrangeCoins(n=5))
print(sl.arrangeCoins(n=8))
print(sl.arrangeCoins(n=1))
