"""
✅ GOOD Recursion
tag: medium, dfs, stack, logic
Lookback:
- Parenthesis <=> stack
- D&C recursion like Calculator/Evaluation problems, base case (primitive) is Crux to understand
- Kudo to Huahua's visualization analysis
Similar
- 726. Number of Atoms

"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def os_eval():
            """
            Runtime: 34 ms, faster than 23.58% of Python3 online submissions for Score of Parentheses.
            T: O(N^2)

            Approach 1: Divide and Conquer
            Call a balanced string primitive if it cannot be partitioned into two non-empty balanced strings.
            For each primitive substring (S[i], S[i+1], ..., S[k]), if the string is length 2, then the score of this string is 1. Otherwise, it's twice the score of the substring (S[i+1], S[i+2], ..., S[k-1]).

            """

            def F(i, j):
                ans = bal = 0
                for k in range(i, j):
                    bal += 1 if s[k] == "(" else -1
                    if bal == 0:
                        if k - i == 1:
                            ans += 1
                        else:
                            ans += 2 * F(i + 1, k)
                        i = k + 1
                return ans

            return F(0, len(s))

        def os_elegant():
            """
            Runtime: 42 ms, faster than 56.30% of Python3 online submissions for Score of Parentheses.

            Approach 3: Count Cores
            T: O(N)
            """
            ans, bal = 0, 0
            for i, x in enumerate(s):
                if x == "(":
                    bal += 1
                else:
                    bal -= 1
                    if s[i - 1] == "(":
                        ans += 1 << bal
            return ans

        return os_eval()


sl = Solution()
# print(sl.scoreOfParentheses("()"))
print(sl.scoreOfParentheses("(())"))
# print(sl.scoreOfParentheses("(()(()))"))
