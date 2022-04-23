"""
tag: Medium, presum, Hash
Lookback:
- subarr sum => presum (This is NOT slide-window)
- only hash first occurrence of presum => to get longest subarr
Similar:
560. Subarray Sum Equals K
561. Binary Subarrays With Sum
"""

from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        def os():
            """
            Runtime: 497 ms, faster than 56.45% of Python3 online submissions for Maximum Size Subarray Sum Equals k.

            T: O(N)
            """
            # def atMost(x):
            #     pass
            presum = longest_subarr = 0
            indices = {}

            for i, num in enumerate(nums):
                presum += num

                # Check if all of the numbers seen so far sum to k.
                if presum == k:
                    longest_subarr = i + 1

                # If any subarray seen so far sums to k, then
                # update the length of the longest_subarray.
                elif presum - k in indices:
                    longest_subarr = max(longest_subarr, i - indices[presum - k])

                # Only add the current prefix_sum index pair to the
                # map if the prefix_sum is not already in the map.
                if presum not in indices:
                    indices[presum] = i

            return longest_subarr

        return os()


sl = Solution()
print(sl.maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3))
print(sl.maxSubArrayLen(nums=[-2, -1, 2, 1], k=1))
