"""
Tag: Easy, 
Lookback:
- `in` doesn't work for subarr in list check
"""

from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        def fxr():
            for i in range(len(arr)):
                p = arr[i : i + m]
                # BUG: if arr[i : i + m] * k in arr[i:]:
                if p * k == arr[i : i + m * k]:
                    return True
            return False

        return fxr()


sl = Solution()
print(sl.containsPattern(arr=[1, 2, 4, 4, 4, 4], m=1, k=3))
print(sl.containsPattern(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2))
print(sl.containsPattern(arr=[1, 2, 1, 2, 1, 3], m=2, k=3))
