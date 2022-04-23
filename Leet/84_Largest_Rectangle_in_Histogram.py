"""
tag: Hard, Stack
Lookback:
- Naming important! I mixed enumerated h & heights[stk.pop()], debugged a while.
- Weekly Special (Jan W5)

Similar:
239. Sliding Window Maximum https://leetcode.com/problems/sliding-window-maximum/discuss/951683/Python-Decreasing-deque-short-explained
496. Next Greater Element I
739. Daily Temperatures
862. Shortest Subarray with Sum at Least K
901. Online Stock Span
907. Sum of Subarray Minimums
1687. Delivering Boxes from Storage to Ports

"""


from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def fxr():
            """
            Runtime: 1248 ms, faster than 59.47% of Python3 online submissions for Largest Rectangle in Histogram.

            https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/995249/Python-increasing-stack-explained
            """
            ans, stk = 0, []
            for i, h in enumerate(heights + [0]):
                while stk and heights[stk[-1]] >= h:
                    H = heights[stk.pop()]
                    W = i if not stk else i - stk[-1] - 1
                    ans = max(ans, W * H)
                # now stk mono-incr
                stk.append(i)
            return ans

        return fxr()


sl = Solution()
print(sl.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
print(sl.largestRectangleArea(heights=[2, 4]))
