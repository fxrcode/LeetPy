"""
✅ GOOD Greedy (Parenthesis)
tag: amazon, medium
Lookback:
- deep understand of valid parenthesis trick, and why forward & backward
- A useful trick (when doing any parentheses validation) is to greedily check balance left-to-right, and then right-to-left.
    * Left-to-right check ensures that we do not have orphan ')' parentheses.
    * Right-to-left checks for orphan '(' parentheses.
Similar:
- 921. Huifeng Guan (snippets)
- 678. Valid Parenthesis String
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        def huangshan01_stk():
            """
            Runtime: 164 ms, faster than 98.90% of Python3 online submissions for Check if a Parentheses String Can Be Valid.

            XXX: stack is still the easiest algs for paren validate
            Identical code as in 678!
            """
            if len(s) % 2 == 1:
                return False
            locked_open, unlocked = [], []
            for i, c in enumerate(s):
                if locked[i] == "0":
                    unlocked.append(i)
                else:
                    if c == "(":
                        locked_open.append(i)
                    else:
                        if locked_open:
                            locked_open.pop()
                        elif unlocked:
                            unlocked.pop()
                        else:
                            return False
            while locked_open:
                if unlocked and unlocked[-1] > locked_open[-1]:
                    unlocked.pop()
                    locked_open.pop()
                else:
                    return False
            return True

        def votrubac_greedy():
            """
            Runtime: 287 ms, faster than 67.30% of Python3 online submissions for Check if a Parentheses String Can Be Valid.

            """

            def validate(s, locked, op) -> bool:
                bal, wild = 0, 0
                for i, c in enumerate(s):
                    if locked[i] == "1":
                        bal += 1 if c == op else -1
                    else:
                        wild += 1
                    if wild + bal < 0:  # if unmatched locked ')' can't be matched w/ wild (left->right)
                        return False
                return bal <= wild  # check if unmatched locked '(' can be matched w/ wild (left->right)

            # left-to-right only will fail for ["))((", "0011"]
            return len(s) % 2 == 0 and validate(s, locked, "(") and validate(s[::-1], locked[::-1], ")")

        return votrubac_greedy()

        def fxr_TLE():
            """
            TLE: 8 / 258 test cases passed.

            """

            def count_bad(s):
                l, r = 0, 0
                for p in s:
                    if p == "(":
                        l += 1
                    else:
                        r += 1
                        if l > 0:
                            l, r = l - 1, r - 1
                return l, r

            def dfs(s, l, r, i):
                # print(s, l, r, i)
                if (0, 0) == count_bad(s):
                    return True
                if i >= len(locked):
                    return False
                if locked[i] == "1":
                    return dfs(s, l, r, i + 1)

                if dfs(s, l, r, i + 1):
                    return True
                if s[i] == "(":
                    if l and dfs(s[:i] + ")" + s[i + 1 :], l - 1, r, i + 1):
                        return True
                else:
                    if r and dfs(s[:i] + "(" + s[i + 1 :], l, r - 1, i + 1):
                        return True
                return False

            l, r = count_bad(s)
            return dfs(s, l, r, 0)

        return fxr_TLE()


sl = Solution()
print(sl.canBeValid(s="))((", locked="0011"))
# print(sl.canBeValid(s="))()))", locked="010100"))
# print(sl.canBeValid(s="()()", locked="0000"))
# print(sl.canBeValid(s=")(", locked="00"))
# print(sl.canBeValid(s=")", locked="0"))
# print(sl.canBeValid("))))(())((()))))((()((((((())())((()))((((())()()))(()", "101100101111110000000101000101001010110001110000000101"))
