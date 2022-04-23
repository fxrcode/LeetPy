"""
tag: Easy
Lookback:
- 410
- Write neat code
"""

from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        def fxr():
            """
            Runtime: 57 ms, faster than 25.33% of Python3 online submissions for Number of Lines To Write String.

            same as #410. feasible()
            """
            o = lambda c: ord(c) - ord("a")
            lines, width = 1, 0
            for c in s:
                wid = widths[o(c)]
                width += wid
                if width > 100:
                    width = wid
                    lines += 1
            return [lines, width]

        return fxr()


sl = Solution()
print(sl.numberOfLines(widths=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], s="abcdefghijklmnopqrstuvwxyz"))
assert sl.numberOfLines(widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], s="bbbcccdddaaa") == [2, 4]
