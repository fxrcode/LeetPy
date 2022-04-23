"""
✅ GOOD Stack (Mono stack)
💡insight
tag: medium, greedy, stack
Lookback:
- mono stack problem is to find property of problem

Similar:
316
1081
1673
"""
from collections import deque


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def os_stk():
            """
            Runtime: 54 ms, faster than 58.11% of Python3 online submissions for Remove K Digits.
            OS solution is neat! use mono stack!

            T: O(N)
            """
            stk = []
            nonlocal k
            for n in num:
                while k and stk and stk[-1] > n:
                    stk.pop()
                    k -= 1
                stk.append(n)

            # trunk the remaining K digits at the end
            finalStk = stk[:-k] if k else stk

            # if empty str after lstrip, then use '' or '0' => '0'! nice pythonic
            return "".join(finalStk).lstrip("0") or "0"


sl = Solution()
print(sl.removeKdigits(num="1432219", k=3))
print(sl.removeKdigits(num="10200", k=1))
print(sl.removeKdigits(num="10", k=2))
print(sl.removeKdigits(num="9", k=1))
print(sl.removeKdigits(num="112", k=1))
