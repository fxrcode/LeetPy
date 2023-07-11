"""
✅ GOOD Greedy (Parenthesis)
tag: medium, greedy, logic
Lookback:
- deep understand of valid parenthesis trick, and why forward & backward
    - Left-to-right check ensures that we do not have orphan `)` parentheses.
    - Right-to-left checks for orphan `(` parentheses.
similar:
- 301
- 856
- 921
- 1249
- 2116
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        def fxr_2116():
            """
            Runtime: 36 ms, faster than 74.20% of Python3 online submissions for Valid Parenthesis String.

            XXX: almost same as in 2116!
            """

            def validate(s, op):
                bal, wild = 0, 0
                for p in s:
                    if p in "()":
                        bal += 1 if p == op else -1
                    else:
                        wild += 1
                    if wild + bal < 0:
                        return False
                return bal <= wild

            # only forward failed for "**(("
            return validate(s, "(") and validate(s[::-1], ")")

        def constant_variation_2stk():
            """
            https://leetcode-cn.com/problems/valid-parenthesis-string/solution/wei-rao-li-lun-ken-ding-shi-zhan-ya-by-w-op09/
            XXX: pairwise handling '(' & '*'
            """
            star, left = [], []
            for i, c in enumerate(s):
                if c == "(":
                    left.append(i)
                elif c == "*":
                    star.append(i)
                else:  # ')'
                    if left:
                        left.pop()
                    elif star:
                        star.pop()
                    else:
                        return False
            while left:
                posL = left[-1]
                if not star:
                    return False
                posS = star[-1]
                if posS > posL:
                    star.pop()
                    left.pop()
                else:
                    return False
            return True

        def hiepit_graph():
            cmin, cmax = 0, 0  # open paren  in range [cmin,cmax]
            for c in s:
                if c == "(":
                    cmax += 1
                    cmin += 1
                elif c == ")":
                    cmax -= 1
                    cmin -= 1
                elif c == "*":
                    cmax += 1  # if `*` become `(` then openCount++
                    cmin -= 1  # if `*` become `)` then openCount--
                    # if `*` become `` then nothing happens
                    # So openCount will be in new range [cmin-1, cmax+1]
                if cmax < 0:
                    # Currently, don't have enough open parentheses to match close parentheses-> Invalid
                    # For example: ())(
                    return False
                # It's invalid if open parentheses count < 0 that's why cmin can't be negative
                cmin = max(cmin, 0)
            # Return true if can find `openCount == 0` in range [cmin, cmax]
            return cmin == 0


sl = Solution()
print(
    sl.checkValidString("**((")
)  # proof: forward is not enough, since forward is for orphan ')'
print(
    sl.checkValidString("))**")
)  # example: backward is not enough, since backward is for orphan '('
print(sl.checkValidString("()"))
print(sl.checkValidString("(*)"))
print(sl.checkValidString("(*))"))
