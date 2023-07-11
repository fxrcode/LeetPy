"""
https://leetcode.com/explore/learn/card/binary-search/137/conclusion/978/
Leetcode Explore: Binary Search - Conclusion

similar: 69
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Runtime: 46 ms, faster than 35.82% of Python3 online submissions for Valid Perfect Square.
        T: O(logn)
        """
        if num < 2:
            return True
        l, r = 2, num // 2
        while l < r:
            mid = (l + r) // 2
            if mid**2 >= num:
                r = mid
            else:
                l = mid + 1
        # print(l)
        return l**2 == num


sl = Solution()
for v in [5, 16, 10000]:
    print(sl.isPerfectSquare(num=v))
