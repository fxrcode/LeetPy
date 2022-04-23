'''
Amazon Top50
tag: Medium

Lookback:
* int to roman starts from left->right, high->low
* pre-compute the components mapping
* loop to use biggest val in mp that fits into num, find how many of the symbol.
* loop until num = 0
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Runtime: 60 ms, faster than 49.80% of Python3 online submissions for Integer to Roman.

        https://leetcode.com/problems/integer-to-roman/solution/
        """
        mp = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        rom = []
        x = num
        for d, r in mp.items():
            if x == 0:
                break
            count, x = divmod(x, d)
            rom.append(r * count)
        return ''.join(rom)


sl = Solution()
print(sl.intToRoman(3))
print(sl.intToRoman(671))
print(sl.intToRoman(58))
print(sl.intToRoman(1994))