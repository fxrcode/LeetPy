"""
tag: medium, Facebook
Lookback:
- like rock impl, no need to pre-build c2o dict, simply loop `order` as order. And use `counter.pop(key)` to remove k/v pair.
"""
from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        def rock():
            """
            Runtime: 43 ms, faster than 54.37% of Python3 online submissions for Custom Sort String.

            """
            ans, cnt = [], Counter(s)
            for c in order:
                if cnt[c]:
                    ans.extend([c] * cnt.pop(c))
            for c, f in cnt.items():
                ans.extend(c * f)
            return "".join(ans)

        return rock()

        def fxr():
            """
            Runtime: 35 ms, faster than 75.62% of Python3 online submissions for Custom Sort String.

            """
            c2o = {c: o for o, c in enumerate(order)}
            freq = Counter(s)

            res = []
            for c in c2o.keys():
                if c in freq:
                    res.extend([c] * freq[c])
            for ow in freq.keys() - c2o.keys():
                res.extend([ow] * freq[ow])
            return "".join(res)

        return fxr()


sl = Solution()
print(sl.customSortString(order="cba", s="abcd"))
print(sl.customSortString(order="cbafg", s="abcd"))
