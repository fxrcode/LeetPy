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

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def os_stk():
            """
            Runtime: 108 ms, faster than 39.11% of Python3 online submissions for Evaluate Reverse Polish Notation.

            """
            ops = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: int(a / b),
            }
            stk = []
            for tok in tokens:
                if tok in ops:
                    sec = stk.pop()
                    fir = stk.pop()
                    op = ops[tok]
                    stk.append(op(fir, sec))
                else:
                    stk.append(int(tok))
            return stk[-1]

        return os_stk()

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
