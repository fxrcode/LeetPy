"""
tag: easy, dfs
Lookback:
Similar:
- 733
- 489
https://leetcode.com/problems/island-perimeter/
Leetcode explore Queue & Stack: Conclusion

As mentioned in 733. Flood Fill's 1st comment, it's similar to 463.
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""


from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def flood_dfs():
            """
            Runtime: 1282 ms, faster than 5.00% of Python3 online submissions for Island Perimeter.
            Memory Usage: 26.6 MB, less than 5.01% of Python3 online submissions for Island Perimeter.

            https://leetcode.com/problems/island-perimeter/discuss/95004/Java-solution-with-DFS
            XXX: Flood fill DFS, just be careful in business logic: check border for 4 directions.
            XXX: Not familiar in D&C recursion (aka. with return)

            XXX: Eastlife: He is counting the grids who surround the island. When DFS to grid[i][j] who is out of bound, count++;
                DFS to grid[i][j] == 1, it will be set to -1 and never considered in the future; DFS to grid[i][j] == 0, count++
                (solved the problem that grid[i][j] == 0 should be counted two times in the corner). So rather than count the '1',
                this algorithm is counting'0's around the island. Really clever!

            Crux: dfs return 1 if reach boundary or water, else 0
            """

            def flood(r, c) -> int:
                # Check boundary conditions and return 1, since it is water
                if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                    return 1

                # Check if the cell is water and return 1. No need to do a DFS
                if grid[r][c] == 0:
                    return 1

                # check if visited, no count
                if grid[r][c] == -1:
                    return 0

                # mark visited
                grid[r][c] = -1
                count = 0

                # calculate perimeter in all four directions
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    count += flood(r + dx, c + dy)
                return count

            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c]:
                        return flood(r, c)
            return 0

        def dbabichev_iter():
            """
            Runtime: 636 ms, faster than 71.68% of Python3 online submissions for Island Perimeter.

            https://leetcode.com/problems/island-perimeter/discuss/95001/clear-and-easy-java-solution/99445
            A similar question asked at Google was "Trees Fencing - how much fencing is needed to cover tree groups (similar to island)".
            If the requirement is to give fencing for each group of trees, then you might need to apply dfs and find the group of trees.
            If it's just the total fencing, then below code should be good enough(even with land gaps in the middle of trees).
            """
            m, n, p = len(grid), len(grid[0]), 0

            for i in range(m):
                for j in range(n):
                    p += 4 * grid[i][j]
                    if i > 0:
                        p -= grid[i][j] * grid[i - 1][j]
                    if i + 1 < m:
                        p -= grid[i][j] * grid[i + 1][j]
                    if j > 0:
                        p -= grid[i][j] * grid[i][j - 1]
                    if j + 1 < n:
                        p -= grid[i][j] * grid[i][j + 1]
            return p

        return dbabichev_iter()

        """
        BUG: WA in 1st try. Coding while not having clear algs
        def flood(r, c, peri):
            # base
            # action
            print((r, c), '+4')
            peri[0] += 4
            grid[r][c] = -1

            o_r, o_c = r, c
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = r+dx, c+dy

                if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                    continue
                if grid[r][c] == 0:
                    continue
                if grid[o_r][o_c] < 0:
                    print((o_r, o_c), (r, c), '-1')
                    peri[0] -= 1
                else:
                    flood(r, c, peri)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                peri = [0]
                flood(r, c, peri)
                return peri[0]

        return 0
        """


sl = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(sl.islandPerimeter(grid))
