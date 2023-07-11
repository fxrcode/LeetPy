"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
https://leetcode.com/explore/learn/card/binary-search/137/conclusion/982/
Leetcode Explore: Binary Search - Conclusion

https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2375/
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def stefanPochmann(x, n):
            """[summary]
            Your runtime beats 96.46 % of python3 submissions.

            https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
            """
            if n == 0:
                return 1
            if n < 0:
                return 1 / stefanPochmann(x, -n)
            if n % 2:
                return x * stefanPochmann(x, n - 1)
            return stefanPochmann(x * x, n // 2)

    def myPow_fxr(self, x: float, n: int) -> float:
        """[summary]
        RecursionError: maximum recursion depth exceeded in comparison
        0.00001
        2147483647
        """

        def recur(x, n) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x
            return x * recur(x, n - 1)

        if n < 0:
            return 1 / recur(x, -n)
        return recur(x, n)


sl = Solution()
print(sl.myPow(2.0000, 10))
print(sl.myPow(2.100, 3))
print(sl.myPow(2.0000, -2))
