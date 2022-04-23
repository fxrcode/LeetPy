"""
tag: easy
Lookback:

"""

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def lee215():
            """
            O(NM)

            Returns:
                _type_: _description_
            """
            return sum(any(a > b for a, b in zip(col, col[1:])) for col in zip(*strs))

        return lee215()

        def fxr():
            """
            Runtime: 84 ms, faster than 99.53% of Python3 online submissions for Delete Columns to Make Sorted.
            O(NlogM)
            """
            cnt = 0
            for col in zip(*strs):
                # print(col, sorted(col))
                if list(col) != sorted(col):
                    cnt += 1
            return cnt

        return fxr()


sl = Solution()
print(sl.minDeletionSize(strs=["cba", "daf", "ghi"]))
