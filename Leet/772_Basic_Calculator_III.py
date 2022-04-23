"""
✅ GOOD recursion (post-order)

tag: recursion, stack
Lookback:
* careful how `)` is handled: not only break recursion, but also do eval!
* must be postorder! so we can get inner result before we eval cur substr: '3*(...)'  -6

Similar:
- 1597. Build Binary Expression Tree From Infix Expression

"""
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        def labuladong():
            """
            Runtime: 47 ms, faster than 76.54% of Python3 online submissions for Basic Calculator III.

            XXX: much to learn!
            * use of stack to store val to eval later
            * post-order traversal, so (...) has been eval'ed before push to stack
            * need to process when +-*/ and () and last pos!

            """

            def rec(q):
                num, sign = 0, "+"
                stk = []
                while q:
                    c = q.popleft()
                    if c.isdigit():
                        num = num * 10 + int(c)
                    if c == "(":
                        num = rec(q)
                    if c in "+-*/)" or not q:
                        #! careful we catch ')' to eval (...), ow  (4-5/2) will only be sum([4,-5]) => -1, /2 is ignored
                        if sign == "+":
                            stk.append(num)
                        elif sign == "-":
                            stk.append(-num)
                        elif sign == "*":
                            stk.append(stk.pop() * num)
                        elif sign == "/":
                            stk.append(int(stk.pop() / float(num)))
                        sign = c
                        num = 0
                    if c == ")":
                        break

                return sum(stk)

            return rec(deque(s))

        return labuladong()


sl = Solution()
# print(sl.calculate('1+1'))
# print(sl.calculate("4-5/2"))
print(sl.calculate("3*(4-15/2)-6"))
# print(sl.calculate(s="4*(6+5*2)/3+(6/2+8)"))
