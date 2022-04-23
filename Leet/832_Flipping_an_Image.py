"""
tag: easy
Lookback:
- similar to 48. rotate image, portion of operation
"""

from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def os():
            # Runtime: 81 ms, faster than 35.96% of Python3 online submissions for Flipping an Image.
            for row in image:
                for i in range((len(row) + 1) / 2):
                    """
                    In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
                    helps us find the i-th value of the row, counting from the right.
                    """
                    row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
            return image

        def fxr():
            """
            Runtime: 80 ms, faster than 37.65% of Python3 online submissions for Flipping an Image.

            """
            R, C = len(image), len(image[0])
            for row in image:
                i, j = 0, C - 1
                while i <= j:
                    if row[i] == row[j]:
                        flip = 1 - row[i]
                        row[i] = row[j] = flip
                    i, j = i + 1, j - 1
            return image
