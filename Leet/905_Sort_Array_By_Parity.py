'''
https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/
leetcode explore: Array 101. In-place operations
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.


'''


from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Your runtime beats 68.24 % of python3 submissions.
        AC in 1st try.
        XXX: Lomuto partition: init s; swap

        """
        s = -1
        for f in range(len(nums)):
            if nums[f] % 2 == 0:
                s += 1
                # BUG: nums[s] = nums[f]
                nums[s], nums[f] = nums[f], nums[s]
        return nums


sl = Solution()
print(sl.sortArrayByParity([3, 1, 2, 4]))
print(sl.sortArrayByParity([0]))
