'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

✅ GOOD Binary Search (Even index only)
TODO: OS Approach 2: Binary Search
'''


from typing import List
from bisect import bisect_left


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def os_brute():
            for i in range(0, len(nums)-2, 2):
                if nums[i] != nums[i+1]:
                    return nums[i]
            return nums[-1]

        def os_even_idx():
            """
            Runtime: 60 ms, faster than 97.98% of Python3 online submissions for Single Element in a Sorted Array.

            XXX: fully understand the question and it's property
            * len(nums) = odd because 2n + 1
            * The single element is the 1st even idex not followed by its pair!

            NOTE: so we only need to binary search on even index. How to do that? Easy: if odd, then -1 => even! Then we do binary search.
                careful, to maintain even, we should mid+2! rather mid+1
            """
            l, r = 0, len(nums)-1
            while l < r:
                mid = (l+r)//2
                if mid % 2:
                    mid -= 1
                if nums[mid] == nums[mid+1]:
                    l = mid + 2
                else:
                    r = mid
            return nums[l]

        def fxr_linear_xor():
            """
            Runtime: 72 ms, faster than 54.91% of Python3 online submissions for Single Element in a Sorted Array.

            T: O(N). xor all numbers, but not using the property: sorted
            """
            ans = nums[0]
            for i in range(1, len(nums)):
                ans ^= nums[i]
            return ans

        def fxr_bisect():
            """
            Runtime: 76 ms, faster than 30.03% of Python3 online submissions for Single Element in a Sorted Array.

            T: O(logN)
            """
            l, r = 0, len(nums)-1
            while l < r:
                mid = (l+r)//2
                if mid % 2 == 1:
                    if nums[mid] == nums[mid-1]:
                        l = mid + 1
                    else:
                        r = mid
                else:
                    if mid + 1 == len(nums):
                        return nums[mid]
                    if nums[mid] == nums[mid+1]:
                        l = mid+1
                    else:
                        r = mid
            return nums[l]
