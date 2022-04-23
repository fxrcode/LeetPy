"""
tag: easy
Lookback:
- observation + logic: this is plusOne, so no need to do school math!
Explore Array & String
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def os():
            """
            Runtime: 32 ms, faster than 92.17% of Python3 online submissions for Plus One.
            """
            n = len(digits)
            for i in range(n - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits
            return [1] + digits

        return os()

        def fxr():
            """
            AC in 1.
            Runtime: 28 ms, faster than 90.46% of Python3 online submissions for Plus One.
            """
            res = []
            # init carry to 1 as plus_one
            carry = 1
            for i in range(len(digits) - 1, -1, -1):
                tmp = digits[i] + carry
                carry = tmp // 10
                left = tmp % 10
                res.append(left)

            if carry == 1:
                res.append(1)

            return reversed(res)


sl = Solution()
print(*sl.plusOne([9, 9, 9]))
print(*sl.plusOne([3, 2, 9]))
