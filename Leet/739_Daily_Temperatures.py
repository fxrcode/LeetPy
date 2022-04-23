"""
tag: Medium, Stack
Lookback:
- OS: Monotonic stacks are a good option when a problem involves comparing the size of numeric elements, with their order being relevant.
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/
Explore-Queue-Stack. Stack: LIFO
"""


from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def fxr():
            """
            Runtime: 1455 ms, faster than 61.95% of Python3 online submissions for Daily Temperatures.

            """
            n = len(temperatures)
            ans = [0] * n
            stk = []

            for i in range(n - 1, -1, -1):
                while stk and temperatures[stk[-1]] <= temperatures[i]:
                    stk.pop()
                # now its mono-decr
                ans[i] = 0 if not stk else stk[-1] - i
                stk.append(i)
            return ans

        return fxr()


sl = Solution()
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
temperatures = [30, 40, 50, 60]
temperatures = [30, 60, 90]
temperatures = [90, 60]

print(sl.dailyTemperatures(temperatures))
