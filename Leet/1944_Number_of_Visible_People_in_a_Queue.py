"""
每日一题打卡群 (12/4/2021)
"""

from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        def fxr_mono():
            """
            Runtime: 1188 ms, faster than 74.47% of Python3 online submissions for Number of Visible People in a Queue.

            https://leetcode.com/problems/number-of-visible-people-in-a-queue/discuss/1363940/C%2B%2BJavaPython-Monotonic-stack-Visualize-picture-Clean-and-Concise

            T: O(N)
            """
            mono = []
            L = len(heights)
            ans = [0] * L
            for i in range(L - 1, -1, -1):
                cur = heights[i]
                while mono and heights[mono[-1]] < cur:
                    ans[i] += 1
                    mono.pop()
                if mono:
                    ans[i] += 1
                mono.append(i)
            return ans

        return fxr_mono()


sl = Solution()
print(sl.canSeePersonsCount(heights=[10, 6, 8, 5, 11, 9]))
