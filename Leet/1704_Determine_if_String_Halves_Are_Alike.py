"""
Tag: Easy, Hash, str
Lookback:
- practice to fast in python API
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def dbabichev():
            # Runtime: 59 ms, faster than 29.72% of Python3 online submissions for Determine if String Halves Are Alike.
            nonlocal s
            s, n, VOWS = s.lower(), len(s), set("aeiou")
            return sum(c in VOWS for c in s[: n // 2]) == sum(
                c in VOWS for c in s[n // 2 :]
            )

        def fxr():
            # Runtime: 43 ms, faster than 67.82% of Python3 online submissions for Determine if String Halves Are Alike.

            VOWELS = set("aeiouAEIOU")

            def vows(ss):
                cnt = 0
                for c in ss:
                    if c in VOWELS:
                        cnt += 1
                return cnt

            return vows(s[: len(s) // 2]) == vows(s[len(s) // 2 :])
