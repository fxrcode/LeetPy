"""
✅ GOOD Mono Stack
每日一题打卡群 (12/3/2021)
"""

from typing import List
from functools import cache


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        def monostk_lee215():
            """
            Runtime: 30 ms, faster than 80.80% of Python3 online submissions for Minimum Cost Tree From Leaf Values.

            T: O(N)
            REF: https://www.youtube.com/watch?v=xcYkzSrgOmY
            Understand the mono-stack analysis from FSM pov
            """
            res = 0
            stack = [float("inf")]
            for a in arr:
                while stack[-1] <= a:
                    mid = stack.pop()
                    res += mid * min(stack[-1], a)
                stack.append(a)
            while len(stack) > 2:
                res += stack.pop() * stack[-1]
            return res

        def greedy_n2():
            """
            Runtime: 52 ms, faster than 38.07% of Python3 online submissions for Minimum Cost Tree From Leaf Values.

            https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/478708/RZ-Summary-of-all-the-solutions-I-have-learned-from-Discuss-in-Python
            """
            res = 0
            while len(arr) > 1:
                i = arr.index(min(arr))
                if 0 < i < len(arr) - 1:
                    res += arr[i] * min(arr[i - 1], arr[i + 1])
                else:
                    res += arr[i] * (arr[i + 1] if i == 0 else arr[i - 1])
                arr.pop(i)
            return res

        def dp_n3():
            """
            Runtime: 327 ms, faster than 6.92% of Python3 online submissions for Minimum Cost Tree From Leaf Values.

            lee215: what's the complexity?
            N^2 states and O(N) to find each.
            So this solution is O(N^3) time and O(N^2) space.
            REF: https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/478708/RZ-Summary-of-all-the-solutions-I-have-learned-from-Discuss-in-Python
            https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/474188/I-think-I-able-to-explain-it-to-myself-and-to-you...(Java-DP)-.-Complexity-is-in-the-question
            """

            @cache
            def dfs(l, r):
                print(l, r)
                if l >= r:
                    return 0

                res = 1e9
                for k in range(l, r):
                    rootval = max(arr[l : k + 1]) * max(arr[k + 1 : r + 1])
                    res = min(res, dfs(l, k) + dfs(k + 1, r) + rootval)
                return res

            return dfs(0, len(arr) - 1)

        # return dp_n3()
        # return greedy_n2()
        return monostk_lee215()


sl = Solution()
# print(sl.mctFromLeafValues(arr=[6, 2, 4]))
print(sl.mctFromLeafValues(arr=[6, 2, 3, 7]))
