"""
Daily Challenge (Jan 5)
小而美的算法技巧: 差分数组

"""

from typing import List


class Difference:
    def __init__(self, nums) -> None:
        self.L = len(nums)
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]

    def incr(self, i, j, v):
        self.diff[i] += v
        if j + 1 < self.L:
            self.diff[j + 1] -= v

    def result(self):
        res = [0] * self.L
        res[0] = self.diff[0]
        for i in range(1, self.L):
            res[i] = res[i - 1] + self.diff[i]
        return res


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        def DBabichev():
            """
            Runtime: 104 ms, faster than 20.17% of Python3 online submissions for Car Pooling.

            https://leetcode.com/problems/car-pooling/discuss/857489/Python-linear-solution-using-cumulative-sums-explained
            trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11. Let us represent it in the following way:

            # # 3 3 3 3 3 # # #
            # # # # # # # 3 3 3
            # # # 8 8 8 8 8 8 8

            ||
            v

            0 0 3 0 0 0 0 -3 0 0 0
            0 0 0 0 0 0 0 3 0 0 -3
            0 0 0 8 0 0 0 0 0 0 -8

            ||
            v
            0 0 3 8 0 0 0 0 0 0 -11 -> cumulative sums -> 0 0 3 11 11 11 11 11 11 11 0
            """
            nums = [0] * 1002
            for p, f, t in trips:
                nums[f + 1] += p
                nums[t + 1] -= p
            for i in range(1, len(nums)):
                nums[i] += nums[i - 1]
                if nums[i] > capacity:
                    print(i, nums[i])
                    return False
            return True

        return DBabichev()

        def labuladong():
            """
            Runtime: 164 ms, faster than 9.55% of Python3 online submissions for Car Pooling.

            T: O(N)
            """
            nums = [0] * 1001
            df = Difference(nums)
            for v, i, j in trips:
                df.incr(i, j - 1, v)

            return capacity >= max(df.result())

        def fxr_sweep():
            """
            Runtime: 56 ms, faster than 99.22% of Python3 online submissions for Car Pooling.
            T: O(nlogn)
            M: O(n)
            """
            A = []
            for p, s, e in trips:
                A.append((s, p))
                A.append((e, -p))
            A.sort()

            carry = 0
            for t, p in A:
                carry += p
                if carry > capacity:
                    return False
            return True


sl = Solution()
print(sl.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=4))
print(sl.carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))
print(sl.carPooling([[9, 0, 1], [3, 3, 7]], 4))
print(sl.carPooling([[2, 1, 5], [3, 5, 7]], 3))
