'''
WC 279
Feb 5, 2022

Lookback
-
'''

from functools import cache
from itertools import zip_longest
from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        ans = []
        odd = sorted(nums[1::2], reverse=True)
        even = sorted(nums[::2])
        for e, o in zip_longest(even, odd):
            if e:
                ans.append(e)
            if o: ans.append(o)
        return ans

    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        sign = -1 if num < 0 else 1
        s = sorted(list(map(int, str(abs(num)))))
        zr, zl = bisect_right(s, 0), bisect_left(s, 0)
        zeros = zr - zl
        if sign > 0:
            # min + 000 + rest
            mn = s[zr]
            rest = s[zr + 1:]
            # print(mn, rest)
            return int(str(mn) + '0' * zeros + ''.join(map(str, rest)))
        else:
            # rev + 000
            rest = s[zr:][::-1]
            # print(rest)
            return -int(''.join(map(str, rest)) + '0' * zeros)

    def minimumTime(self, s: str) -> int:
        """
        "011001111111101001010000001010011"

        12 / 88 test cases passed.
        """
        def build(s):
            rf = []
            s += '$'
            i, j = 0, 0
            while i < len(s) - 1:
                j = i
                while s[j] == s[i]:
                    j += 1
                # s[j] != s[i]
                if s[i] == '1':
                    rf.append(j - i)
                else:
                    rf.append(0)
                i = j
            return rf

        def bt(r, cost, res):
            if not r or not any(r):
                res.append(cost)
                return

            # remove left
            bt(r[1:], cost + (1 if r[0] == 0 else r[0]), res)
            bt(r[:-1], cost + (1 if r[-1] == 0 else r[-1]), res)

        rf = build(s)
        print(rf)
        res = []
        bt(rf, 0, res)
        return min(res)


class Bitset:
    def __init__(self, size: int):
        self.sz = size
        self.O = set()
        self.Z = set(range(size))

    def fix(self, idx: int) -> None:
        if idx in self.Z:
            self.O.add(idx)
            self.Z.remove(idx)

    def unfix(self, idx: int) -> None:
        if idx in self.O:
            self.O.remove(idx)
            self.Z.add(idx)

    def flip(self) -> None:
        # tmp = set()
        # for i in range(self.sz):
        #     if i not in self.O:
        #         tmp.add(i)
        # self.O = tmp
        self.O, self.Z = self.Z, self.O

    def all(self) -> bool:
        return len(self.O) == self.sz

    def one(self) -> bool:
        return len(self.O) != 0

    def count(self) -> int:
        return len(self.O)

    def toString(self) -> str:
        sb = []
        for i in range(self.sz):
            if i not in self.O:
                sb.append('0')
            else:
                sb.append('1')

        return ''.join(sb)


# v = '76005'
# v = '76'
# s = list(map(int, v))
# ss = sorted(s)
# print(ss)
# zl = bisect_left(ss, 0)
# zr = bisect_right(ss, 0)
# print(zl, zr)

sl = Solution()
# print(
#     sl.sortEvenOdd([
#         5, 39, 33, 5, 12, 27, 20, 45, 14, 25, 32, 33, 30, 30, 9, 14, 44, 15, 21
#     ]))
# print(sl.smallestNumber(310))
# print(sl.smallestNumber(-7605))
s = "011001111111101001010000001010011"
# s = '0000'
# s = '111'
# s = '1100101'
# s = "0010"
# s = '1111000'
print(sl.minimumTime(s))