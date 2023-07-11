"""

Weekly Special (Dec W3)
"""


from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        def fxr():
            """
            Runtime: 2149 ms, faster than 40.92% of Python3 online submissions for Maximum Distance in Arrays.

            T: O(N), M: O(1)
            """
            INF = 1e6
            mn, mx = arrays[0][0], arrays[0][-1]
            d = 0
            for i in range(1, len(arrays)):
                arr = arrays[i]
                d = max(
                    d,
                    abs(arr[0] - mx),
                    abs(arr[-1] - mn),
                    abs(arr[0] - mn),
                    abs(arr[-1] - mx),
                )
                mn = min(mn, arr[0])
                mx = max(mx, arr[-1])
            return d

        return fxr()


sl = Solution()
print(sl.maxDistance(arrays=[[1, 2, 3], [4, 5], [1, 2, 3]]))
print(sl.maxDistance(arrays=[[1, 4], [0, 5]]))
