'''
Daily Challenge (Nov 19)
01:54:50 left
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def os_bitcount():
            # Runtime: 24 ms, faster than 95.74% of Python3 online submissions for Hamming Distance.
            return bin(x ^ y).count('1')

        def fxr():
            """
            Runtime: 24 ms, faster than 95.74% of Python3 online submissions for Hamming Distance.

            """
            nonlocal x, y
            ans = 0
            while x or y:
                ans += (x & 1) ^ (y & 1)
                x >>= 1
                y >>= 1
            return ans
