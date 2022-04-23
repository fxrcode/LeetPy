"""
✅ GOOD Array (Presum + Bucket-Sort)
tag: easy, sort
Lookback:
- group first occurrence: dict.setdefault(num, idx)
- sort nums in limited: counting sort. T: O(N)
- smaller: presum
Similar: 
- 315, 493, 1365

[ ] REDO
"""

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def pythonic_1liner():
            return [sum(j < i and j != i for j in nums) for i in nums]

        def lenchen1112():
            # Runtime: 114 ms, faster than 63.21% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
            indices = {}
            for i, n in enumerate(sorted(nums)):
                indices.setdefault(n, i)
            return [indices[n] for n in nums]

        def localhostghost_CountSort():
            """
            Runtime: 96 ms, faster than 70.41% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

            https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/discuss/553078/Python3-Easy-Bucket-Sort-O(n)-Beats-100
            """
            buckets = [0] * 101
            for n in nums:
                buckets[n] += 1
            pre = 0
            for n, b in enumerate(buckets):
                if b != 0:
                    buckets[n] = pre
                    pre += b
            return [buckets[n] for n in nums]

        return localhostghost_CountSort()

        def fxr_bf():
            """
            Runtime: 64 ms, faster than 89.75% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

            T: O(2*nlogn), M: O(N)
            """
            nonlocal nums
            A = [(n, i) for i, n in enumerate(nums)]
            A.sort()
            res = [0] * len(nums)

            def bileft(x):
                l, r = 0, len(nums) - 1
                while l < r:
                    mid = (l + r) // 2
                    if A[mid][0] >= x:
                        r = mid
                    else:
                        l = mid + 1
                return l

            for n, i in A:
                j = bileft(n)
                res[i] = j
            return res

        return fxr_bf()


sl = Solution()
print(sl.smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
# print(sl.smallerNumbersThanCurrent(nums=[7, 7, 7, 7]))
