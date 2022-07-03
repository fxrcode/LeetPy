"""
✅ GOOD DP (1D definition)
Tag: Medium, DP
Lookback:
- Study Plan: Dynamic Programming
- 1st. notice the different of DP table definition compare to regular 1D DP (in common 1D DP, T[i] must ends with nums[i])
        max up wiggle (end of up) using first i-elements, end at a certain position (no neccesory nums[i])!!!
- 2nd. when you can't extend the length, you inherit from up[i-1]
"""


from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def os_greedy():
            """
            https://leetcode.com/problems/wiggle-subsequence/solution/204874
            For the greedy approach, in brief:
            Another way to put it is to count all changes of direction (all peaks and valleys) and return that count +1:
            """
            mxlen, sign = 0, 0
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1] and sign != -1:  # peak
                    sign = -1
                    mxlen += 1
                elif nums[i] > nums[i - 1] and sign != 1:  # valley
                    sign = 1
                    mxlen += 1
            return mxlen + 1

        return os_greedy()

        def os_linear():
            """
            leetcode-cn has better OS and high-vote:
            https://leetcode-cn.com/problems/wiggle-subsequence/solution/dong-tai-gui-hua-by-cheungq-6-yhvj/
                Using 1 exxample to find recurrence relation, no need theory proof for DP formula as in OS
                However, theory proof is good to study.


            Runtime: 32 ms, faster than 86.02% of Python3 online submissions for Wiggle Subsequence.
            Memory Usage: 14.1 MB, less than 97.87% of Python3 online submissions for Wiggle Subsequence.

            T: O(N), M: O(N)
            """
            N = len(nums)

            up = [1] * N
            down = [1] * N
            for i in range(1, N):
                if nums[i - 1] < nums[i]:
                    up[i] = down[i - 1] + 1
                    down[i] = down[i - 1]
                elif nums[i - 1] > nums[i]:
                    down[i] = up[i - 1] + 1
                    up[i] = up[i - 1]
                else:
                    up[i] = up[i - 1]
                    down[i] = down[i - 1]
            return max(up[N - 1], down[N - 1])

        def fxr_LIS():
            """
            Runtime: 188 ms, faster than 13.20% of Python3 online submissions for Wiggle Subsequence.

            # T[i] is the len of wiggle subsequence end with nums[i]
            # 0: down, 1: up to nums[i]
            # T[i][0] = for all T[k][1] k < i and nums[i] > nums[k]
            # T[i][1] = for all T[k][0] k < i and nums[i] < nums[k]

            T: O(N^2)
            """
            N = len(nums)
            # if N < 3:
            #     return N
            T = [[1] * 2 for _ in range(N)]
            for i in range(1, N):
                mx_T_j_0, mx_T_j_1 = 1, 1
                for j in range(i):
                    if nums[j] > nums[i]:
                        mx_T_j_0 = max(mx_T_j_0, T[j][1] + 1)
                    elif nums[j] < nums[i]:
                        mx_T_j_1 = max(mx_T_j_1, T[j][0] + 1)
                T[i][0] = mx_T_j_0
                T[i][1] = mx_T_j_1
            print(T)
            return max(T[N - 1])

        # return fxr_LIS()
        return os_linear()


sl = Solution()
print(sl.wiggleMaxLength(nums=[1, 7, 4, 9, 2, 5]))
print(sl.wiggleMaxLength(nums=[1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))
print(sl.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(sl.wiggleMaxLength([0]))
print(sl.wiggleMaxLength([1, 1]))
