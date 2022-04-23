"""
tag: Easy, 2ptr
Lookback:
- similar: #360

https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
Leetcode Explore: Array 101: Conclusion

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""


from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def os_2ptr():
            """
            Runtime: 234 ms, faster than 86.25% of Python3 online submissions for Squares of a Sorted Array.

            """
            n = len(nums)
            res = [0] * n
            l, r = 0, n - 1
            for i in range(n - 1, -1, -1):
                left, right = nums[l], nums[r]
                if abs(left) > abs(right):
                    res[i] = left * left
                    l += 1
                else:
                    res[i] = right * right
                    r -= 1
            return res

        return os_2ptr()

        def clarencechee_2ptr():
            """[summary]
            https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
            XXX: nums sorted, and square order's max candidates should in 2 ends!
            XXX: 1st saw r-l as index
            """
            res = [0] * len(nums)
            l, r = 0, len(nums) - 1
            # XXX: because r-l is mono-decreasing [n-1->0], so we can use it as index
            while l <= r:
                left, right = nums[l], nums[r]
                if abs(left) < abs(right):
                    res[r - l] = right**2
                    r -= 1
                else:
                    res[r - l] = left**2
                    l += 1
            return res

        def fxr_bf():
            res = []
            for n in nums:
                res.append(n * n)
            res.sort()
            return res


sl = Solution()

nums = [-4, -1, 0, 3, 10]
print(sl.sortedSquares(nums))
assert sl.sortedSquares(nums=[-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
