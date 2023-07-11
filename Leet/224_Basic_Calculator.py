"""
C3.ai phone
✅ GOOD Recursion
"""
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        """
        Runtime: 201 ms, faster than 10.09% of Python3 online submissions for Basic Calculator.

        """

        def rec(q):
            stk, num, sign = [], 0, "+"
            while q:
                c = q.popleft()
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == "(":
                    num = rec(q)
                if c in "+-)" or len(q) == 0:
                    # if (not c.isdigit() and c != ' ') or len(q) == 0:
                    if sign == "+":
                        stk.append(num)
                    elif sign == "-":
                        stk.append(-num)
                    sign = c
                    num = 0
                if c == ")":
                    break
            return sum(stk)

        return rec(deque(s))


sl = Solution()
# print(sl.calculate(s='1 +  1'))
# print(sl.calculate(s='3-(2+(9-4))'))
print(sl.calculate(s="1-(9-4)"))
