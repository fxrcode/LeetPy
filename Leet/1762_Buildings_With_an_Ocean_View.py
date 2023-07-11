"""
FB tag (medium)
"""

from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        def os_best():
            """
            Runtime: 664 ms, faster than 96.44% of Python3 online submissions for Buildings With an Ocean View.

            XXX: no need of NGE, just need max_height till now, search from right to left.
            T: O(N), M: O(1)
            """
            L = len(heights)
            ans = []
            mx_height = -1
            for i in reversed(range(L)):
                if mx_height < heights[i]:
                    ans.append(i)
                    mx_height = heights[i]
            ans.reverse()
            return ans

        return os_best()

        def fxr_nge():
            """
            Runtime: 788 ms, faster than 46.94% of Python3 online submissions for Buildings With an Ocean View.

            T:O(N)
            """
            L = len(heights)
            stk = []
            ng = [-1] * L
            ans = []
            for i in range(L - 1, -1, -1):
                while stk and heights[stk[-1]] < heights[i]:
                    stk.pop()
                ng[i] = stk[-1] if stk else -1
                if ng[i] == -1:
                    ans.append(i)
                stk.append(i)
            return ans[::-1]

        return fxr_nge()


sl = Solution()
print(sl.findBuildings([4, 2, 3, 1]))
print(sl.findBuildings([4, 3, 2, 1]))
print(sl.findBuildings([1, 3, 2, 4]))
