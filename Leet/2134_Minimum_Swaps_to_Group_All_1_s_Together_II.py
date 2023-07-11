"""
Weekly Contest 275 (Jan 8, 2022)
"""
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def fxr_labuladong():
            """
            Runtime: 2275 ms, faster than 75.00% of Python3 online submissions for Minimum Swaps to Group All 1's Together II.

            XXX: l,r update vs result update
            T:O(N)
            """
            ones = nums.count(1)
            n = len(nums)
            res = n
            cnt = 0
            l, r = 0, 0
            while r < 2 * n:
                c = nums[r % n]
                r += 1
                cnt += c
                while r - l >= ones:
                    d = nums[l % n]
                    l += 1
                    res = min(res, ones - cnt)
                    cnt -= d
            return res

        return fxr_labuladong()


sl = Solution()
print(sl.minSwaps(nums=[0, 1, 0, 1, 1, 0, 0]))
print(sl.minSwaps(nums=[0, 1, 1, 1, 0, 0, 1, 1, 0]))
print(sl.minSwaps(nums=[1, 1, 0, 0, 1]))
