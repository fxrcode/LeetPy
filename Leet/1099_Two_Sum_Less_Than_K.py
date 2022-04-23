'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List
from bisect import bisect_left


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        def fxr():
            """
            Runtime: 44 ms, faster than 64.88% of Python3 online submissions for Two Sum Less Than K.

            T: O(nlogn), M: O(n)
            """
            nums.sort()
            l, r = 0, len(nums)-1
            ans = -1
            while l < r:
                slr = nums[l] + nums[r]
                if slr >= k:
                    r -= 1
                else:
                    l += 1
                    ans = max(ans, slr)
            return ans

        def os_bisec():
            """
            Runtime: 44 ms, faster than 64.88% of Python3 online submissions for Two Sum Less Than K.

            XXX: Note that the binary search returns the "insertion point" for the searched value, i.e. the position where
                that value would be inserted to keep the array sorted. So, the binary search result points to the first
                element that is equal or greater than the complement value. Since our sum must be smaller than k, we consider
                the element immediately before the found element.

            T: O(nlong), M: O(n)
            """
            ans = -1
            nums.sort()
            for i in range(len(nums)):
                j = bisect_left(nums, k-nums[i], i+1)
                if j > i:
                    ans = max(ans, nums[i] + nums[j])
            return ans

        # return fxr()


sl = Solution()
print(sl.twoSumLessThanK(nums=[34, 23, 1, 24, 75, 33, 54, 8], k=60))
