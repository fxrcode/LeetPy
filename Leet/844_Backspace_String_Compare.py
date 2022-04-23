"""
FB tag (easy)
[] REDO
"""
from itertools import zip_longest


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def os():
            """
            Runtime: 32 ms, faster than 65.78% of Python3 online submissions for Backspace String Compare.

            clean logic
            """

            def F(s):
                skip = 0
                for x in reversed(s):
                    if x == "#":
                        skip += 1
                    elif skip:
                        skip -= 1
                    else:
                        yield x

            # print(list(F(s)))
            # print(list(F(t)))

            return all(x == y for x, y in zip_longest(F(s), F(t)))

        return os()

        def fxr():
            """
            Runtime: 53 ms, faster than 8.06% of Python3 online submissions for Backspace String Compare.

            T: O(N)
            M: O(N)
            """

            def helper(s):
                stk = []
                for c in s:
                    if c != "#":
                        stk.append(c)
                    else:
                        if stk:
                            stk.pop()
                print("".join(stk))
                return stk

            return helper(s) == helper(t)

        return fxr()


sl = Solution()
print(sl.backspaceCompare(s="ab#c", t="ad#c"))
print(sl.backspaceCompare(s="ab##", t="c#d#"))
print(sl.backspaceCompare(s="a#c", t="b"))

print(sl.backspaceCompare("bxj##tw", "bxj###tw"))

