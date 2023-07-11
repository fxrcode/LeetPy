"""
tag: Medium, hash, str
Lookback:
- Python should be neat in str processing
"""

from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        def dbabhichev():
            """
            Runtime: 1299 ms, faster than 54.22% of Python3 online submissions for Evaluate the Bracket Pairs of a String.

            XXX: neat!
            """
            d = {k: v for k, v in knowledge}
            t = s.split("(")
            ans = t[0]
            for i in range(1, len(t)):
                a, b = t[i].split(")")
                ans += d.get(a, "?") + b
            return ans

        return dbabhichev()

        def fxr():
            # Runtime: 1423 ms, faster than 41.94% of Python3 online submissions for Evaluate the Bracket Pairs of a String.
            l, r = 0, 0
            res = []
            d = {k: v for k, v in knowledge}
            while l < len(s):
                if s[l] == "(":
                    l += 1
                    r = l
                    while r < len(s) and s[r] != ")":
                        r += 1
                    # r oor or s[r] != ')'
                    if r < len(s) and s[r] == ")":
                        res.append(d.get(s[l:r], "?"))
                        r += 1
                    l = r
                else:
                    res.append(s[l])
                    l += 1
            return "".join(res)

        return fxr()


sl = Solution()
print(
    sl.evaluate(s="(name)is(age)yearsold", knowledge=[["name", "bob"], ["age", "two"]])
)  # == "bobistwoyearsold"
print(sl.evaluate(s="hi(name)", knowledge=[["a", "b"]]))
print(sl.evaluate(s="(a)(a)(a)aaa", knowledge=[["a", "yes"]]))
