"""
Tag: Easy, DP
Lookback:
- Study Plan: Dynamic Programming
- Explore Array & String: 2D Array
"""


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def archit91_topdown():
            """
            Runtime: 45 ms, faster than 57.99% of Python3 online submissions for Pascal's Triangle.

            """

            def f(n):
                if n:
                    f(n - 1)
                    ans.append([1] * n)
                    for i in range(1, n - 1):
                        ans[n - 1][i] = ans[n - 2][i] + ans[n - 2][i - 1]

            ans = []
            f(numRows)
            return ans

        return archit91_topdown()

        def fxr():
            """
            Your runtime beats 87.38 % of python3 submissions.
            AC in 1. Used trick from ??? to append dummy 0 in both end to generalize the pre[i]+pre[i+1]
            """
            res = [[1]]

            for l in range(1, numRows):
                new_level = []
                pre = [0] + res[-1] + [0]
                for i in range(len(pre) - 1):
                    new_level.append(pre[i] + pre[i + 1])
                # done this new level
                res.append(new_level)
            return res


sl = Solution()
print(sl.generate(5))
