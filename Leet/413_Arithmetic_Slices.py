"""
Daily Challenge (Mar 2, 2022)
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming
tag: medium, logic
"""


from functools import cache
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        def os_math():
            """
            Runtime: 32 ms, faster than 98.00% of Python3 online submissions for Arithmetic Slices.

            T: O(N)
            """
            cnt, tot = 0, 0
            A.append(2e9)
            for i in range(2, len(A)):
                if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                    cnt += 1
                else:
                    tot += cnt * (cnt + 1) // 2
                    cnt = 0
            return tot

        def os_rec():
            """
            Runtime: 88 ms, faster than 5.54% of Python3 online submissions for Arithmetic Slices.

            T: O(N)
            """

            @cache
            def arith(i):
                """
                # of arithmetic slices in prefix nums[0...i]
                """
                if i < 2:
                    return 0
                if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                    return 1 + arith(i - 1)
                else:
                    return 0

            return sum(arith(i) for i in range(2, len(A)))

        def fxr_dp():
            """
            Runtime: 36 ms, faster than 82.73% of Python3 online submissions for Arithmetic Slices.

            AC in 1! Now I found the useful to think about brute-force first, since it brings me some insights of specific property!
            """
            n = len(A)
            if n < 3:
                return 0
            F = [0] * n  # cnt arithmetic slices end with nums[i]
            if A[0] - A[1] == A[1] - A[2]:
                F[2] = 1
            for i in range(3, n):
                if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                    F[i] = F[i - 1] + 1

            print(F)
            return sum(F)

        def fxr_brute():
            """
            Runtime: 40 ms, faster than 59.09% of Python3 online submissions for Arithmetic Slices.

            XXX: basic coding skill, must be bug-free!
            T: O(N^2)
            """
            cnt = 0
            n = len(A)
            for s in range(n - 2):
                # XXX: how to init var correctly?
                dif = A[s + 1] - A[s]
                # BUG: for j, w in enumerate(nums, start=i+1):
                #   start means count from i+1, not iterate from nums[i+1]!!!
                for e in range(s + 2, n):
                    if dif == A[e] - A[e - 1]:
                        cnt += 1
                    else:
                        break
            return cnt

        # return fxr_brute()
        return fxr_dp()
        # return os_rec()


sl = Solution()
print(sl.numberOfArithmeticSlices([1, 2, 3, 4]))
print(sl.numberOfArithmeticSlices([1, 2, 3, 8, 9, 10]))
