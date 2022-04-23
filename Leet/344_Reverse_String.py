"""
tag: easy, str
Lookback:

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/
Explore Array & String: 2 pointer technique

Write a function that reverses a string. The input string is given as an array of characters s.

"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        AC in 1.
        Your runtime beats 81.73 % of python3 submissions.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s

    def reverseString_recur1(self, s: List[str]) -> None:
        def recur(s):
            l = len(s)
            if l < 2:
                return s
            return recur(s[l // 2 :]) + recur(s[: l // 2])

        s = recur(s)

    def reverseString_recur(self, s: List[str]) -> None:
        """
        XXX: Clean substring recursion: use l,r pointer as argument (aka state for subproblem)
        """

        def recur(s, l, r):
            if l > r:
                return
            s[l], s[r] = s[r], s[l]
            recur(s, l + 1, r - 1)

        recur(s, 0, len(s) - 1)


sl = Solution()
s = list("hello")
# sl.reverseString(list(s))
sl.reverseString_recur(s)
print(s)
