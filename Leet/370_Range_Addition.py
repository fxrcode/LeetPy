"""
小而美的算法技巧: 差分数组

"""
from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        Runtime: 357 ms, faster than 5.03% of Python3 online submissions for Range Addition.
        """
        ans = [0] * (length)
        for s, e, inc in updates:
            ans[s] += inc
            if e + 1 < length:
                ans[e + 1] -= inc
        for i in range(1, length):
            ans[i] += ans[i - 1]
        return ans


sl = Solution()
print(sl.getModifiedArray(length=5, updates=[[1, 3, 2], [2, 4, 3], [0, 2, -2]]))

