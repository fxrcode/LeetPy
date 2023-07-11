"""
✅ GOOD Coding Skill
Daily Challenge (Feb 6)
Lookback
- Stefan's logic is neat and crystal!
- Easy to extend to K duplicates!
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def stefanpochmann(k):
            """
            Runtime: 52 ms, faster than 90.93% of Python3 online submissions for Remove Duplicates from Sorted Array II.

            XXX: go through the numbers and include those in the result that haven't been included twice already.

            T: O(N)
            """
            w = 0
            for n in nums:
                if w < k or n > nums[w - k]:
                    nums[w] = n
                    w += 1
            print(nums)
            return w

        return stefanpochmann(k=1)

        def fxr():
            """
            Runtime: 87 ms, faster than 33.06% of Python3 online submissions for Remove Duplicates from Sorted Array II.
            T:O(N)
            """
            r1 = r2 = w = 0
            while r2 < len(nums):
                r1 = r2
                dup = 0
                while r2 < len(nums) and nums[r1] == nums[r2]:
                    r2 += 1
                    dup += 1
                    if dup <= 2:
                        nums[w] = nums[r1]
                        w += 1
            print(nums)
            return w


sl = Solution()
nums = [1, 1, 1, 2, 2, 3]
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(sl.removeDuplicates(nums))
