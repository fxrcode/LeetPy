'''
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

'''


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def os():
            """
            Runtime: 52 ms, faster than 86.34% of Python3 online submissions for Maximum Product Subarray.

            XXX: understand the logic of tmp_mx, and why not another tmp for mn_so_far
            """
            if len(nums) == 0:
                return 0
            mx_so_far = nums[0]
            mn_so_far = nums[0]
            ans = mx_so_far
            for i in range(1, len(nums)):
                cur = nums[i]
                tmp_mx = max(cur, cur*mx_so_far, cur*mn_so_far)
                mn_so_far = min(cur, cur*mx_so_far, cur*mn_so_far)
                mx_so_far = tmp_mx
                ans = max(ans, mx_so_far)
            return ans

        def fxr():
            """
            Runtime: 64 ms, faster than 46.47% of Python3 online submissions for Maximum Product Subarray.

            AC in 1st
            """
            INF = 1e6
            N = len(nums)
            # F = [[-INF, INF] for _ in range(N)]
            F = [[-INF, INF] for _ in range(2)]
            F[0] = [nums[0], nums[0]]
            ans = nums[0]
            for i in range(1, N):
                # if nums[i] >= 0:
                #     F[i] = (F[i-1] if F[i-1] >= 0 else 1) * nums[i]
                # else:
                #     F[i] = (F[i-1] if F[i-1] <= 0 else 1) * nums[i]
                # ans = max(ans, F[i])
                mn, mx = F[(i-1) % 2]
                prods = [mn*nums[i], mx*nums[i]]
                include = prods + [nums[i]]
                F[i % 2] = [min(include), max(include)]
                ans = max(ans, *F[i % 2])
            return ans

        return fxr()


sl = Solution()
print(sl.maxProduct(nums=[2, 3, -2, 4]))
print(sl.maxProduct(nums=[-2, 0, -1]))
print(sl.maxProduct(nums=[-2, 4, -1]))
print(sl.maxProduct([-2]))
