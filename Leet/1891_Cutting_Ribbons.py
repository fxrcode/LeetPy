"""
Tag: Medium, bisect
Lookback:
- In a conclusion, It does not hurt(since it's logn) to set the bounds a little wider so you dont need to tweak the boundary condition ;)

"""

from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def fxr():
            """
            Runtime: 1237 ms, faster than 97.89% of Python3 online submissions for Cutting Ribbons.

            https://leetcode.com/problems/cutting-ribbons/discuss/1263773/Python-3-Binary-Search-O(nlogn)O(1)-One-Template-solves-ALL-BS/1042748
            """

            def cnt(x):
                seg = 0
                for n in ribbons:
                    seg += n // x
                return seg

            # BUG: if r = sum(ribbons)//k, then got WA: 9999 rather 10000 for case 4
            l, r = 1, sum(ribbons) // k + 1
            while l < r:
                mid = (l + r) // 2
                if cnt(mid) < k:
                    r = mid
                else:
                    l = mid + 1
            return l - 1

        return fxr()


sl = Solution()
print(sl.maxLength(ribbons=[9, 7, 5], k=3))
print(sl.maxLength(ribbons=[7, 5, 9], k=4))
print(sl.maxLength(ribbons=[5, 7, 9], k=22))
print(sl.maxLength([1, 10000, 10000, 10000], k=3))
