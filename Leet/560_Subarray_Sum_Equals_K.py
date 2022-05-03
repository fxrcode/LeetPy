"""
Tag: Medium, prefix-sum, hash
Lookback:
- running state, similar idea as in #1371

https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions
Similar:
437. Path Sum III's OS : Prefix Sum technique介绍的入门题
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        def lee215():
            """
            Runtime: 312 ms, faster than 57.13% of Python3 online submissions for Subarray Sum Equals K.

            https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation/105608

            """
            cnt, cur, res = {0: 1}, 0, 0
            for x in nums:
                cur += x
                res += cnt.get(cur - k, 0)
                cnt[cur] = cnt.get(cur, 0) + 1
            return res

        return lee215()

        def fxr():
            """
            Your runtime beats 68.05 % of python3 submissions.

            REF: https://leetcode.com/problems/path-sum-iii/solution/
            As a prerequisite for 437. Path Sum III's prefix-sum.
            """
            cnt, cur_sum = 0, 0
            d = defaultdict(int)

            for n in nums:
                cur_sum += n
                # situation 1: subarray from beginning
                if cur_sum == k:
                    cnt += 1

                # situation 2: subarray in the middle of array, rather start from beginning
                cnt += d[cur_sum - k]

                # add the current sum
                d[cur_sum] += 1
            return cnt


sl = Solution()
print(sl.subarraySum(nums=[1, 1, 1], k=2))
print(sl.subarraySum(nums=[1, 2, 3], k=3))
