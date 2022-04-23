"""
✅ GOOD presum 
✅ GOOD Hash (setdefault)
Tag: Medium, Hash
Lookback:
- First occurrance === setdefault(k,v)
"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        def fxr():
            """
            Runtime: 893 ms, faster than 97.36% of Python3 online submissions for Continuous Subarray Sum.

            https://leetcode.com/problems/continuous-subarray-sum/discuss/485589/C%2B%2BPython-Easy-and-Concise
            """
            N = len(nums)
            pre = 0
            pre_r = {0: -1}
            for i in range(N):
                pre = pre + nums[i]
                remainder = pre % k
                if i - pre_r.setdefault(remainder, i) >= 2:
                    return True
            return False

        return fxr()


sl = Solution()
print(sl.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
print(sl.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))
print(sl.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))
assert sl.checkSubarraySum([0], 1) == False
