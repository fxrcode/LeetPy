"""
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

tag: easy, math
Lookback:
- not familiar presum, and how to calc subarr sum from it. Base-0 vs base-1?
- math count how many subarr including A[i]? better break into: subarr start from A[i] vs end with A[i]. Then multiply these 2!
"""

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        def lee215():
            """
            Runtime: 50 ms, faster than 86.80% of Python3 online submissions for Sum of All Odd Length Subarrays.

            https://leetcode.com/problems/sum-of-all-odd-length-subarrays/discuss/854184/JavaC%2B%2BPython-O(N)-Time-O(1)-Space
            https://youtu.be/J5IIH35EBVE?t=592

            XXX: In total, there are k = (i + 1) * (n - i) subarrays, that contains A[i].
            XXX: (k+1)//2 subarr w/ odd len, and k/2 subarr w/ even length.
            """
            res, n = 0, len(arr)
            for i, a in enumerate(arr):
                res += ((i + 1) * (n - i) + 1) // 2 * a
            return res

        return lee215()

        def fxr():
            """
            Runtime: 72 ms, faster than 64.24% of Python3 online submissions for Sum of All Odd Length Subarrays.

            XXX: presum not familiar, base-0 vs base-1?
            """

            def win(l, r):
                print(l, r)
                return P[r + 1] - P[l]

            P = [0] * (len(arr) + 1)
            print(P)
            ans = 0
            for i in range(len(arr)):
                P[i + 1] = arr[i] + P[i]

            for sz in range(1, len(arr) + 1, 2):
                for l in range(len(arr)):
                    if l + sz - 1 < len(arr):
                        ans += win(l, l + sz - 1)
            return ans

        return fxr()


sl = Solution()
print(sl.sumOddLengthSubarrays(arr=[1, 4, 2, 5, 3]))
print(sl.sumOddLengthSubarrays(arr=[1, 2]))
print(sl.sumOddLengthSubarrays(arr=[10, 11, 12]))
