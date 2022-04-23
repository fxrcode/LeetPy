"""
✅ GOOD mono-stack
💡insight (logic + 2ptr)
tag: medium, mono-stack, 2ptr
Lookback:
- mono-incr vs mono-decr?
- same or reverse logic vs 84?

https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        def os_mono():
            """
            Runtime: 149 ms, faster than 34.54% of Python3 online submissions for Trapping Rain Water.

            XXX: compare with 84: mono-decr vs mono-incr
            """
            stk, res = [], 0
            for i, h in enumerate(height):
                while stk and height[stk[-1]] < h:
                    low_i = stk.pop()
                    # eg 1 is good example of this edge case
                    if not stk:
                        break
                    W = i - stk[-1] - 1
                    H = min(height[stk[-1]], h) - height[low_i]
                    res += W * H
                stk.append(i)
            return res

        return os_mono()

        def labuladong_dp():
            if not height:
                return 0
            n = len(height)
            ans = 0
            l_max, r_max = [0] * n, [0] * n
            l_max[0] = height[0]
            r_max[n - 1] = height[n - 1]
            # l_max[i]: max height [0...i]
            for i in range(1, n):
                l_max[i] = max(height[i], l_max[i - 1])
            # r_max[i]: max height [i...n-1]
            for i in range(n - 2, -1, -1):
                r_max[i] = max(height[i], r_max[i + 1])
            for i in range(1, n - 1):
                ans += min(l_max[i], r_max[i]) - height[i]
            return ans

        def labuladong_2ptr():
            """
            Runtime: 91 ms, faster than 33.76% of Python3 online submissions for Trapping Rain Water.
            T: O(N), M: O(1)
            TODO: fully understand the logic and difference
            """
            if not height:
                return 0
            n = len(height)
            l, r = 0, n - 1
            l_max, r_max = height[l], height[r]
            ans = 0
            while l <= r:
                l_max = max(height[l], l_max)
                r_max = max(height[r], r_max)
                if l_max < r_max:
                    ans += l_max - height[l]
                    l += 1
                else:
                    ans += r_max - height[r]
                    r -= 1
            return ans


sl = Solution()
print(sl.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(sl.trap(height=[4, 2, 0, 3, 2, 5]))
