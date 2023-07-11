"""
date: 04082023
tag: Easy, Hashmap
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

"""


from collections import defaultdict, deque
from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def fxr():
            """
            Runtime: 28 ms, faster than 94.76% of Python3 online submissions for Find Anagram Mappings.

            AC in 1
            T: O(N), M: O(N)
            """
            d = defaultdict(deque)
            for i, v in enumerate(nums2):
                d[v].append(i)
            ans = []
            for v in nums1:
                ans.append(d[v].popleft())
            return ans

        return fxr()


sl = Solution()
print(sl.anagramMappings(nums1=[12, 28, 46, 32, 50], nums2=[50, 12, 32, 46, 28]))
print(sl.anagramMappings(nums1=[84, 46], nums2=[84, 46]))
print(sl.anagramMappings(nums1=[84, 46, 46], nums2=[46, 84, 46]))
