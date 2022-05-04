"""
Tag: Medium, Hash, Sort
Lookback:
- bad in counting problems
"""

from collections import Counter
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        def os_2sum():
            """
            Runtime: 743 ms, faster than 73.22% of Python3 online submissions for Max Number of K-Sum Pairs.

            T: O(nlogn), M: O(n)
            """
            nums.sort()
            l, r = 0, len(nums) - 1
            res = 0
            while l < r:
                lr = nums[l] + nums[r]
                if lr < k:
                    l += 1
                elif lr > k:
                    r -= 1
                else:
                    res += 1
                    l, r = l + 1, r - 1
            return res

        return os_2sum()

        def dbabichev():
            freq, res = Counter(nums), 0
            for n in freq:
                res += min(freq[n], freq[k - n])
            return res // 2

        return dbabichev()

        def fxr():
            freq = Counter(nums)
            ops = 0
            for n in list(freq.keys()):
                if n * 2 == k:
                    ops += freq[n] // 2
                    freq.pop(n)
                if k - n in freq:
                    ops += min(freq[n], freq[k - n])
                    freq.pop(n)
                    freq.pop(k - n)
            return ops


sl = Solution()
print(sl.maxOperations(nums=[1, 2, 3, 4], k=5))
print(sl.maxOperations(nums=[3, 1, 3, 4, 3], k=6))
print(sl.maxOperations([2, 2, 2, 3, 1, 1, 4, 1], 4))
print(sl.maxOperations([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3))
