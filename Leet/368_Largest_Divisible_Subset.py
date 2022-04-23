'''
Daily Challenge (Nov 15)
02:56:24 left
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 10: DP on String

✅ GOOD DP (LIS pattern)

XXX: Top Vote
This is the Standard LIS problem : 300. Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/
Some of its variants are : )
354. Russian Doll Envelopes - https://leetcode.com/problems/russian-doll-envelopes/
646. Maximum Length of Pair Chain - https://leetcode.com/problems/maximum-length-of-pair-chain/
1626. Best Team With No Conflicts - https://leetcode.com/problems/best-team-with-no-conflicts/
1691. Maximum Height by Stacking Cuboids - https://leetcode.com/problems/maximum-height-by-stacking-cuboids/
1909. Remove One Element to Make the Array Strictly Increasing - https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

'''

from typing import List
from functools import cache


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        def os_4loc():
            """
            Runtime: 348 ms, faster than 82.06% of Python3 online submissions for Largest Divisible Subset.

            T: O(n^2), M: O(m^2)

            """
            nums.sort()
            EDS = {-1: set()}
            for x in nums:
                # XXX: nice use max(iterable, key=lambda/builtin)
                EDS[x] = max([EDS[k] for k in EDS
                              if x % k == 0], key=len) | {x}
            return list(max(EDS.values(), key=len))

        def os_dp_itenary():
            # TODO
            pass

        def os_dp_recur():
            """
            Runtime: 368 ms, faster than 78.69% of Python3 online submissions for Largest Divisible Subset.

            T: O(N^2), M: O(N^2)
            """
            @cache
            def eds(i):
                tail = nums[i]
                max_subset = []
                # the value of eds(i) depends on its previous elements
                for p in range(i):
                    if tail % nums[p] == 0:
                        subset = eds(p)
                        if len(max_subset) < len(subset):
                            max_subset = subset
                # extend the found max subset with the current tail
                max_subset = max_subset.copy()
                max_subset.append(tail)

                return max_subset

            if len(nums) == 0:
                return []

            nums.sort()
            return max([eds(i) for i in range(len(nums))], key=len)

        def fxr():
            """
            Runtime: 372 ms, faster than 77.58% of Python3 online submissions for Largest Divisible Subset.

            AC in 3rd.
            NOTE: 30min to debug
            """
            nums.sort()
            F = [[-1, 1]] * len(nums)  # [idx of previous choose, total len]
            mx = 1
            ans = []
            global_mx = 0
            global_i = 0
            for i, n in enumerate(nums):
                if i == 0:
                    continue

                mx = 1
                for j in range(i):
                    if n % nums[j] == 0:
                        if F[j][1] + 1 > mx:
                            mx = F[j][1]+1
                            F[i] = [j, F[j][1]+1]
                            global_mx = max(global_mx, F[i][1])
                            if global_mx == F[i][1]:
                                global_i = i
            print(F)
            print(global_mx, global_i)
            x = global_i
            while x >= 0:
                ans.append(nums[x])
                x = F[x][0]

            return ans[::-1]

        def fxr_WA():
            nums.sort()
            F = [1] * len(nums)
            mx = 2
            ans = []
            cur = [nums[0]]
            for i in range(1, len(nums)):
                if nums[i] % nums[i-1] == 0:
                    F[i] = F[i-1]+1
                    cur.append(nums[i])
                    mx = max(mx, F[i])
                    if mx == F[i]:
                        ans = cur
                else:
                    cur = [nums[i]]
                    continue
            return ans

        # return fxr()
        return os_dp_recur()


sl = Solution()
# print(sl.largestDivisibleSubset(nums=[1, 2, 3, 5, 9, 15, 17, 51, 153]))
# print(sl.largestDivisibleSubset([3, 4, 16, 8]))
print(sl.largestDivisibleSubset([4, 8, 10, 240]))
