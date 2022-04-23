'''
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

✅ GOOD DP (1D) Kadane's Algs
'''


from functools import cache
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def os_kadane_algs():
            """
            Runtime: 905 ms, faster than 22.32% of Python3 online submissions for Maximum Subarray.

            OS: impl is neat!
            """
            cur_subarr = max_subarr = nums[0]
            for n in nums[1:]:
                cur_subarr = max(n, n+cur_subarr)
                max_subarr = max(max_subarr, cur_subarr)
            return max_subarr

        def fxr_2():
            """
            Runtime: 1201 ms, faster than 8.71% of Python3 online submissions for Maximum Subarray.

            """
            @cache
            def opt(i):
                if i == 0:
                    return nums[0]
                return max(0, opt(i-1))+nums[i]
            return max(map(opt, range(len(nums))))

        def fujiwaranoSai():
            """
            Runtime: 756 ms, faster than 40.42% of Python3 online submissions for Maximum Subarray.

            Top post: Simple DP and thoughts on DP
            T: O(N)
            REF: https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts
            """
            n = len(nums)

            # XXX: Define F[i] means maxSubArray for A[0:i ] which must has A[i] as the end element.
            #      Note F[i] is less flexible but easier find recurrence relation.
            #       so we have to keep update global optimal
            F = [0] * n
            F[0] = nums[0]
            ans = F[0]
            for i in range(1, n):
                F[i] = (F[i-1] if F[i-1] > 0 else 0) + nums[i]
                ans = max(ans, F[i])
            return ans

        def fxr_1():
            """
            Runtime: 860 ms, faster than 20.19% of Python3 online submissions for Maximum Subarray.
            2nd try, due to consecutive, I can optimize the min(presum[:j]) to O(1).
            So T: O(2N)

            TLE: 203 / 209 test cases passed.
            1st attempt, this is O(N^2) due to min(array)
            """
            N = len(nums)
            presum = [0] * (N+1)
            for i in range(N):
                presum[i+1] = presum[i] + nums[i]
            # print(presum)
            ans = -1e6
            min_j = 0
            for j in range(1, N+1):
                min_j = min(min_j, presum[j-1])
                ans = max(ans, presum[j] - min_j)
                # ans = max(ans, presum[j] - min(presum[:j]))
            return ans

        # return fxr_1()
        return fujiwaranoSai()


sl = Solution()
print(sl.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sl.maxSubArray(nums=[5, 4, -1, 7, 8]))
