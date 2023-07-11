"""

https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions

similar: 162
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def fxr():
            """
            Runtime: 76 ms, faster than 69.76% of Python3 online submissions for Peak Index in a Mountain Array.

            AC in 1.
            """
            l, r = 1, len(arr) - 1
            while l < r:
                mid = (l + r) // 2
                # BUG: Don't wordy translate! if arr[mid-1] > arr[mid] > arr[mid+1]:
                if arr[mid - 1] > arr[mid]:
                    r = mid
                else:
                    l = mid + 1
            return l - 1

        return fxr()


sl = Solution()
AA = [
    [0, 1, 0],
    [0, 2, 1, 0],
    [0, 10, 5, 2],
    [3, 4, 5, 1],
    [24, 69, 100, 99, 79, 78, 67, 36, 26, 19],
]
for A in AA:
    print(sl.peakIndexInMountainArray(A))
