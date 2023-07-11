"""
https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
Leetcode Explore Array 101: Deleting Items from an Array
Explore Array & String: 2 pointer technique

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

XXX: Classic 2 pointer pattern, also explained in labuladong
XXX: read pointer always move faster than write pointer, because read traverse nums. while write only increase after candidate found
"""


from typing import List


class Solution:
    def removeElement_sol_II(self, nums: List[int], val: int) -> int:
        """
        https://leetcode.com/problems/remove-element/solution/
        XXX: When val is rare in nums, we can just use last item to try.
        T: O(n), n is # of val
        """
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Runtime: 28 ms, faster than 93.88% of Python3 online submissions for Remove Element.
        XXX: just use lomuto template. Crux is loop invariant
        XXX: T: O(len)
        """
        l = -1
        # XXX: loop-invariant: [0..l] != val
        for i in range(len(nums)):
            if nums[i] != val:
                l += 1
                nums[l] = nums[i]
        return l + 1

    def lomuto(self, nums: List[int]):
        """
        Also, quick sort is unstable due to the swap
        """
        pivot = nums[-1]
        l = -1
        # XXX: loop-invariant: [0..l] < p
        for i in range(len(nums) - 1):
            if nums[i] < pivot:
                l += 1
                nums[l], nums[i] = nums[i], nums[l]
        nums[l + 1], nums[-1] = nums[-1], nums[l + 1]
        return l + 1


sl = Solution()
print(sl.removeElement([3, 2, 2, 3], 3))
