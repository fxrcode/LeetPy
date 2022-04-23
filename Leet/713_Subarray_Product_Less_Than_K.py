"""
tag: Medium, slide-window, bisect
Lookback:
- convert multiply into log plus
- 1st time seeing find upper bound st. < k => bisect_right(A, x-1e-9)
"""

from bisect import bisect_right
from math import log
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        def os_bisect():
            """
            Runtime: 1352 ms, faster than 9.28% of Python3 online submissions for Subarray Product Less Than K.

            log(a*b*c*d) = log(a)+log(b)+log(c)+log(d)
            Money exchange (Coinbase: Dijkstra, Bellman-Ford)
            """
            nonlocal k
            if k <= 0:
                return 0
            k = log(k)

            prefix = [0]
            for x in nums:
                prefix.append(prefix[-1] + log(x))

            ans = 0
            for i, x in enumerate(prefix):
                # find max prefix[j] st. prefix[j]-prefix[i] < k
                j = bisect_right(prefix, x + k - 1e-9, i + 1)
                ans += j - i - 1
            return ans

        return os_bisect()

        def fxr():
            """
            Runtime: 965 ms, faster than 44.32% of Python3 online submissions for Subarray Product Less Than K.

            Note that the Sliding window approach is only valid because numbers are positive.
            also relies on the fact that the numbers are all integers, hence cannot be between zero and 1. (We require prod to decrease as left increases)
            """
            if k <= 0:
                return 0
            cnt = 0
            l, r = 0, 0
            p = 1
            while r < len(nums):
                c = nums[r]
                r += 1
                p *= c
                while l < r and p >= k:
                    d = nums[l]
                    l += 1
                    p //= d
                # now p < k
                cnt += r - l

            return cnt

        return fxr()


sl = Solution()
print(sl.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100))
print(sl.numSubarrayProductLessThanK([1, 1, 1], 1))
