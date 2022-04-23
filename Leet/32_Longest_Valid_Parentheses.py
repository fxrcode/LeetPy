"""
Kevin

TuSimple list
[ ] TODO: still not sure the stack logic
tag: Hard, Stack
"""


class Solution:

    def longestValidParentheses(self, s: str) -> int:

        def os_stack():
            """
            Runtime: 59 ms, faster than 24.44% of Python3 online submissions for Longest Valid Parentheses.

            leetcode official youtube solution, nice explain

            T: O(N)
            """
            ans = 0
            stk = [-1]  # means valid parantheses can only start from 0
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
