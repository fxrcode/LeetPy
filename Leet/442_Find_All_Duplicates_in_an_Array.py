"""
Tag: Medium
Lookback: recall cyclic sort b/c it's a problem of nums in range [0,n] and deal with duplicate/missing
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        def fxr():
            bk = [0] * (len(nums) + 1)
            res = []
            for v in nums:
                bk[v] += 1
            for i, v in enumerate(bk):
                if v == 1:
                    res.append(i)
            return res

        def cyc_sort():
            i = 0
            while i < len(nums):
                correct_idx = nums[i] - 1
                if nums[correct_idx] != nums[i]:
                    nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                else:
                    i += 1
            dups = []
            for i in range(len(nums)):
                if nums[i] != i + 1:
                    dups.append(nums[i])
            return dups

        # return cyc_sort()

        def one_pass():
            # https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/4921063/Utilizing-Integer-Range-for-Duplicate-Identification
            # use elem as index to mark the corresponding elem as negative, if we encounter an elem is already neg, we know it's duplicate
            ans = []
            for i in range(len(nums)):
                x = abs(nums[i])
                if nums[x - 1] < 0:
                    ans.append(x)
                nums[x - 1] *= -1
            return ans

        return one_pass()


sl = Solution()
print(sl.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
print(sl.findDuplicates([4, 1, 2, 3, 2]))
print(sl.findDuplicates([2, 1, 1]))
print(sl.findDuplicates([1]))
