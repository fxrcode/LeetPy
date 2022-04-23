'''
每日一题打卡群 (12/1/2021)

REF:
https://docs.google.com/presentation/d/1r4uWF4SkO8jQlZkqnJ57ZWP2p-T-OOZh8_jMCotYsPI/edit#slide=id.p
https://www.bilibili.com/video/BV17z4y1y7tS?from=search&seid=8486234178848924416
'''
from typing import AnyStr, List
from functools import cache


class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        def fxr_mono():
            """
            Runtime: 785 ms, faster than 18.92% of Python3 online submissions for Number of Valid Subarrays.

            XXX: mono-stack
            T: O(N)
            """
            stk = []
            nse = [0] * len(nums)
            ans = 0
            for i in range(len(nums)-1, -1, -1):
                while stk and nums[stk[-1]] >= nums[i]:
                    stk.pop()
                nse[i] = len(nums) if not stk else stk[-1]
                ans += nse[i] - i
                stk.append(i)
            return ans

        def fxr_bf():
            """
            Runtime: 6976 ms, faster than 9.46% of Python3 online submissions for Number of Valid Subarrays.

            T: O(N^2)
            """
            ans = 0
            for i in range(len(nums)):
                cur = 0
                for j in range(i, len(nums)):
                    if nums[i] <= nums[j]:
                        cur += 1
                    else:
                        break
                print(nums[i], cur)
                ans += cur
            return ans

        # return fxr_bf()
        return fxr_mono()


sl = Solution()
print(sl.validSubarrays(nums=[1, 4, 2, 5, 3]))
# print(sl.validSubarrays(nums=[3, 2, 1]))
