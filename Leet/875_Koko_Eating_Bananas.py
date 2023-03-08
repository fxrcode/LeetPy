"""
✅ GOOD Binary Search  济公学院 Example I.
https://leetcode.com/discuss/interview-question/354854/Facebook-or-Phone-Screen-or-Cut-Wood

Daily Challenge (Jan 20, 2022)

Example in Labuladong Ch 5.3.1
Similar to Lintcode 138. Wood Cut.

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Return the minimum integer k such that she can eat all the bananas within h hours.

similar:
- [774. Minimize Max Distance to Gas Station](https://leetcode.com/problems/minimize-max-distance-to-gas-station/discuss/113633/C++JavaPython-Binary-Search)
- 1539 [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/discuss/779999/JavaC++Python-O(logN))
- 1482 [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/discuss/686316/javacpython-binary-search/578488)
- 1283 [Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/discuss/446376/javacpython-bianry-search/401806)
- 1231 [Divide Chocolate](https://leetcode.com/problems/divide-chocolate/discuss/408503/Python-Binary-Search)
- 1011 [Capacity To Ship Packages In N Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/256729/javacpython-binary-search/351188?page=3)
- 410 [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)
"""

from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Runtime: 584 ms, faster than 37.34% of Python3 online submissions for Koko Eating Bananas.

        ✅ 济公学院's bool func is useful: The generic binary search find minimum x that f(x) is True!
            or say: f(x) maps x to FFTT!
        eg. 138. Wood Cut's largest segment.
        """

        def bin_search():
            def f(x: int) -> bool:
                """
                math.ceil is quite handy!
                if p < x, then p/x < 1, so ceil => 1
                if p >= x, say p/x = 2.5, then ceil => 3
                """
                hr = 0
                for p in piles:
                    hr += ceil(p / x)
                return hr <= h

            l, r = 1, max(piles)
            while l < r:
                x = (l + r) // 2
                # zhijun_liao: Powerful Ultimate Binary Search Template: Minimize k, s.t. f(k) is True
                #  f(k) map problem to FFFTTT, find first index of T
                if f(x):
                    r = x
                else:
                    l = x + 1
            return l

        return bin_search()

        def bruteforce():
            l, r = 1, max(piles)
            for eat in range(l, r + 1):
                hr = 0
                for p in piles:
                    cost = p // eat + (1 if p % eat != 0 else 0)
                    hr += cost
                    # print(cost, hr)
                if hr <= h:
                    return eat
            return -1


sl = Solution()
print(sl.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(sl.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(sl.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
