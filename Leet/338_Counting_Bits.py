"""
https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75

tag: easy, math
Lookback
- Leetcode is about problem solving skill.
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        def os_dp_LSetB():
            """
            Runtime: 72 ms, faster than 97.12% of Python3 online submissions for Counting Bits.
            #! transition func: P(x) = P(x & (x-1)) + 1, same bit trick as in popcount

            T: O(N)
            """
            ans = [0] * (n + 1)
            for x in range(1, n + 1):
                ans[x] = ans[x & (x - 1)] + 1
            return ans

        def os_dp_LSB():
            """
            Runtime: 68 ms, faster than 99.68% of Python3 online submissions for Counting Bits.

            T:O(N)
            """
            #! transition func: P(x) = P(x/2)+1.
            ans = [0] * (n + 1)
            for x in range(n + 1):
                ans[x] = ans[x >> 1] + (x & 1)
            return ans

        def os_dp_MSB():
            ans = [0] * (n + 1)
            x = 0
            b = 1

            # XXX: how to translate formula into code? var? boundary?
            #! transition func: P(x+b) = P(x)+1. b=(2^m) > x
            # [0, b) is calculated
            while b <= n:
                # generate [b, 2b) or [b, n) from [0, b)
                while x < b and x + b <= n:
                    ans[x + b] = ans[x] + 1
                    x += 1
                x = 0  # reset x
                b <<= 1  # b = 2b
            return ans

        def fxr():
            def ones(x):
                cnt = 0
                while x:
                    cnt += 1
                    x &= x - 1
                return cnt

            ans = []
            for i in range(n + 1):
                ans.append(ones(i))
            return ans

        # return fxr()
        # return os_dp_MSB()
        return os_dp_LSB()
        # return os_dp_LSetB()


sl = Solution()
print(sl.countBits(2))
