from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        def fxr():
            """
            Runtime: 182 ms, faster than 10.77% of Python3 online submissions for Minimum Difference Between Highest and Lowest of K Scores.
            T: O(N)
            """
            nums.sort()
            ans = 1e6
            for i in range(len(nums) - k + 1):
                ans = min(nums[i + k - 1] - nums[i], ans)
            return ans
