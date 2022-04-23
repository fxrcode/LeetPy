"""
Weekly Special (W2 Mar 2022)
tag: medium, recursion, logic
Lookback:
- recursion = base & recurrence-relation
"""

from functools import cache
from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def os_dfs():
            """
            Runtime: 250 ms, faster than 62.88% of Python3 online submissions for Strobogrammatic Number II.

            !base-case & recurrence relation
            """
            REV_PAIRS = ["00", "11", "69", "88", "96"]

            @cache
            def dfs(l):
                if l == 0:
                    return [""]
                if l == 1:
                    return ["0", "1", "8"]
                """
                ME: ["1111","6119","8118","9116","1691","6699","8698","9696","1881","6889","8888","9886","1961","6969","8968","9966"]
                EXPECTED: ["1001","1111","1691","1881","1961","6009","6119","6699","6889","6969","8008","8118","8698","8888","8968","9006","9116","9696","9886","9966"]
                # BUG:
                # if l == 2:
                #     return ["11", "69", "88", "96"]
                """

                # if l == n and xy=='00', don't append.
                return [xy[0] + n_2 + xy[1] for n_2 in dfs(l - 2) for xy in REV_PAIRS if not (l == n and xy == "00")]

            return dfs(n)

        return os_dfs()


sl = Solution()
# print(sl.findStrobogrammatic(n=1))
print(sl.findStrobogrammatic(n=3))
print(sl.findStrobogrammatic(n=4))
