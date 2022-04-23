"""
tag: easy
Lookback:

"""

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        def fxr():
            # Runtime: 68 ms, faster than 89.02% of Python3 online submissions for Decompress Run-Length Encoded List.
            res = []
            for i in range(0, len(nums), 2):
                f, x = nums[i], nums[i + 1]
                res.extend([x] * f)
            return res

        return fxr()


sl = Solution()
print(sl.decompressRLElist([1, 2, 3, 4]))
assert sl.decompressRLElist(nums=[1, 1, 2, 3]) == [1, 3, 3]
