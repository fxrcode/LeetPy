"""
Tag: Easy, Logic
Lookback:
- smart grid[j][i] to update col max, so we can do yz in one-pass along with xz!
- reminds me #807, understand the projection direction
"""


class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        def os_1pass():
            """
            https://leetcode.com/problems/projection-area-of-3d-shapes/discuss/156726/C%2B%2BJavaPython-Straight-Forward-One-Pass
            T: O(N^2)
            """
            n = len(grid)
            cnt = 1
            for i in range(n):
                mxr, mxc = 0, 0
                for j in range(n):
                    if grid[i][j]:
                        cnt += 1  # xy
                    mxr = max(mxr, grid[i][j])  # xz
                    mxc = max(mxc, grid[j][i])  # yz
                cnt += mxr + mxc
            return cnt

        def fxr():
            """
            Runtime: 69 ms, faster than 95.27% of Python3 online submissions for Projection Area of 3D Shapes.
            T: O(3N^2)
            """
            cnt = 0
            # xy:
            cnt += sum(1 for row in grid for r in row if r)
            # xz: <===
            cnt += sum(max(row) for row in grid)
            # yz: ^
            cnt += sum(max(col) for col in zip(*grid))
            return cnt

        return fxr()


sl = Solution()
print(sl.projectionArea(grid=[[1, 2], [3, 4]]))
assert sl.projectionArea(grid=[[2]]) == 5
print(sl.projectionArea(grid=[[1, 0], [0, 2]]))
