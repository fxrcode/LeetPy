"""
tag: easy
Lookback:

"""

from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        def fxr():
            """
            Runtime: 782 ms, faster than 48.93% of Python3 online submissions for Count Good Triplets.

            """
            l = len(arr)
            res = 0
            for i in range(l):
                for j in range(i + 1, l):
                    for k in range(j + 1, l):
                        if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            res += 1
            return res

        return fxr()


sl = Solution()
print(sl.countGoodTriplets(arr=[3, 0, 1, 1, 9, 7], a=7, b=2, c=3))
