'''
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1393/
Leetcode explore Queue & Stack: Conclusion
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.
'''


from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(r, c, visited):
            """[summary]
            AC in first try, but needs refactor
            """
            oriCol = image[r][c]
            image[r][c] = newColor
            visited.add((r, c))
            for xx, yy in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if (xx, yy) in visited:
                    continue
                if xx < 0 or xx >= len(image) or yy < 0 or yy >= len(image[0]):
                    continue
                if oriCol != image[xx][yy]:
                    continue
                dfs(xx, yy, visited)

        orig_color = image[sr][sc]

        def dfs_yangshun(r, c):
            # base
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            if image[r][c] != orig_color:
                return
            # cur
            image[r][c] = newColor
            # recur
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                print((r+dx, c+dy))
                dfs_yangshun(r+dx, c+dy)

        if image[sr][sc] != newColor:
            # dfs(sr, sc, newColor, set())
            dfs_yangshun(sr, sc)
        return image


sl = Solution()
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(sl.floodFill(image, 1, 1, 2))
