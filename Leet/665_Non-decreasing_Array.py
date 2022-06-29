"""
✅ GOOD Logic Analysis (cases)
Tag: Medium, Logic, Math
Lookback:
- 
XXX: Follow up: what if you can change at most k elements?

https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions
"""

from typing import List


class Solution:
    def checkPossibility_FU(self, nums: List[int], k: int) -> bool:
        def yaroslav_repeta_dp(k):
            # TODO: how does DP work here?
            INF = 1e6
            dp = [-INF] * (k + 1) + [INF]
            for x in nums:
                for i in range(k, -1, -1):
                    dp[i] = min(x, dp[i - 1]) if dp[i] <= x else dp[i - 1]
            return dp[-2] != INF

        return yaroslav_repeta_dp(k)

    def checkPossibility(self, nums: List[int]) -> bool:
        def sgallivan_visual_analysis():
            """
            REF: https://leetcode.com/problems/non-decreasing-array/discuss/1190763/JS-Python-Java-C%2B%2B-or-Simple-Solution-w-Visual-Explanation

            TODO: how does the analysis translate into code? Why only consider YabY?
            """
            err = 0
            for i in range(1, len(nums)):
                if err or (
                    i > 1
                    and i < len(nums) - 1
                    and nums[i - 2] > nums[i]
                    and nums[i + 1] < nums[i - 1]
                ):
                    return False
                err = 1
            return True

        def os_greedy():
            """
            Runtime: 212 ms, faster than 44.34% of Python3 online submissions for Non-decreasing Array.

            XXX: when you see F[i] > F[i+1], which one do you change? decr F[i] or incr F[i+1]
                Here's the proof that greedy choice to be wise.
            """
            cnt_violations = 0
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    if cnt_violations == 1:
                        return False
                    cnt_violations += 1
                    if i >= 2 and nums[i - 2] > nums[i]:
                        nums[i] = nums[i - 1]
            return True


sl = Solution()
print(sl.checkPossibility(nums=[4, 2, 3]))
print(sl.checkPossibility(nums=[4, 2, 1]))
print(sl.checkPossibility(nums=[2, 3, 4, 2, 2, 2]))
print(sl.checkPossibility(nums=[5, 7, 1, 8]))
