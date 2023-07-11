"""
✅ GOOD Interval (stefan)
FB tag (easy)
tag: easy, array

Lookback:
- learn generalized impl from stefan, reminds me: 1288. lee215, 57. StefanPochmann
- 1st time seeing Python: **slice assignment**: `r[1:]=(n,)` 
    * Slice assignment is a special syntax for lists, where you can insert, delete, or replace contents from a list
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def stefan():
            """
            Runtime: 48 ms, faster than 10.20% of Python3 online submissions for Summary Ranges.

            https://leetcode.com/problems/summary-ranges/discuss/63193/6-lines-in-Python

            r is current range (at most 2 elem)
            ranges += [[]] or ranges.append([])
            <=> r[1:] = [n] <=> r[1:] = n, (comma turns rhs a tuple)
            """
            ranges, r = [], []
            for n in nums:
                if n - 1 not in r:
                    r = []
                    ranges += [r]
                #!Wow: slice assignment - replace: https://www.learnbyexample.org/python-list-slicing/#insert-multiple-list-items
                #! if slice not exist, it just append rhs: https://stackoverflow.com/questions/65571630/why-is-this-slice-assignment-not-raising-an-error
                r[1:] = [n]
            return ["->".join(map(str, r)) for r in ranges]

        return stefan()

        def fxr():
            """
            Runtime: 28 ms, faster than 82.57% of Python3 online submissions for Summary Ranges.

            """
            i, j = 0, 0
            ans = []
            while i < len(nums):
                while j < len(nums) and nums[j] - nums[i] == j - i:
                    j += 1
                if j == i + 1:
                    ans.append(f"{nums[i]}")
                else:
                    ans.append(f"{nums[i]}->{nums[j-1]}")
                i = j
            return ans

        return fxr()


sl = Solution()
# print(sl.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
print(sl.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
