"""
✅ GOOD Logic (indexing)
tag: easy, google
Lookback:
- need to bend my mind to understand a = b*q+r, and recursive indexing
- code is simple, but logic/math is hard.
    * reminds me 528. Random Pick with Weight, code is 2-liner
Similar
- 41. Solution #1: in-place hashing
[ ] REDO
"""

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        def indecision_tree():
            """
            Runtime: 211 ms, faster than 23.08% of Python3 online submissions for Build Array from Permutation.

            https://leetcode.com/problems/build-array-from-permutation/discuss/1315926/Python-O(n)-Time-O(1)-Space-w-Full-Explanation
            """
            q = len(nums)

            # turn the array into a=qb+r
            for i in range(len(nums)):
                r = nums[i]

                # retrieve correct value from potentially already processed element
                # i.e. get r from something maybe already in the form a = qb + r
                # if it isnt already processed (doesnt have qb yet), that's ok b/c
                # r < q, so r % q will return the same value
                b = nums[nums[i]] % q
                nums[i] = q * b + r

            # extract just the final b values
            for i in range(len(nums)):
                nums[i] //= q
            return nums

        def fxr():
            res = [0] * len(nums)
            for i in range(len(nums)):
                res[i] = nums[nums[i]]
            return res

        return fxr()

        """
        BUG: got: [0, 2, 1, 3, 5, 4], expected: [0, 1, 2, 4, 5, 3]
        """

        def fxr_cyclic_WA():
            i = 0
            while i < len(nums):
                x = nums[nums[i]]
                if x != i:
                    nums[i], nums[x] = nums[x], nums[i]
                else:
                    i += 1
            return nums

        return fxr_cyclic()


sl = Solution()
print(sl.buildArray(nums=[0, 2, 1, 5, 3, 4]))
