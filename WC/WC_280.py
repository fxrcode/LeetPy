'''
Weekly Contest #280
Feb 12, 2022
'''

from collections import Counter
from heapq import heapify
from re import I, X
from typing import List


class Solution:

    def countOperations(self, num1: int, num2: int) -> int:
        x, y = num1, num2
        ops = 0
        while (x * y) != 0:
            if x >= y:
                x = x - y
            else:
                y = y - x
            ops += 1
        return ops

    def minimumOperations(self, nums: List[int]) -> int:
        # odds, evens = 0,0
        # for i in range(2, len(nums), 2):
        #     if nums[i-2] != nums[i]:
        #         evens += 1
        # for i in range(3, len(nums), 2):
        #     if nums[i-2] != nums[i]:
        #         odds +=1
        if len(nums) == 1:
            return 0
        te, to = len(nums[::2]), len(nums[1::2])
        Ce, Co = Counter(nums[::2]), Counter(nums[1::2])
        mosto_2 = Co.most_common(2)
        moste_2 = Ce.most_common(2)
        print(moste_2, mosto_2)
        if mosto_2[0][0] != moste_2[0][0]:
            ro, re = to - mosto_2[0][1], te - moste_2[0][1]
            return ro + re
        else:
            if len(mosto_2) == len(moste_2) == 1:
                return min(mosto_2[0][1], moste_2[0][1])
            x = to - mosto_2[0][1] + (1e6 if len(moste_2) == 1 else te - moste_2[1][1])
            y = (1e6 if len(mosto_2) == 1 else to - mosto_2[1][1]) + te - moste_2[0][1]
            print(x, y)
            return min(x, y)

    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        A = beans

        # return min(sum(A[:i]) + sum(A[i:]) - (len(A) - i) * A[i] for i in range(len(A)))
        return sum(A) - max((len(A) - i) * A[i] for i in range(len(A)))
    
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        


sl = Solution()
# print(sl.countOperations(2, 3))
# print(sl.countOperations(10, 10))

# print(sl.minimumOperations(nums=[3, 1, 3, 2, 4, 3]))
# print(sl.minimumOperations(nums=[1, 2, 2, 2, 2]))
# print(sl.minimumOperations(nums=[1]))
# print(sl.minimumOperations(nums=[2, 2, 2, 2, 2]))
# print(sl.minimumOperations(nums=[4, 4, 4, 4, 2, 2, 2, 2]))

# print(sl.minimumRemoval([4, 1, 6, 5]))
# print(sl.minimumRemoval(beans=[2, 10, 3, 2]))
# print(sl.minimumRemoval(beans=[3, 3, 3, 3]))
# print(sl.minimumRemoval(beans=[1, 1, 1, 100]))
# print(sl.minimumRemoval(beans=[99, 99, 100]))
print(sl.minimumRemoval([66, 90, 47, 25, 92, 90, 76, 85, 22, 3]))  # ans:200
