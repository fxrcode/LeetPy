'''

https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
Leetcode Explore: Hash Table. Practical Application - HashSet


tag: Pigeonhole (check 164. Maximum Gap)
'''

from typing import List
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        def pigeonhole():
            pigeons = len(nums)
            holes = len(set(nums))
            return pigeons > holes

        return pigeonhole()


sl = Solution()
print(sl.containsDuplicate(nums=[1, 2, 3, 1]))
print(sl.containsDuplicate(nums=[1, 2, 3, 9]))
