"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, str
"""


class Solution:
    def interpret(self, CMD: str) -> str:
        def pythonic_1line():
            """
            Runtime: 38 ms, faster than 64.54% of Python3 online submissions for Goal Parser Interpretation.

            """
            return CMD.replace("()", "o").replace("(al)", "al")

        def fxr():
            """
            Runtime: 46 ms, faster than 43.03% of Python3 online submissions for Goal Parser Interpretation.

            """
            stk = []
            i = 0
            while i < len(CMD):
                if CMD[i] in "G(":
                    stk.append(CMD[i])
                elif CMD[i] == "a":
                    stk.pop()
                    stk.append("al")
                    i += 1
                elif CMD[i] == ")":
                    if stk[-1] == "(":
                        stk.pop()
                        stk.append("o")
                i += 1
            return "".join(stk)

        return fxr()


sl = Solution()
print(sl.interpret("G()(al)"))
print(sl.interpret("G()()()()(al)"))
print(sl.interpret("(al)G(al)()()G"))
