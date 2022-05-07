"""
✅ GOOD Stack (mono)
Tag: Medium, Stack
Lookback:
- mono-stk usage
- Gongshui3ye: iterate i vs j vs k (ikj -> 132-pattern)
"""

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        def gongshui3ye():
            """
            Runtime: 469 ms, faster than 47.77% of Python3 online submissions for 132 Pattern.

            T: O(N)
            """
            stk = []
            k = -2e9
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] < k:
                    return True
                while stk and stk[-1] < nums[i]:
                    k = max(k, stk.pop())
                stk.append(nums[i])
            return False

        return gongshui3ye()

        def fuxuemingzhu():
            """
            Runtime: 454 ms, faster than 52.23% of Python3 online submissions for 132 Pattern.

            https://leetcode-cn.com/problems/132-pattern/solution/fu-xue-ming-zhu-cong-bao-li-qiu-jie-dao-eg78f/
            """
            N = len(nums)
            # minimum before index i
            leftMin = [float("inf")] * N
            for i in range(1, N):
                leftMin[i] = min(leftMin[i - 1], nums[i - 1])
            stk = []
            for j in range(N - 1, -1, -1):
                nums_k = float("-inf")
                while stk and stk[-1] < nums[j]:
                    nums_k = stk.pop()
                if leftMin[j] < nums_k:
                    return True
                stk.append(nums[j])
            return False

        return fuxuemingzhu()
        """
        def fxr_WA():
            # WA: [3,5,0,3,4] should be True: [3,5,4]
            stk = []
            for n in nums:
                while stk and stk[-1] >= n:
                    three = stk.pop()
                    if stk and stk[0] < n < three:
                        return True
                stk.append(n)
            return False
        """


sl = Solution()
print(sl.find132pattern(nums=[1, 2, 3, 4]))
print(sl.find132pattern(nums=[3, 1, 4, 2]))
print(sl.find132pattern(nums=[-1, 3, 2, 0]))
assert sl.find132pattern([3, 5, 0, 3, 4]) == True
assert sl.find132pattern([1, 0, 1, -4, -3]) == False
