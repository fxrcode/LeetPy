"""
Weekly Contest (Mar 12, 2022)
2/4
"""

from functools import cache
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        @cache
        def dp(left, p):
            # print(left, p)
            if p >= len(nums) or left < 0:
                return -1
            if left == 0:
                if p < len(nums):
                    return nums[p]
            ans = dp(left - 1, p + 1)
            if left >= 2:
                ans = max(ans, dp(left - 2, p), dp(left - 2, p + 2))
            if left >= 3:
                ans = max(
                    ans,
                    dp(left - 3, p + 1),
                    dp(left - 3, p + 3),
                    max(nums[p : p + 3] + [-1]) if p < len(nums) else -1,
                )
            # if left >= 4:
            #     ans = max(ans, dp(left - 4, p), dp(left - 4, p + 4))
            return ans

        return dp(k, 0)

    def digArtifacts(
        self, n: int, artifacts: List[List[int]], dig: List[List[int]]
    ) -> int:
        dig = set([(i, j) for i, j in dig])
        cnt = 0
        for r1, c1, r2, c2 in artifacts:
            art = set([(r, c) for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)])
            if art.intersection(dig) == art:
                cnt += 1
        return cnt

    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        kjs = [i for i, n in enumerate(nums) if n == key]
        ans = set()
        for i, n in enumerate(nums):
            for j in kjs:
                if abs(i - j) <= k:
                    ans.add(i)
        return list(ans)


sl = Solution()
print(sl.maximumTop(nums=[5, 2, 2, 4, 0, 6], k=4))
print(sl.maximumTop(nums=[2], k=1))
print(sl.maximumTop([99, 95, 68, 24, 18], 69))
print(sl.maximumTop([2], 1))
print(
    sl.maximumTop(
        [
            73,
            63,
            62,
            16,
            95,
            92,
            93,
            52,
            89,
            36,
            75,
            79,
            67,
            60,
            42,
            93,
            93,
            74,
            94,
            73,
            35,
            86,
            96,
        ],
        59,
    )
)
print(sl.maximumTop([18], 3))

# nums = [2, 2, 2, 2, 2]
# key = 2
# k = 2
# print(sl.findKDistantIndices(nums, key, k))
# n = 2
# artifacts = [[0, 0, 0, 0], [0, 1, 1, 1]]
# # dig = [[0, 0], [0, 1]]
# dig = [[0, 0], [0, 1], [1, 1]]
# print(sl.digArtifacts(n, artifacts, dig))
