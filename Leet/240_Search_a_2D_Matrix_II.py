"""
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2872/
Leetcode explore Recursion II: Divide and Conquer

XXX: This kind of a matrix is called a Young Tableau. CLRS has a good explanation.
https://en.wikipedia.org/wiki/Young_tableau

tag: medium, bisect, logic

Lookback
- best solution: O(m+n)
- variant bisect: O(mlogn)
- O(M+N) can be worse than O(NlogM) if M is much large than N.

similar:
- 47
- 1428
- 1351 (Kevin, FB)
"""

import logging
from bisect import bisect_left
from typing import List

logging.basicConfig(level=logging.DEBUG)


class Solution:
    def searchMatrix_brainchiang_tw(self, matrix: List[List[int]], target: int) -> bool:
        """
        https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/528263/Two-efficient-python-sol.-sharing.-90%2B-w-Diagram
        Two approaches:
        method 1: variant binary search. O(mlogn)
        method 2: adaptive search from bottom-left. O(m+n)
        """

        def method1a(mat: List[List[int]], target) -> bool:
            # https://www.geeksforgeeks.org/binary-search-bisect-in-python/
            # Your runtime beats 32.09 % of python3 submissions.
            for r in range(len(mat)):
                row = mat[r]
                if row[0] <= target <= row[-1]:
                    i = bisect_left(row, target)
                    if i != len(row) and row[i] == target:
                        # print(f'found {target} @ {(r,i)}')
                        return True
            return False

        def method1b(mat: List[List[int]], target) -> bool:
            def binary_search(a: List[int], x: int) -> int:
                """
                Your runtime beats 72.69 % of python3 submissions.

                [Python] Powerful Ultimate Binary Search Template. Solved many problems (Leetcode post)
                https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
                """
                l, r = 0, len(a) - 1
                while l < r:
                    mid = (l + r) // 2
                    if a[mid] >= target:
                        r = mid
                    else:
                        l = mid + 1
                return l

            for r in range(len(mat)):
                row = mat[r]
                if row[0] <= target <= row[-1]:
                    idx = binary_search(row, target)
                    if idx != len(row) and row[idx] == target:
                        return True
            return False

        def method2(mat: List[List[int]], target) -> bool:
            # Your runtime beats 34.63 % of python3 submissions.
            h, w = len(mat), len(mat[0])

            r, c = h - 1, 0
            while r >= 0 and c < w:
                cur = mat[r][c]
                if cur == target:
                    print(f"found {target} @ {(r,c)}")
                    return True
                elif cur < target:
                    c += 1
                else:
                    r -= 1
            return False

        # return method1(matrix, target)
        # return method2(matrix, target)
        return method1b(matrix, target)

    def searchMatrix_fxr(self, matrix: List[List[int]], target: int) -> bool:
        """
        Runtime: 338 ms, faster than 5.04% of Python3 online submissions for Search a 2D Matrix II.
        AC in 1st try.

        Took so much time on cranking the indexing of submatrix!!!
        """

        def helper(mat: List[List[int]], top_l, bot_r, target) -> bool:
            """
            As taught in explore recursion II, the 1st thought is to break matrix into 4 submatrix and compare pivot with target,
            then discard one, so D&C on the rest 3 submatrix.

            There's more optimal D&C cut in the 2nd strategy.


            https://superuser.com/questions/1328283/how-to-draw-boxes-and-tables-in-plain-text
            Here's the indexing of submatrix ==> It's very important to illustration/naming in big/clear manner.
            +-----------------------+---------------------+
            |                      | |                    |
            |           1          |b|          2         |
            |                      | |                    |
            +----------------------   --------------------+
            |           a           p           c         |   # p for pivot, at Centroid of matrix in 1st strategy
            +----------------------   --------------------+   # take care of very row/col of p!!!
            |                      | |                    |
            |           3          |d|          4         |
            |                      | |                    |
            +-----------------------+---------------------+
            """
            if top_l[0] > bot_r[0] or top_l[1] > bot_r[1]:
                # if submatrix don't exist, I should return False because I can't find target!
                return False
            pi = ((top_l[0] + bot_r[0]) // 2, (top_l[1] + bot_r[1]) // 2)
            pivot = mat[pi[0]][pi[1]]

            logging.debug(f"pivot {pivot} at loc: {pi}")

            # sub1 ul,br; sub2 ul, br; sub3 ul, br; sub4 ul, br.
            # Careful on index vs index-1 (for discard, we include index)
            # sub1 = top_left, (pivot_idx[0]-1, pivot_idx[1]-1)
            # sub2 = (top_left[0], pivot_idx[1]+1), (pivot_idx[0]-1, bot_right[1])
            # sub3 = (pivot_idx[0]+1, top_left[1]), (bot_right[0], pivot_idx[1]-1)
            # sub4 = (pivot_idx[0]+1, pivot_idx[1]+1), bot_right

            # print(sub1, sub2, sub3, sub4)

            if pivot == target:
                logging.debug(f"found {pivot} at {pi}")
                return pi
            elif pivot < target:
                # discard submatrix < pivot (aka submatrix #1+a+b) <=> only check #2,3,4
                return (
                    helper(mat, (top_l[0], pi[1] + 1), (pi[0] - 1, bot_r[1]), target)
                    or helper(mat, (pi[0] + 1, top_l[1]), (bot_r[0], pi[1]), target)
                    or helper(mat, (pi[0], pi[1] + 1), bot_r, target)
                )
            else:
                # pivot > target: discard submatrix > pivot > target (aka sub4+c+d) <==> only check #1,2,3
                return (
                    helper(mat, top_l, (pi[0] - 1, pi[1] - 1), target)
                    or helper(mat, (top_l[0], pi[1]), (pi[0] - 1, bot_r[1]), target)
                    or helper(mat, (pi[0], top_l[1]), (bot_r[0], pi[1] - 1), target)
                )

        return helper(matrix, (0, 0), (len(matrix) - 1, len(matrix[0]) - 1), target)


sl = Solution()
print(
    sl.searchMatrix_brainchiang_tw(
        matrix=[
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        target=20,
    )
)
