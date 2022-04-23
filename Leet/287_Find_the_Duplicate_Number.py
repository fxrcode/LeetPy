"""
✅ GOOD Logic (link-list: create edge i->nums[i])
tag: medium, bisect, pointer, sort
Lookback:
- as missing number, here comes cyclic-sort
- creativity: s = nums[s], f = nums[nums[f]]
- vs 41. 268

https://leetcode.com/explore/learn/card/binary-search/146/more-practices-ii/1039/
Leetcode Explore: Binary Search - More Practice

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
"""


from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def os_cyclic_sort():
            nonlocal nums
            while nums[0] != nums[nums[0]]:
                nums[nums[0]], nums[0] = nums[0], nums[nums[0]]
            return nums[0]

        return os_cyclic_sort()

        def bisect():
            """
            Your runtime beats 20.99 % of python3 submissions.

            https://leetcode.com/problems/find-the-duplicate-number/solution/
            XXX: The Art and Craft of Problem Solving: Abstract to concrete, so as to begin.
            Find that count is non-decreasing, so binary search O(nlogn), rather O(N^2) linear scan
            """
            l, r = 1, len(nums) - 1
            while l < r:
                cur = (l + r) // 2
                count = 0
                count = sum(n <= cur for n in nums)
                if count > cur:
                    r = cur
                else:
                    l = cur + 1
            print(l)
            return l

        def floyd_cycle():
            """
            https://leetcode.com/problems/find-the-duplicate-number/solution/
            XXX: this is so coooooooool to transform arr to linked list! Similar to 202. Happy Number
            Crux: encode list using f(x) = nums[x]
            """
            s, f = nums[0], nums[0]
            while True:
                s = nums[s]
                f = nums[nums[f]]
                if s == f:
                    break

            f = nums[0]
            while f != s:
                s = nums[s]
                f = nums[f]
            print(f)
            return f


sl = Solution()
print(sl.findDuplicate(nums=[1, 3, 4, 2, 2]))
print(sl.findDuplicate(nums=[3, 1, 3, 4, 2]))
print(sl.findDuplicate(nums=[1, 1, 2]))
print(sl.findDuplicate(nums=[2, 2, 2, 2, 2, 2]))
