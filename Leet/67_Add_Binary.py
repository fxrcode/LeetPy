"""
tag: easy, bit
Lookback:
- `xor` is non-carry addition, `&<<1` get carry
Daily Challenge (Jan 10)
Completion Streak: 57 Days
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def os():
            """
            Runtime: 34 ms, faster than 87.46% of Python3 online submissions for Add Binary.

            TODO: learn bit manipulation
            """
            x, y = int(a, 2), int(b, 2)
            while y:
                ans = x ^ y
                carry = (x & y) << 1
                x, y = ans, carry
            return bin(x)[2:]

        def fxr():
            """
            Runtime: 47 ms, faster than 20.77% of Python3 online submissions for Add Binary.

            T:O(N)
            """
            c = 0
            ans = []
            aa = a[::-1]
            bb = b[::-1]
            if len(aa) > len(bb):
                aa, bb = bb, aa
            for i in range(len(aa)):
                x, y = int(aa[i]), int(bb[i])
                c, v = divmod(x + y + c, 2)
                ans.append(v)
            for j in range(i + 1, len(bb)):
                x, y = int(bb[j]), 0
                c, v = divmod(x + y + c, 2)
                ans.append(v)
            if c:
                ans.append(c)
            return "".join(str(v) for v in ans)[::-1]

        return fxr()


sl = Solution()
print(sl.addBinary("11", "1"))
print(sl.addBinary(a="1010", b="1011"))
