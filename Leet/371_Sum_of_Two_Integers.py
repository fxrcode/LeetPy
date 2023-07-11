"""
✅ GOOD bit manipulation

https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions

XXX: Extremely popular Facebook problem designed to check your knowledge of bitwise operators
XOR, &, ~

XXX: Interview Tip for Bit Manipulation Problems: Use XOR for input data.
NOTE: XOR(a,b) === Sum(a,b) without carry!
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Runtime: 32 ms, faster than 59.64% of Python3 online submissions for Sum of Two Integers.

        REF: OS excellent explain.
        """
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of 2 positive integers, XOR (sum without carry), (x^y)<<1 is carry
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of 2 positive integers, XOR (diff without borrow), ((~x)&y)<<1 is borrow
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        return sign * x


sl = Solution()
print(sl.getSum(-14, 16))
