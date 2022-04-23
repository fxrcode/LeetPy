"""
💡 Insight (Math)
Tag: Easy, Math
Lookback:
- 1st O(N^0.25)
- from logic, we just need to test if n is PRIME^2. 
- check PRIME in O(N^0.5)
Similar:
- 1979
"""

from math import isqrt


class Solution:
    def isThree(self, n: int) -> bool:
        def ye15():
            """
            Runtime: 29 ms, faster than 96.47% of Python3 online submissions for Three Divisors.

            https://leetcode.com/problems/three-divisors/discuss/1375468/Python3-1-line
            T: O(N^0.25)
            """
            if n < 4:
                return False
            x = isqrt(n)
            # check if n is square number
            if x * x != n:
                return False
            # check if n is square of PRIME, so check if x is PRIME
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return True

        return ye15()

        def fxr():
            # Runtime: 37 ms, faster than 82.95% of Python3 online submissions for Three Divisors.
            if n < 4:
                return False
            cnt = 2
            for d in range(2, isqrt(n) + 1):
                if n % d == 0:
                    cnt += 1
                    if d * d != n:
                        cnt += 1
                    if cnt > 3:
                        break
            return cnt == 3


sl = Solution()
print(sl.isThree(n=14))
