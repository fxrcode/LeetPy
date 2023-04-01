"""
date: 03312023
tag: Medium, Mono-Stack
Lookback:
- OS: Monotonic stacks are a good option when a problem involves comparing the size of numeric elements, with their order being relevant.
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/
Explore-Queue-Stack. Stack: LIFO
"""


from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def archit91_mono(T: list[int]):
            """
            https://leetcode.com/problems/daily-temperatures/discuss/1574808/C%2B%2BPython-3-Simple-Solutions-w-Explanation-Examples-and-Images-or-2-Monotonic-Stack-Approaches
            Nice visualization and walk-through from brute-force to mono-stack
            """
            ans, s = [0] * len(T), deque()
            for cur in range(len(T) - 1, -1, -1):
                while s and T[s[-1]] <= T[cur]:
                    s.pop()
                ans[cur] = s[-1] - cur if s else 0
                s.append(cur)
            return ans

        return archit91_mono(temperatures)

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
TS = [[73, 74, 75, 71, 69, 72, 76, 73], [30, 40, 50, 60], [30, 60, 90], [90, 60]]

for T in TS:
    print(sl.dailyTemperatures(T))
