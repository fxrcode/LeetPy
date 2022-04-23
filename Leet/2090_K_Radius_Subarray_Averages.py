'''
Weekly Contest 269 (Nov 27, 2021)
'''

from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        if N < 2*k+1:
            return [-1]*N
        twok_1 = sum(nums[:2*k+1])
        res = [-1]*k
        nums.extend([0]*k)
        for i in range(k, N-k):
            avg = twok_1//(2*k+1)
            print(twok_1, avg)
            res.append(avg)
            if i+k+1 >= N:
                break
            twok_1 += (-nums[i-k] + nums[i+k+1])
        res.extend([-1]*k)
        return res


sl = Solution()
print(sl.getAverages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
print(sl.getAverages(nums=[100000], k=0))
