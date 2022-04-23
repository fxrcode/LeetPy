"""
tag: medium, hash
Lookback:
- like word break (spart matrix)
"""

from collections import Counter
from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        def ye15():
            """
            Runtime: 38 ms, faster than 95.64% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.

            """
            freq = Counter(nums)
            ans = 0
            for k, v in freq.items():
                if target.startswith(k):
                    suffix = target[len(k) :]
                    ans += v * freq[suffix]
                    if k == suffix:
                        ans -= freq[suffix]
            return ans

        def fxr():
            """
            Runtime: 55 ms, faster than 80.13% of Python3 online submissions for Number of Pairs of Strings With Concatenation Equal to Target.
            T: O(N), M: O(N)
            """
            C = Counter(nums)
            res = 0
            for b in range(len(target)):
                x, y = target[:b], target[b:]
                if x == y:
                    res += C[x] * (C[x] - 1)
                else:
                    res += C[x] * C[y]
            return res

        return fxr()


sl = Solution()
print(sl.numOfPairs(nums=["777", "7", "77", "77"], target="7777"))
print(sl.numOfPairs(nums=["123", "4", "12", "34"], target="1234"))
print(sl.numOfPairs(nums=["1", "1", "1"], target="11"))
