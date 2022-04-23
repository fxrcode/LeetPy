'''
C3.ai phone
https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/
Leetcode Explore: Binary Search - Template III

XXX: Common snippet
'''

from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange_template_iii(self, nums: List[int],
                                 target: int) -> List[int]:
        """
        Your runtime beats 91.67 % of python3 submissions.
        """
        def bs(l, r, x):
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            return l

        # if not nums:
        #     return [-1, -1]

        # XXX: this is the trick to handle [6] find 6.
        # https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems/656774
        nums.append(1e10)
        fir = bs(0, len(nums) - 1, target)
        if nums[fir] != target:
            return [-1, -1]
        las = bs(0, len(nums) - 1, target + 1) - 1
        return [fir, las]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime: 92 ms, faster than 36.91% of Python3 online submissions.

        [Python] Powerful Ultimate Binary Search Template. Solved many problems
        https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
        """
        def find_first():
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        def find_last():
            '''
            Q: why search-space right is len(nums)?
            A: @mzbuddy The original search space is indeed [0, len(nums) - 1]. But we are returning left - 1,
            not left, so we need to set right = len(nums), otherwise, if we set right = len(nums) - 1, then
            len(nums) - 1 would never be returned, the maximum returned value is at most len(nums) - 2.
            That's not correct, since we don't include all possible values.

            '''
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return l - 1

        if not nums:
            return [-1, -1]
        fir, las = find_first(), find_last()
        if nums[fir] != target:
            return [-1, -1]
        return [fir, las]

    def searchRange_bisect(self, nums: List[int], target: int) -> List[int]:
        """
        Runtime: 123 ms, faster than 18.86% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.

        XXX: the indices will be equal only if the target is not in the list
        """
        first = bisect_left(nums, target)
        last = bisect_right(nums, target)

        if first == last:
            return [-1, -1]

        return [first, last - 1]


sl = Solution()
print(sl.searchRange_template_iii(nums=[5, 7, 7, 8, 8, 10], target=8))
print(sl.searchRange_template_iii(nums=[5, 7, 7, 8, 8, 10], target=6))
print(sl.searchRange_template_iii(nums=[6], target=6))
print(sl.searchRange_template_iii(nums=[], target=6))
