"""
tag: easy, matrix
Lookback:
- 289. Game of Life

"""

from typing import List


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        def jb07():
            """
            Runtime: 830 ms, faster than 51.52% of Python3 online submissions for Image Smoother.

            https://leetcode.com/problems/image-smoother/discuss/454951/Python3-simple-solution
            XXX: handy list comprehension for valid range of submatrix
            """
            R, C = len(M), len(M[0])
            res = [[0] * C for _ in range(R)]
            dirs = [
                (0, 0),
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
                (1, 1),
                (-1, -1),
                (-1, 1),
                (1, -1),
            ]
            for x in range(R):
                for y in range(C):
                    tmp = [
                        M[x + dx][y + dy]
                        for dx, dy in dirs
                        if 0 <= x + dx < R and 0 <= y + dy < C
                    ]
                    res[x][y] = sum(tmp) // len(tmp)
            return res

        return jb07()
