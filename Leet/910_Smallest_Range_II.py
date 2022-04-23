"""
✅ GOOD Logic
tag: Medium, Sort, Logic
Lookback:
- follow-up of #908 
"""


from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        def dim_sum():
            """
            Runtime: 160 ms, faster than 94.12% of Python3 online submissions for Smallest Range II.

            https://leetcode.com/problems/smallest-range-ii/discuss/173389/simple-C++-solution-with-explanation

            """
            nums.sort()
            left, right = nums[0] + k, nums[-1] - k
            ans = nums[-1] - nums[0]
            for p in range(len(nums) - 1):
                mn, mx = min(nums[p + 1] - k, left), max(nums[p] + k, right)
                ans = min(mx - mn, ans)
            return ans

        return dim_sum()


sl = Solution()
print(sl.smallestRangeII(nums=[1, 3, 6], k=3))
