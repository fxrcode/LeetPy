'''
FB tag (easy)

Parentheses Problem Foundation
More Parentheses Problem To Advance
Here is a ladder of parentheses problem, in order of problem number.

1541. Minimum Insertions to Balance a Parentheses String
1249. Minimum Remove to Make Valid Parentheses
1111. Maximum Nesting Depth of Two Valid Parentheses Strings
1190. Reverse Substrings Between Each Pair of Parentheses
1021. Remove Outermost Parentheses
921.  Minimum Add to Make Parentheses Valid
856.  Score of Parentheses
'''


class Solution:
    def maxDepth(self, s: str) -> int:
        def fxr():
            """
            Runtime: 32 ms, faster than 67.62% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.

            T: O(N), M:O(N)
            """
            mx = 0
            stk = []
            for c in s:
                if c == '(':
                    stk.append(c)
                    mx = max(mx, len(stk))
                elif c == ')':
                    stk.pop()
            return mx

        def lee215():
            """
            Runtime: 28 ms, faster than 86.37% of Python3 online submissions for Maximum Nesting Depth of the Parentheses.

            T: O(N), M: O(1)
            https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/discuss/888949/JavaC%2B%2BPython-Parentheses-Problem-Foundation
            """
            mx = cur = 0
            for c in s:
                if c == '(':
                    cur += 1
                    mx = max(mx, cur)
                elif c == ')':
                    cur -= 1
            return mx