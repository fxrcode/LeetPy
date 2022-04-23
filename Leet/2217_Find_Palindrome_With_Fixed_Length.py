"""
✅ GOOD Skills
tag: Medium, Math, Recursion, skills
Lookback:
- same as #89. Gray Code 
- Good Skills: indexing, reverse, %, l-1//2, etc
"""


from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def lee215():
            # Runtime: 648 ms, faster than 92.44% of Python3 online submissions for Find Palindrome With Fixed Length.
            l = intLength
            # 5 -> 2, 6 -> 2
            base = 10 ** ((l - 1) // 2)
            res = [q - 1 + base for q in queries]
            for i, a in enumerate(res):
                # 5 -> 103->01. 6 -> 103->301
                b = str(a) + str(a)[-1 - l % 2 :: -1]
                res[i] = int(b) if len(b) == l else -1
            return res

        return lee215()


sl = Solution()
# print(sl.kthPalindrome(queries=[1, 2, 3, 4, 5, 90], intLength=3))
print(sl.kthPalindrome(queries=[2, 4, 6], intLength=5))
