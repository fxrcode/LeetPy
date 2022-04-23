"""
Tag: Easy, Skill
Lookback:
- practice to AC in 3min
"""

from typing import List


class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        def mxmb():
            # Runtime: 38 ms, faster than 86.73% of Python3 online submissions for Array Transformation.
            while True:
                pre = list(arr)
                for i in range(1, len(arr) - 1):
                    if pre[i] < min(pre[i - 1], pre[i + 1]):
                        arr[i] += 1
                    elif pre[i] > max(pre[i - 1], pre[i + 1]):
                        arr[i] -= 1
                if pre == arr:
                    return arr

        return mxmb()


sl = Solution()
print(sl.transformArray(arr=[6, 2, 3, 4]))
print(sl.transformArray(arr=[1, 6, 3, 4, 3, 5]))
print(sl.transformArray([6, 5, 8, 6, 7, 7, 3, 9, 8, 8, 3, 1, 2, 9, 8, 3]))
