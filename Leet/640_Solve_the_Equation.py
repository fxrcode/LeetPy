"""
tag: medium, str, skills
Lookback:
- practice more on parse str, so as to have neat code as hiepit/ye15/lee215/rock
"""


from collections import Counter


class Solution:
    def solveEquation(self, equation: str) -> str:
        def ye15():
            """
            Runtime: 37 ms, faster than 66.05% of Python3 online submissions for Solve the Equation.

            XXX: Best & Neat!
            [ ] REDO
            """
            lhs, rhs = equation.split("=")

            def fn(s):
                """Parse s into coefficients."""
                ii = x = y = 0
                for i in range(len(s) + 1):
                    if i == len(s) or s[i] in "+-":
                        if ii < i:
                            y += int(s[ii:i])
                        ii = i
                    elif s[i] == "x":
                        if ii == i or s[ii:i] in "+-":
                            x += int(s[ii:i] + "1")
                        else:
                            x += int(s[ii:i])
                        ii = i + 1
                return x, y

            (lx, ly), (rx, ry) = fn(lhs), fn(rhs)
            if lx == rx:
                if ly != ry:
                    return "No solution"
                else:
                    return "Infinite solutions"
            return f"x={(ry-ly)//(lx-rx)}"

        return ye15()

        def hiepit():
            """
            Runtime: 28 ms, faster than 93.95% of Python3 online submissions for Solve the Equation.

            """

            def evaluate(expr):
                print(expr)
                tokens = expr.replace("+", "#+").replace("-", "#-").split("#")  # For example: "x+5-3+x" is replaced to "x#+5#-3#+x" then split by "#"
                print(tokens)
                res = [0] * 2
                for token in tokens:
                    if not token:
                        continue
                    if token == "x" or token == "+x":
                        res[0] += 1
                    elif token == "-x":
                        res[0] -= 1
                    elif "x" in token:
                        res[0] += int(token[: token.index("x")])  # For example: "3x" or "-5x" or "+6x"
                    else:
                        res[1] += int(token)
                return res

            parts = equation.split("=")
            leftRes = evaluate(parts[0])
            rightRes = evaluate(parts[1])
            a = leftRes[0] - rightRes[0]
            b = rightRes[1] - leftRes[1]
            if a == 0 and b == 0:
                return "Infinite solutions"
            if a == 0:
                return "No solution"
            return f"x={b // a}"

        return hiepit()

        def fxr():
            """
            Runtime: 39 ms, faster than 59.26% of Python3 online submissions for Solve the Equation.

            So slow in basic parsing/if-else-loop
            """

            def parse(s: str):
                cnt = Counter()
                num = coeff = ""
                is_x = False
                for i in range(len(s) - 1, -1, -1):
                    if s[i] in "+-":
                        sign = 1
                        if s[i] == "-":
                            sign = -1
                        if is_x:
                            cnt["x"] += sign * (int(coeff) if coeff else 1)
                        else:
                            cnt["const"] += sign * int(num)
                        coeff = num = ""
                        is_x = False
                    elif s[i] == "x":
                        is_x = True
                    else:
                        if is_x:
                            coeff = s[i] + coeff
                        else:
                            num = s[i] + num
                return cnt

            lhs, rhs = equation.split("=")
            if lhs[0] not in "+-":
                lhs = "+" + lhs
            if rhs[0] not in "+-":
                rhs = "+" + rhs
            cl, cr = parse(lhs), parse(rhs)
            # print(cl, cr)

            cl["x"] -= cr["x"]
            cr["const"] -= cl["const"]
            if cl["x"] == 0:
                if cr["const"] != 0:
                    return "No solution"
                return "Infinite solutions"
            ans = cr["const"] // cl["x"]
            return f"x={ans}"

        return fxr()


sl = Solution()
for eq in ["x+5-13+13x=6+15x-2"]:  # , "x=x", "2x=x", "1-10x+9=-10-20x+30", "x-10=x+20"]:
    print(sl.solveEquation(eq))
