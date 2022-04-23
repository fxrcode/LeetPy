"""
tag: easy, math
Lookback:
- Python % is like distance on clock, always in range [0, MOD)
"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        def ye15():
            """
            Runtime: 37 ms, faster than 74.97% of Python3 online submissions for Minimum Time to Type Word Using Special Typewriter.

            """
            ans = len(word)
            prev = "a"
            for c in word:
                val = (ord(c) - ord(prev)) % 26
                ans += min(val, 26 - val)
                prev = c
            return ans

        return ye15()

        def fxr():
            """
            Runtime: 49 ms, faster than 43.21% of Python3 online submissions for Minimum Time to Type Word Using Special Typewriter.

            """

            def o(c):
                return ord(c) - ord("a")

            a = "a"
            cost = 0
            for c in word:
                d1 = abs(o(c) - o(a))
                d2 = 0
                if o(c) > o(a):
                    d2 = abs(o(c) - (o("z") + 1 + o(a)))
                else:
                    d2 = abs(o(a) - (o("z") + 1 + o(c)))
                cost += min(d1, d2) + 1
                a = c
            return cost


sl = Solution()
print(sl.minTimeToType("abc"))
print(sl.minTimeToType("bza"))
