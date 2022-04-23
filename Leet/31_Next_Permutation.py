"""
✅ GOOD Backtracking (logic)
Tag: Medium, Recursive
Lookback: 
- Good eg: 0125330 -> 0130235
- it's not implemented in backtracking, but requires fully understanding backtracking
Similar: 
- 1386. Iterator for Combination
- [ ] TODO: Nayuki: previous permutation

https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def oldCodingFarmer():
            """
            Runtime: 63 ms, faster than 43.54% of Python3 online submissions for Next Permutation.

            Do not return anything, modify nums in-place instead.
            REF: Love Back to Back SWE, explain the logic of algs by understanding permutation backtrack!
                * https://www.youtube.com/watch?v=quAS1iydq7U
                * pivot, succesor: https://leetcode.com/problems/next-permutation/discuss/13994/Readable-code-without-confusing-ij-and-with-explanation
            """
            nonlocal nums
            i = j = len(nums) - 1
            while i >= 1 and nums[i - 1] >= nums[i]:
                i -= 1
            if i == 0:
                """
                http://web.stanford.edu/class/archive/cs/cs106a/cs106a.1212/handouts/mutation.html
                binding vs mutation
                BUG: nums = nums[::-1]
                """
                nums[::] = nums[::-1]
                return
            k = i - 1
            while nums[j] <= nums[k]:
                j -= 1
            nums[k], nums[j] = nums[j], nums[k]
            nums[k + 1 :] = nums[k + 1 :][::-1]

        return oldCodingFarmer()


sl = Solution()
# print(sl.nextPermutation([1, 2, 3]))
print(sl.nextPermutation([3, 2, 1]))
# print(sl.nextPermutation([1]))
print(sl.nextPermutation([6, 2, 1, 5, 4, 0, 3]))
