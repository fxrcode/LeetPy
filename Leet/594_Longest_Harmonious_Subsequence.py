"""
tag: easy, hash
Lookback:
- always think about 1-pass in counting problems
- mirrored problem should consider unique case, don't be duplicated count.
    - 2217. Find Palindrome With Fixed Length
    - rotate image
"""

from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        def os_1pass():
            """
            Runtime: 605 ms, faster than 14.88% of Python3 online submissions for Longest Harmonious Subsequence.

            """
            C = Counter()
            mx = 0
            for n in nums:
                C[n] += 1
                if n - 1 in C:
                    mx = max(mx, C[n] + C[n - 1])
                if n + 1 in C:
                    mx = max(mx, C[n] + C[n + 1])
            return mx

        return os_1pass()

        def dbabichev():
            C = Counter(nums)
            return max((C[n] + C[n + 1] for n in C if n + 1 in C), default=0)

        return dbabichev()

        def fxr():
            """
            Runtime: 401 ms, faster than 61.64% of Python3 online submissions for Longest Harmonious Subsequence.

            """
            cnt = Counter(nums)
            mx = 0
            for n in nums:
                if n - 1 in cnt or n + 1 in cnt:
                    mx = max(mx, cnt[n - 1] + cnt[n], cnt[n + 1] + cnt[n])
            return mx

        return fxr()


sl = Solution()
assert sl.findLHS(nums=[1, 3, 2, 2, 5, 2, 3, 7]) == 5
assert sl.findLHS(nums=[1, 1, 1, 1]) == 0
