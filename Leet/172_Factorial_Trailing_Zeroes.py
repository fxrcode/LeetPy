"""
https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        def os_logN():
            """
            Runtime: 28 ms, faster than 92.94% of Python3 online submissions for Factorial Trailing Zeroes.

            REF: OS, we need to count #5s, since 25 has two 5, so how to get it correctly?
                A: n/5 + n/25.
                therefore: count5 = n/5+n/25+n/125 +... = n/5 + (n/5)/5 + (n/5/5)/5
            """
            ans = 0
            v = n
            while v > 0:
                v //= 5
                ans += v
            return v

        def fxr_brute():
            """
            Runtime: 432 ms, faster than 29.90% of Python3 online submissions for Factorial Trailing Zeroes.

            """
            ans = 0
            if n == 0:
                return ans

            cnt = {5: 0, 10: 0}
            for i in range(1, n+1):
                for div in [10, 5]:
                    while i % div == 0:
                        i = i // div
                        cnt[div] += 1
            ans += cnt[10] + cnt[5]
            return ans

        return fxr_brute()


sl = Solution()
print(sl.trailingZeroes(5))
