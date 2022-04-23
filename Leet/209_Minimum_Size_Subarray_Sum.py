"""
tag: medium, bisect, presum, slide-window
Lookback
- subarr => slide-window
- subarr sum => presum, {nums[i..j] = presum[j+1]-presum[i]}

similar:
713. Subarray Product Less Than K

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
Explore Array & String: 2 pointer technique
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""


from bisect import bisect_left
from collections import deque
from typing import List


class Solution:
    def minSubArrayLen_sol_binSearch(self, target: int, nums: List[int]) -> int:
        """
        Runtime: 88 ms, faster than 71.62% of Python3 online submissions for Minimum Size Subarray Sum.

        https://leetcode.com/problems/minimum-size-subarray-sum/solution/
        Binary Search approach, detail coding basic skill on indexing

        T: O(nlogn)
        """
        n = len(nums)
        if n == 0:
            return 0
        ans = 1e9
        # presum[0] means sum of first 0 elements, presum[k] means sum of first k elements
        presum = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            to_find = target + presum[i - 1]  # to_find - presum[i] = target
            bound = bisect_left(presum, to_find)
            if bound != len(presum):  # crux, means not found large enough subarr
                ans = min(ans, (bound - (i - 1)))
        return ans if ans != 1e9 else 0

    def minSubArrayLen_fxr_sol(self, target: int, nums: List[int]) -> int:
        """
        Runtime: 111 ms, faster than 48.00% of Python3 online submissions for Minimum Size Subarray Sum.
        https://leetcode.com/problems/minimum-size-subarray-sum/discuss/1249381/Python-Sliding-Window-O(N)-Clean-and-Concise

        My implementation based on solution idea, but still using labuladong's template
        """
        l, r, n = 0, 0, len(nums)
        ans = n + 1
        wind = 0  # window sum
        while r < n:
            wind += nums[r]
            r += 1
            while wind >= target:
                ans = min(ans, r - l)
                wind -= nums[l]
                l += 1
        return ans if ans != n + 1 else 0

    def minSubArrayLen_fxr(self, target: int, nums: List[int]) -> int:
        """
        Runtime: 1392 ms, faster than 5.06% of Python3 online submissions for Minimum Size Subarray Sum.

        AC in 1! XXX: 1st time using sliding window myself.
        Obviously not optimal, because O(N^2) due to sum(nums)
        """
        l, r, n = 0, 0, len(nums)
        wind = deque()
        ans = [0, n]
        if sum(nums) < target:
            return 0
        while r < n:
            c = nums[r]
            r += 1
            wind.append(c)

            while sum(wind) >= target:
                if r - l + 1 <= ans[1] - ans[0] + 1:
                    ans = [l, r]
                    print(ans)
                d = nums[l]
                l += 1
                wind.popleft()
        print(ans)
        return ans[1] - ans[0]


sl = Solution()
print(sl.minSubArrayLen_sol_binSearch(3, nums=[1, 2, 3, 4, 5]))


def test_bisect():
    nums = [0, 4, 7, 12]
    for n in [7, 8, 100]:
        print(n, bisect_left(nums, n))


test_bisect()
