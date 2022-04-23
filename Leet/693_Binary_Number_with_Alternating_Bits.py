"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, math
Lookback:
- no need to memoize bit tricks, you should Polya 4Q to solve it by analysis. 
    * Just like 1192. Critical Connections in a Network. You don't need to invent Tarjan SCC. You should be able to solve it by analysis!
    * Leetcode is about problem solving skill, rather memoization.
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        def san89kalp(n):
            """
            Runtime: 37 ms, faster than 64.92% of Python3 online submissions for Binary Number with Alternating Bits.

            https://leetcode.com/problems/binary-number-with-alternating-bits/discuss/113933/Java-super-simple-explanation-with-inline-example
            XXX: Smart!
            """
            n ^= n >> 1
            return (n & (n + 1)) == 0

        def os():
            """
            Runtime: 30 ms, faster than 86.26% of Python3 online submissions for Binary Number with Alternating Bits.

            T:O(1)
            """
            x, cur = divmod(n, 2)
            while x:
                if cur == x & 1:
                    return False
                x, cur = divmod(x, 2)
            return True

        # return os()
        return san89kalp(n)


sl = Solution()
for n in [1, 5, 7, 11]:
    print(sl.hasAlternatingBits(n))
