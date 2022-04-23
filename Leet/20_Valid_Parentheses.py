"""
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1361/
Explore-queue-stack: Stack LIFO
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        def fxr_stk():
            """
            Runtime: 38 ms, faster than 69.16% of Python3 online submissions for Valid Parentheses.

            XXX: always check if len(s) is odd for parenthesis problems
            """
            if len(s) % 2 == 1:
                return False
            stk = []
            pas = {")": "(", "]": "[", "}": "{"}
            for c in s:
                if c not in pas:
                    stk.append(c)
                else:
                    if not stk or pas[c] != stk.pop():
                        return False
            return not stk

        return fxr_stk()

        def labuladong():
            """[summary]
            Runtime: 24 ms, faster than 96.52% of Python3 online submissions for Valid Parentheses.
            AC in 1st try. It's simple Labuladong example.

            XXX: or you can init stk = ['#'], a dummy node generalize the stack poping.
            https://leetcode.com/problems/valid-parentheses/discuss/9203/Simple-Python-solution-with-stack
            """
            stk = []
            close2open = {}
            for c, o in zip(")]}", "([{"):
                close2open[c] = o
            for i in s:
                # if close, get top to validate
                if i in close2open.keys():
                    if not stk:
                        return False
                    t = stk.pop()
                    if close2open[i] != t:
                        return False

                # ow, push open
                else:
                    stk.append(i)
            return not stk


sl = Solution()
ss = ["()", "()[]{}", "](", "(}"]
for s in ss:
    print(sl.isValid(s))
