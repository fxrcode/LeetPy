"""
tag: easy
Lookback:
- python3 has hex()
"""


class Solution:
    def toHexspeak(self, num: str) -> str:
        def fxr():
            # Runtime: 50 ms, faster than 37.78% of Python3 online submissions for Hexspeak.
            x16 = hex(int(num))[2:]
            after = x16.replace("0", "O").replace("1", "I").upper()
            print(after)
            valid = {"A", "B", "C", "D", "E", "F", "I", "O"}
            if all(c in valid for c in set(after)):
                return "".join(after)
            return "ERROR"

        return fxr()


sl = Solution()
print(sl.toHexspeak("747823223228"))
