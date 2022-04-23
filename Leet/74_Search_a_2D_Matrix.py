"""
tag: Medium, bisect
Lookback:
- Kevin: bisect
- Don't treat it as a 2D matrix, just treat it as a sorted list
"""
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def fxr_bisect_left():
            """
            Runtime: 61 ms, faster than 44.18% of Python3 online submissions for Search a 2D Matrix.
            T: O(N)
            """
            if not matrix or not matrix[0]:
                return False
            m, n = len(matrix), len(matrix[0])
            l, r = 0, m * n - 1
            while l < r:
                mid = (l + r) // 2
                x, y = divmod(mid, n)
                v = matrix[x][y]
                print(x, y, v)
                if v >= target:
                    r = mid
                else:
                    l = mid + 1

            x, y = divmod(l, n)
            return matrix[x][y] == target

        return fxr_bisect_left()


sl = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 3
target = 13
print(sl.searchMatrix(matrix, target))
