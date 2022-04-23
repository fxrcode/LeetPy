'''
Explore Array & String: 2D Array
https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

'''


from typing import List
from collections import deque


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        https://leetcode.com/problems/diagonal-traverse/discuss/581868/Easy-Python-NO-DIRECTION-CHECKING
        XXX: diagonals means each num's (r+c) is same! And even (r+c) means even level! And simple loop of matrix is always up to down
        XXX: Dicts are now ordered, get used to it https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/
        Changed in version 3.7: Dictionary order is guaranteed to be insertion order. This behavior was an implementation detail of CPython from 3.6.
        """
        d = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])

        res = []
        # due to Python3 dict ordered by insertion, it's in i+j = 0, 1, 2, ...
        for entry in d.items():
            if entry[0] % 2 == 0:
                res.extend(entry[1][::-1])
            else:
                res.extend(entry[1])
        return res

    def findDiagonalOrder_fxr(self, mat: List[List[int]]) -> List[int]:
        """
        Your runtime beats 30.82 % of python3 submissions.
        XXX: BFS variant
        """
        R, C = len(mat), len(mat[0])
        q = deque([(0, 0)])
        visited = set([(0, 0)])
        res = []
        odd = True
        while q:
            qlen = len(q)
            cur_level = []
            for _ in range(qlen):
                x, y = q.popleft()
                cur_level.append(mat[x][y])
                for dx, dy in [(0, 1), (1, 0)]:
                    xx, yy = x+dx, y+dy
                    if xx < R and yy < C and (xx, yy) not in visited:
                        q.append((xx, yy))
                        visited.add((xx, yy))
            if odd:
                cur_level.reverse()
            # BUG: DIR.reverse(). This won't work!
            res.extend(cur_level)
            odd = not odd
        return res


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sl = Solution()
print(sl.findDiagonalOrder(mat))
