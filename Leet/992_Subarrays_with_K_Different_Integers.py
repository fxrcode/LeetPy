"""
💡insight (logic & sliding-window)
tag: Hard, Sliding Window

Lookback:
- GraceMeng: so-called sliding window technique needs an aggregated requirement, for example, the window with at most K dinstinct or with at least K dinstinct.
"""

from collections import Counter
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def lee215_sliding():
            """
            Runtime: 656 ms, faster than 37.64% of Python3 online submissions for Subarrays with K Different Integers.

            https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window
            T: O(N)
            """

            def atMost(K):
                dist = Counter()
                l, r = 0, 0
                res = 0
                k = 0
                while r < len(nums):
                    c = nums[r]
                    if dist[c] == 0:
                        k += 1
                    dist[c] += 1
                    r += 1
                    while k > K:
                        d = nums[l]
                        dist[d] -= 1
                        if dist[d] == 0:
                            k -= 1
                        l += 1
                    # now k <= K
                    res += r - l + 1
                return res

            return atMost(k) - atMost(k - 1)

        return lee215_sliding()


sl = Solution()
print(sl.subarraysWithKDistinct(nums=[1, 2, 1, 2, 3], k=2))
print(sl.subarraysWithKDistinct(nums=[1, 2, 1, 3, 4], k=3))
