"""
tag: easy
Lookback:
* string is immutable, so I convert it to list.
XXX: TypeError: 'str' object does not support item assignment
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def fxr():
            """
            Runtime: 52 ms, faster than 42.59% of Python3 online submissions for Reverse String II.

            """
            ss = list(s)
            for i in range(0, len(ss), 2 * k):
                ss[i : i + k] = ss[i : i + k][::-1]
            return "".join(ss)

        return fxr()


sl = Solution()
print(sl.reverseStr(s="abcdefg", k=2))
print(sl.reverseStr(s="abcd", k=2))
print(sl.reverseStr(s="abcd", k=10))
