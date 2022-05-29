"""
✅ GOOD DP
Tag: Hard, Stack, DP
Lookback:
- 1st time seeing this kind of dp function
- Kevin
"""


from functools import cache


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def dbabichev_dp():
            """
            Runtime: 67 ms, faster than 40.99% of Python3 online submissions for Longest Valid Parentheses.

            """

            @cache
            def dp(i):
                if i < 0 or s[i] == "(":
                    return 0
                j = i - dp(i - 1) - 1
                if j >= 0 and s[j] == "(":
                    return 2 + dp(i - 1) + dp(j - 1)
                return 0

            return max(dp(i) for i in range(len(s))) if s else 0

        return dbabichev_dp()

        def os_stack():
            """
            Runtime: 59 ms, faster than 24.44% of Python3 online submissions for Longest Valid Parentheses.

            leetcode official youtube solution, nice explain

            T: O(N)
            """
            ans = 0
            stk = [-1]  # means valid parentheses can only start from 0
            for i, c in enumerate(s):
                if c == "(":
                    stk.append(i)
                else:
                    stk.pop()
                    if not stk:
                        stk.append(i)
                    else:
                        ans = max(ans, i - stk[-1])
            return ans

        return os_stack()


sl = Solution()
# example from leetcode official: https://www.youtube.com/watch?v=39CEPFCl5sE
print(sl.longestValidParentheses("(()(())"))
print(sl.longestValidParentheses("(()"))
print(sl.longestValidParentheses(")()())"))
