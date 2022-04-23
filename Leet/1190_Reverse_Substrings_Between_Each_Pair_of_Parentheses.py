"""
TuSimple list

Similar: 394. Decode String
"""
from collections import deque


class Solution:
    def reverseParentheses(self, s: str) -> str:
        def fxr():
            """
            Runtime: 24 ms, faster than 97.48% of Python3 online submissions for Reverse Substrings Between Each Pair of Parentheses.

            """

            def dfs(q):
                res = ""
                while q:
                    c = q.popleft()
                    if c == "(":
                        inner = dfs(q)
                        res += inner[::-1]
                    elif c.isalpha():
                        res += c
                    elif c == ")":
                        break
                return res

            return dfs(deque(s))

        return fxr()


sl = Solution()
print(sl.reverseParentheses("(u(love)i)"))
