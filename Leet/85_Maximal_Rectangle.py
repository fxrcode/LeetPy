"""
Daily Challenge (Nov 30)

"""
from collections import defaultdict
from typing import List


class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        def os_max_height() -> int:
            """
            Runtime: 212 ms, faster than 62.67% of Python3 online submissions for Maximal Rectangle.

            [ ] REDO
            """
            if not mat:
                return 0

            m = len(mat)
            n = len(mat[0])

            # initialize left as the leftmost boundary possible
            left = [0] * n
            # initialize right as the rightmost boundary possible
            right = [n] * n
            height = [0] * n

            maxarea = 0

            for i in range(m):
                cur_left, cur_right = 0, n
                # update height
                for j in range(n):
                    if mat[i][j] == "1":
                        height[j] += 1
                    else:
                        height[j] = 0
                # update left
                for j in range(n):
                    if mat[i][j] == "1":
                        left[j] = max(left[j], cur_left)
                    else:
                        left[j] = 0
                        cur_left = j + 1
                # update right
                for j in range(n - 1, -1, -1):
                    if mat[i][j] == "1":
                        right[j] = min(right[j], cur_right)
                    else:
                        right[j] = n
                        cur_right = j
                # update the area
                for j in range(n):
                    maxarea = max(maxarea, height[j] * (right[j] - left[j]))

            return maxarea

        def os_max_rec_historgram():
            """
            TLE: 70 / 71 test cases passed.


            """
            mxarea = 0
            if not mat or len(mat) == 0:
                return 0
            T, m, n = defaultdict(int), len(mat), len(mat[0])
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == "0":
                        continue

                    # compute max widht and update dp with it
                    T[i, j] = T[i, j - 1] + 1 if j else 1
                    width = T[i, j]

                    for k in range(i, -1, -1):
                        width = min(width, T[k, j])
                        mxarea = max(mxarea, width * (i - k + 1))
            return mxarea

        def fxr_dp_WA():
            if not mat or len(mat) == 0:
                return 0
            T, m, n = defaultdict(lambda: [0, 0]), len(mat), len(mat[0])
            T[-1, 0] = T[0, -1] = (0, 0)

            # T[i,j] is max rec with right-bottom cornor @(i,j), value = max rec W/H
            # for i in range(m):
            #     if mat[i][0] == '1':
            #         w, h = T[i-1, 0]
            #         T[i, 0] = [w, h+1]
            # for j in range(n):
            #     if mat[i][0] == '1':
            #         w, h = T[0, j-1]
            #         T[0, j] = [h, w+1]
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == "0":
                        continue
                    # up
                    uw, uh = T[i - 1, j]
                    # left
                    lw, lh = T[i, j - 1]
                    # up area
                    ua = min(uw + 1, lw) * min(uh + 1, lh)
                    # left area
                    la = min(uh, lh + 1) * min(lw + 1, uw)
                    if ua + la == 0:
                        T[i, j] = [1, 1]
                        continue

                    if ua > la:
                        T[i, j] = [min(uw + 1, lw), min(uh + 1, lh)]
                    else:
                        T[i, j] = [min(lw + 1, uw), min(uh, lh + 1)]
            print(T)
            return max(T.values(), key=lambda tu: tu[0] * tu[1])

        return os_max_height()


sl = Solution()
print(sl.maximalRectangle([]))
print(sl.maximalRectangle(["1"]))
print(
    sl.maximalRectangle(
        mat=[
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)
