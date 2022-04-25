"""
✅ GOOD Set (<= means issubset: Set Comparison Operators)
Tag: Easy, Hash
Lookback:
- for/else: The else clause executes after the loop completes normally.
"""
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def lee215():
            """
            Runtime: 38 ms, faster than 61.50% of Python3 online submissions for Keyboard Row.

            """
            one, two, three = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
            res = []
            for w in words:
                ws = set(w.lower())
                #! https://docs.python.org/3/library/stdtypes.html#frozenset.issubset
                if ws <= one or ws <= two or ws <= three:
                    res.append(w)
            return res

        return lee215()

        def fxr():
            one, two, three = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
            res = []
            for w in words:
                for s in (one, two, three):
                    if w[0].lower() in s:
                        break
                if all(c.lower() in s for c in w[1:]):
                    res.append(w)
            return res


sl = Solution()
print(sl.findWords(words=["Hello", "Alaska", "Dad", "Peace"]))
print(sl.findWords(["Aasdfghjkl", "Qwertyuiop", "zZxcvbnm"]))
