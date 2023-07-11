"""
✅ GOOD Coding Skill

Facebook Tag
tag: Easy

similar:
1827. Minimum Operations to Make the Array Increasing
2111. Minimum Operations to Make the Array K-Increasing
80. Remove Duplicates from Sorted Array II

"""

from bisect import bisect_left
from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def astareadytocode():
            """
            https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/discuss/1300632/Dynamic-Programming-Approach-LIS-variant-

            T: O(nlogn)
            """

            def lis(A):
                """
                From 300. Longest Increasing Subsequence
                T: O(nlogn)
                """
                sub = []
                for n in nums:
                    i = bisect_left(sub, n)
                    # if n is greater than any element in sub
                    if i == len(sub):
                        sub.append(n)

                    # ow, replace the first elem in sub >= n
                    else:
                        sub[i] = n
                return len(sub)

            ls = lis(nums)
            return len(nums) - ls < 2

        return astareadytocode()

        def ye15():
            """
            Runtime: 81 ms, faster than 54.81% of Python3 online submissions for Remove One Element to Make the Array Strictly Increasing.

            https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/discuss/1298457/Python3-collect-non-conforming-indices
            https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/discuss/1298517/Python%3A-Explained%3A-Easy-to-understand%3A-O(n)-Time-and-O(1)-Space
            https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/discuss/1299306/Two-Conditions

            XXX: check Stefan's 2ptr in 80. Remove Duplicates from Sorted Array II

            T: O(N) one-pass!
            """
            prev, drop = -1e5, False  # drop means we have saw drop or not
            for i, x in enumerate(nums):
                if prev < x:
                    prev = x
                else:
                    # if drop again, fail termination
                    if drop:
                        return False
                    drop = True
                    # Two cases
                    #   a) 1,3,2: remove 3, so update prev = 2 for next iter
                    #   b) 2,3,1: remove 1, so prev = 3 (stays) for next iter
                    if i == 1 or nums[i - 2] < x:
                        prev = x
            return True

        def fxr():
            """
            Your runtime beats 76.38 % of python3 submissions.

            T: O(3N)
            XXX: not that
            """
            cand = []
            for i in range(1, len(nums)):
                if nums[i - 1] >= nums[i]:
                    if cand:
                        return False
                    cand.extend([i - 1, i])

            def check(rm):
                A = nums[:rm] + nums[rm + 1 :]
                for i in range(1, len(A)):
                    if A[i - 1] >= A[i]:
                        return False
                return True

            if not cand:
                return True

            print(cand)
            return check(cand[0]) or check(cand[1])


sl = Solution()
# nums = [1, 2, 10, 5, 7]
# nums = [2, 3, 1, 2]
nums = [1, 1, 1]
print(sl.canBeIncreasing(nums))
