"""
WC 291, Apr 30, 2022
2/2
Q3: TLE
"""


from collections import defaultdict
from typing import List


class Solution:
    def appealSum(self, s: str) -> int:
        pass

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        def cnt(l, r):
            subdist = set()
            for i in range(l, r):
                for j in range(i + 1, r + 1):
                    subdist.add(tuple(nums[i:j]))
            return subdist

        l, r = 0, 0
        n = len(nums)
        divcnt = 0
        tot = set()
        while r < n:
            c = nums[r]
            r += 1
            if c % p == 0:
                divcnt += 1
            while divcnt > k:
                # contract win
                d = nums[l]
                l += 1
                if d % p == 0:
                    divcnt -= 1
            # now divcnt <= k
            # sz = r - l
            # tot += sz // 2 * (sz + 1)
            sub = cnt(l, r)
            print(l, r, sub)
            tot.update(sub)
        print(tot)
        return len(tot)

    def minimumCardPickup(self, cards: List[int]) -> int:
        occ = {}
        mn = 2e9
        for i, c in enumerate(cards):
            if c not in occ:
                occ[c] = i
            else:
                dist = i - occ[c] + 1
                mn = min(mn, dist)
                occ[c] = i
        return -1 if mn == 2e9 else mn

    def removeDigit(self, number: str, digit: str) -> str:
        mx = 0
        for i, n in enumerate(number):
            if n == digit:
                t = number[:i] + number[i + 1 :]
                if int(t) > mx:
                    mx = int(t)
                    ans = t
        return ans


sl = Solution()
print(sl.countDistinct(nums=[2, 3, 3, 2, 2], k=2, p=2))
# print(sl.countDistinct(nums=[1, 2, 3, 4], k=4, p=1))
# print(sl.minimumCardPickup([3, 4, 2, 3, 4, 7]))
# print(sl.minimumCardPickup([1, 0, 5, 3]))
# print(sl.removeDigit("123", "3"))
# print(sl.removeDigit(number="551", digit="5"))
