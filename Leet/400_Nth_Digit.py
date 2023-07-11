"""
✅ GOOD Math
FB tag (medium)
[ ] REDO
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        def agave():
            """
            Runtime: 39 ms, faster than 24.43% of Python3 online submissions for Nth Digit.

            https://leetcode.com/problems/nth-digit/discuss/88417/4-liner-in-Python-and-complexity-analysis

            T: O(logN)
            """
            bit = 1
            cnt = 9
            start = 1
            nonlocal n
            while n - cnt * bit > 0:
                n -= cnt * bit
                cnt *= 10
                bit += 1
                start *= 10

            print(n, cnt, bit, start)
            d, m = divmod(n - 1, bit)
            return str(start + d)[m]

        return agave()


sl = Solution()
print(sl.findNthDigit(n=3))
print(sl.findNthDigit(n=11))
print(sl.findNthDigit(n=22))
