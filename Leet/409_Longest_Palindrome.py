"""
tag: easy, hash
Lookback
- logic is important in counting problem
"""


from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        def dbabichev():
            """
            Runtime: 28 ms, faster than 97.69% of Python3 online submissions for Longest Palindrome.
            XXX: using logic
            """
            odds = sum([freq % 2 for freq in Counter(s).values()])
            return len(s) if odds <= 1 else len(s) - odds + 1

        def fxr():
            """
            Runtime: 53 ms, faster than 36.50% of Python3 online submissions for Longest Palindrome.
            XXX: same logic as in 2016...
            """
            C = Counter(s)
            ans = 0
            has_odds = 0
            for k, v in C.items():
                if v % 2 == 0:
                    ans += v
                else:
                    ans += v - 1
                    has_odds += 1

            if has_odds:
                ans += 1
            return ans
