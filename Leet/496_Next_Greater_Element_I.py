"""
tagg: easy, mono-stack
Lookback:
- coding skill snippet, NGE, PSE
"""
from collections import deque
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def fxr():
            """
            Runtime: 87 ms, faster than 37.22% of Python3 online submissions for Next Greater Element I.

            """
            d = {}  # number to next_greater
            st = []  # mono-stack

            for i in range(len(nums2) - 1, -1, -1):
                while st and st[-1] <= nums2[i]:
                    st.pop()
                d[nums2[i]] = -1 if not st else st[-1]
                st.append(nums2[i])
            return list(map(d.get, nums1))

        return fxr()


sl = Solution()
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(sl.nextGreaterElement(nums1, nums2))
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
print(sl.nextGreaterElement(nums1, nums2))
