"""
tag: medium, stack
Lookback:
- evaluation type, use lambda inside dict is pythonic

Similar:
- 1628: stack + dfs
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/
Leetcode Explore-Queue-Stack: Stack
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
"""

import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def rec_YogurtIvan():
            operations_map = {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv,
            }

            def rec(tokens: List[str]) -> int:
                val = tokens.pop()
                if val not in operations_map:
                    return int(val)
                right = rec(tokens)
                left = rec(tokens)
                return int(operations_map[val](left, right))

            return rec(tokens)

        return rec_YogurtIvan()

        def os_stk():
            """
            Runtime: 66 ms, faster than 96.07% of Python3 online submissions for Evaluate Reverse Polish Notation.

            O(N)TS
            """
            stack, ops = [], {
                "+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv,
            }
            for t in tokens:
                if str.isnumeric(t) or (len(t) > 1 and t[0] == "-"):
                    stack += (int(t),)
                else:
                    fn, y, x = ops[t], stack.pop(), stack.pop()
                    stack += (int(fn(x, y)),)

            return stack.pop()

        def fxr():
            """
            Your runtime beats 84.73 % of python3 submissions.

            almost AC in 1st try. Gotcha in 3rd test case for 1/-132. Python 3 round to -1 in eval(equation)

            """
            stk = []
            for t in tokens:
                if t not in "+-*/":
                    stk.append(int(t))
                else:
                    sec = stk.pop()
                    fir = stk.pop()
                    if t == "+":
                        stk.append(fir + sec)
                    elif t == "-":
                        stk.append(fir - sec)
                    elif t == "*":
                        stk.append(fir * sec)
                    # https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/47429/6uff08-132uff09-0-or-1
                    # for div, python default doesn't truncate, so 1/-132 = -1, rather 0!
                    # In [6]: (6/-132)
                    # Out[6]: -0.045454545454545456
                    else:
                        stk.append(int(fir / sec))

            return stk[-1]


sl = Solution()
# tokens = ["2", "1", "+", "3", "*"]
# tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
assert sl.evalRPN(tokens) == 22
