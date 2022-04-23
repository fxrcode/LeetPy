"""
tag: easy
Lookback:
- Lee215: crystal clear logic + neat impl
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        def lee215():
            # add every char unless 1st '(' or last ')'
            res, opened = [], 0
            for c in s:
                if c == "(" and opened > 0:
                    res.append(c)
                if c == ")" and opened > 1:
                    res.append(c)
                opened += 1 if c == "(" else -1
            return "".join(res)

        return lee215()

        def fxr():
            # Runtime: 32 ms, faster than 98.04% of Python3 online submissions for Remove Outermost Parentheses.
            res = []
            count = 0
            for c in s:
                if c == "(":
                    if count != 0:
                        res.append(c)
                    count += 1
                else:
                    if count != 1:
                        res.append(c)
                    count -= 1
            return "".join(res)

        return fxr()


sl = Solution()
print(sl.removeOuterParentheses(s="(()())(())"))
print(sl.removeOuterParentheses(s="(()())(())(()(()))"))
print(sl.removeOuterParentheses(s="()()"))
