"""
https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75
"""
from typing import Optional


class Solution:
    def reverseBits(self, n: int) -> int:
        def fxr(n):
            """
            Runtime: 32 ms, faster than 77.68% of Python3 online submissions for Reverse Bits.

            https://stackoverflow.com/a/10411108/3984911

            '{0:08b}'.format(6)
            {} places a variable into a string
            0 takes the variable at argument position 0
            : adds formatting options for this variable (otherwise it would represent decimal 6)
            08 formats the number to eight digits zero-padded on the left
            b converts the number to its binary representation

            """
            oribin = '{0:032b}'.format(n)
            reversebin = oribin[::-1]
            return int(reversebin, 2)

        def os_bit_reverse(n):
            """
            Runtime: 20 ms, faster than 99.50% of Python3 online submissions for Reverse Bits.

            """
            print(n)
            print('{0:032b}'.format(n))
            ret, power = 0, 31
            while n:
                ret += (n & 1) << power
                n = n >> 1
                power -= 1
            print('{0:032b'.format(n))
            return ret
        # return os_bit_reverse(n)
        return fxr(n)


sl = Solution()
print(sl.reverseBits(n=43261596))
