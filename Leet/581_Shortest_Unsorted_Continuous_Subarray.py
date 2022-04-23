"""
✅ GOOD Logic
✅ GOOD Stack (mono)
tag: medium, sort, logic
Lookback:
- os approach 3 reminds me 1539. Kth missing positive, compare correct value to find inner property: idx!
- os approach 4: selective sorting?
"""

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        def os5_nostk():
            # TODO: no need of stack
        def os4_stk():
            """
            Runtime: 252 ms, faster than 71.80% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
            T: O(N), M: O(N)
            """
            stk = []
            l, r = len(nums), 0
            for i, n in enumerate(nums):
                while stk and nums[stk[-1]] > n:
                    l = min(stk.pop(), l)
                stk.append(i)
            stk = []
            for i in range(len(nums) - 1, -1, -1):
                while stk and nums[stk[-1]] < nums[i]:
                    r = max(stk.pop(), r)
                stk.append(i)
            return r - l + 1 if r - l > 0 else 0

        return os4_stk()

        def os3_sort():
            """
            Runtime: 224 ms, faster than 85.00% of Python3 online submissions for Shortest Unsorted Continuous Subarray.

            T: O(nlogn), M: O(N)
            """
            snums = sorted(nums)
            start, end = len(nums), 0
            for i, n in enumerate(nums):
                if n != snums[i]:
                    start = min(i, start)
                    end = max(i, end)
            return end - start + 1 if end - start >= 0 else 0

        return os3_sort()


sl = Solution()
nums = [2, 6, 4, 8, 10, 9, 15]
print(sl.findUnsortedSubarray(nums))
