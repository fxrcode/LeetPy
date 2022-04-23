"""
tag: medium, Math, Hash
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def Xyzzy123():
            """
            Runtime: 32 ms, faster than 76.45% of Python3 online submissions for Fraction to Recurring Decimal.

            https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51110/Do-not-use-python-as-cpp-here's-a-short-version-python-code/574314
            """
            sign = "-" if numerator * denominator < 0 else ""
            nmr, dnm = abs(numerator), abs(denominator)
            q, r = divmod(nmr, dnm)  # divmod return tuple(quotient, remainder)
            res = [sign + str(q), "."]
            rs = {}
            while r > 0 and r not in rs:
                rs[r] = len(res)
                q, r = divmod(r * 10, dnm)
                res.append(str(q))

            if r in rs:
                idx = rs[r]
                res.insert(idx, "(")
                res.append(")")
            return "".join(res).rstrip(".")

        return Xyzzy123()

        def fxr():
            d, m = divmod(numerator, denominator)
            res = [d, "."]
            seen = set([m])
            isfrac = False

            frac = []
            while True:
                d, m = divmod(m * 10, denominator)
                frac.append(d)
                if m in seen:
                    isfrac = True
                    break
                if m == 0:
                    break
            if isfrac:
                return [res + ["("] + frac + [")"]]
            return [res + frac]

        return fxr()


sl = Solution()
# print(sl.fractionToDecimal(numerator=1, denominator=2))
# print(sl.fractionToDecimal(numerator=2, denominator=1))
# print(sl.fractionToDecimal(numerator=4, denominator=9))
print(sl.fractionToDecimal(numerator=4, denominator=333))
