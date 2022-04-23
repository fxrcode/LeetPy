"""
FB tag (easy)
tag: easy, str, 2ptr
Lookback
- logic!
- palindrome check in O(n)
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def yangshun():
            """
            Runtime: 151 ms, faster than 74.72% of Python3 online submissions for Valid Palindrome II.

            """
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    one, two = s[i:j], s[i + 1 : j + 1]
                    return one == one[::-1] or two == two[::-1]
                i, j = i + 1, j - 1
            return True

        return yangshun()


sl = Solution()
print(sl.validPalindrome(s="abca"))
