'''
💡insight (logic & sliding-window)
Amazon Top50
tag: Medium, Sliding Window
'''

from collections import Counter
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def lee215_sliding():
            """
            Runtime: 1361 ms, faster than 23.62% of Python3 online submissions for Count Number of Nice Subarrays.

            similar: 1248. exactly(K) = atMost(K) - atMost(K-1)
            T: O(N)
            """
            def atMost(K):
                res, l, r = 0, 0, 0
                o = 0
                while r < len(nums):
                    c = nums[r]
                    if c & 1: o += 1
                    r += 1
                    while o > K:
                        d = nums[l]
                        if d & 1: o -= 1
                        l += 1
                    res += r - l + 1
                return res

            return atMost(k) - atMost(k - 1)

        return lee215_sliding()

        def subarr_sum_k():
            """
            Runtime: 1012 ms, faster than 50.30% of Python3 online submissions for Count Number of Nice Subarrays.

            replace even=>0, odd=>1, then problem reduced to the #subarrays with sum k.

            https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC++Python-Sliding-Window-O(1)-Space/797992
            eg. say k = 3, then we check [3,0], [4,1], [5,2], ...

            XXX: but this is not general as lee215's formula
            """
            runsum, ans = 0, 0
            sumdict = {0: 1}
            for n in nums:
                runsum += n % 2
                if runsum - k in sumdict:
                    ans += sumdict[runsum - k]
                sumdict[runsum] = sumdict.get(runsum, 0) + 1
            return ans


sl = Solution()
print(sl.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3))
print(sl.numberOfSubarrays(nums=[2, 4, 6], k=1))
print(sl.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))
