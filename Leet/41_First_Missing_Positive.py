"""
✅ GOOD Sort
✅ GOOD Logic
tag: hard, hash, logic
Lookback:
- 1st time: 'Cyclic sort'
- DON'T be smart, separate things into steps to make logic crystal clear
- amazon VO3 - Mar 16, 2022

[ ] REDO
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        def makuiyu_cyclic_sort():
            """
            Runtime: 1198 ms, faster than 51.56% of Python3 online submissions for First Missing Positive.

            cycle sort to put valid A[i] into correct position: idx = A[i]-1
            eg. [3,4,-1,1]
            valid range is [1...4], so correct positions is in [0...3]
            3's correct pos = 3-1 = 2
            4's correct pos = 4-1 = 3
            -1 out of [1...4], so skip to try next number
            1's correct pos = 1-1 = 0
            """
            i = 0
            n = len(nums)
            while i < n:
                idx = nums[i] - 1
                # put num[i] to the correct place if nums[i] in the range [1, n]
                if 0 <= idx < n and nums[i] != nums[idx]:
                    nums[i], nums[idx] = nums[idx], nums[i]
                else:
                    i += 1
            # so far, all the integers that could find their own correct place
            # have been put to the correct place, next thing is to find out the
            # place that occupied wrongly
            for i in range(n):
                if nums[i] != i + 1:
                    return i + 1
            return n + 1

        return makuiyu_cyclic_sort()

        def asones():
            """
            Runtime: 1610 ms, faster than 16.24% of Python3 online submissions for First Missing Positive.


            For nums with length n, the possible result is in the range of
            [1 : n + 1], we want to know the smallest integer in the range
            of [1 : n] that is not in nums, if [1 : n] are all in nums,
            the result is n + 1

            So those numbers not in [1 : n] are not useful and we can just
            change them to be 0

            Then we go through nums, if nums[i] is in the range of
            [1 : n], we use index (nums[i] - 1) to record that we have
            seen nums[i] by adding n + 1 to nums[nums[i] - 1]

            Finally we just need to find the first index i for which
            nums[i] is less than n + 1 (which means we never met number
            i + 1 so we did not add n + 1 to nums[i])
            """
            nonlocal nums
            n = len(nums)
            for i in range(n):
                if nums[i] < 1 or nums[i] > n:
                    nums[i] = 0

            for i in range(n):
                if 1 <= nums[i] % (n + 1) <= n:
                    idx = nums[i] % (n + 1) - 1
                    nums[idx] += n + 1

            for i in range(n):
                if nums[i] <= n:
                    return i + 1

            return n + 1

        return asones()

        '''
        def fxr_WA():
            """
            BUG: same wrong idea as in 2018, didn't learn from done problem!!! RED FLAG!
            """

            A = nums
            for i in range(len(A)):
                if A[i] <= 0:
                    # A[i] *= -1
                    A[i] = 0.5
                elif 0 < A[i] <= len(A):
                    A[i] *= -1
                else:
                    A[i] = 0.5
            print(A)
            for i, n in enumerate(A):
                if n > 0.5:
                    return i + 1
            return len(A)
        '''


sl = Solution()
print(sl.firstMissingPositive(nums=[1, 2, 0]))
print(sl.firstMissingPositive(nums=[3, 4, -1, 1]))
