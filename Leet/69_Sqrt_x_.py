"""
https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
Leetcode Explore: Binary Search - Template I

Given a non-negative integer x, compute and return the square root of x.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Runtime: 36 ms, faster than 84.66% of Python3 online submissions for Sqrt(x).

        [Python] Powerful Ultimate Binary Search Template. Solved many problems

        XXX: Minimize k, s.t. condition(k) is True
        """
        # BUG: l, r = 0, x. Same as right most pos of target, because l is the minimum
        #   that satified l**2 > x, l-1 is the solution. so we need to init r = x+1
        if x < 2:
            return x
        l, r = 2, x + 1
        while l < r:
            mid = (l + r) // 2
            if mid**2 > x:
                r = mid
            else:
                l = mid + 1

        return l - 1


sl = Solution()
print(sl.mySqrt(4))
print(sl.mySqrt(8))
print(sl.mySqrt(9))
