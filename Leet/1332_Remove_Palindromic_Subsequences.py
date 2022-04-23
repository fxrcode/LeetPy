"""
tag: easy, logic
Lookback:
- AC in  1
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def os():
            if s == s[::-1]:
                return 1
            return 2

        def fxr():
            # Runtime: 18 ms, faster than 99.81% of Python3 online submissions for Remove Palindromic Subsequences.
            l, r = 0, len(s) - 1
            while l < r and s[l] == s[r]:
                l, r = l + 1, r - 1
            if l >= r:
                return 1
            return 2

        return fxr()


sl = Solution()
print(sl.removePalindromeSub("babababbababab"))
