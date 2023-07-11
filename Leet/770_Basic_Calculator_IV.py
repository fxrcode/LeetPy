"""

💡Smart use of Counter to interpretate var mapping, pure var, and int
Smart use of eval
Smart use re
FINAL version of basic calculator: SUPER HARD

Fast.co Karat phone...
"""

import re
from collections import Counter
from typing import List


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        """
        https://leetcode.com/problems/basic-calculator-iv/discuss/113549/Easy-%3A-P
        XXX: StefanPochmann is KING
        """

        class C(Counter):
            def __add__(self, other):
                self.update(other)
                return self

            def __sub__(self, other):
                self.subtract(other)
                return self

            def __mul__(self, other):
                product = C()
                for x in self:
                    for y in other:
                        xy = tuple(sorted(x + y))
                        product[xy] += self[x] * other[y]
                return product

        vals = dict(zip(evalvars, evalints))

        def f(s):
            s = str(vals.get(s, s))
            return C({(s,): 1}) if s.isalpha() else C({(): int(s)})

        parsed = re.sub("(\w+)", r'f("\1")', expression)
        c = eval(parsed)

        ans = []
        sorted_c = sorted(c, key=lambda x: (-len(x), x))
        for x in sorted_c:
            if c[x]:
                v = "*".join((str(c[x]),) + x)
                ans.append(v)
        return ans

        # return ['*'.join((str(c[x]),) + x)
        #         for x in sorted(c, key=lambda x: (-len(x), x))
        #         if c[x]]


sl = Solution()
print(sl.basicCalculatorIV(expression="e * a * 42 + 5", evalvars=["x"], evalints=[1]))
