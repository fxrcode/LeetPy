'''
FB tag (easy)
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        def half():
            """
            Runtime: 91 ms, faster than 28.09% of Python3 online submissions for Palindrome Number.

            https://leetcode.com/problems/palindrome-number/discuss/785314/Python-3-greater-1-solution-is-89.20-faster.-2nd-is-99.14-faster.-Explanation-added
            """
            nonlocal x
            if x < 0 or (x > 0 and x % 10 == 0):
                return False

            res = 0
            while x > res:
                res = res * 10 + x % 10
                x = x // 10
            if x == res or x == res // 10:
                return True
            return False