"""
tag: easy, skills
Lookback:
- similar to #942. no need to exactly mark right in 2nd place!
- same as #1629, one-pass is sufficient
"""
from collections import defaultdict
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        def lee215_1pass():
            # TODO
            pass

        def os():
            """
            Runtime: 252 ms, faster than 83.90% of Python3 online submissions for Degree of an Array.

            """
            left, right, count = {}, {}, defaultdict(int)
            for i, x in enumerate(nums):
                if x not in left:
                    left[x] = i
                right[x] = i  # this is the gem, better than me.
                count[x] += 1
            ans = len(nums)
            degree = max(count.values())
            for x in count:
                if count[x] == degree:
                    ans = min(ans, right[x] - left[x] + 1)
            return ans

        return os()

        """
        def fxr():
            # Runtime: 260 ms, faster than 78.65% of Python3 online submissions for Degree of an Array.
            P = defaultdict(lambda: [-1, -1])
            F = defaultdict(int)
            mxlen = 0
            for i, n in enumerate(nums):
                if P[n][0] == -1:
                    P[n][0] = i
                else:
                    P[n][1] = i
                F[n] += 1
                mxlen = max(mxlen, F[n])

            mnlen = len(nums)
            for n, f in F.items():
                if f == mxlen:
                    l, r = P[n]
                    mnlen = min(mnlen, r - l + 1)
            return max(1, mnlen)
        """


sl = Solution()
print(sl.findShortestSubArray([1]))
print(sl.findShortestSubArray(nums=[1, 2, 2, 3, 1]))
print(sl.findShortestSubArray(nums=[1, 2, 2, 3, 1, 4, 2]))
