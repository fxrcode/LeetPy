"""
tag: medium, mono-stk
Lookback:

To Solve 84. Largest Rectangle in Histogram, I need better understanding of mono-stack
https://www.geeksforgeeks.org/next-greater-element/
https://www.geeksforgeeks.org/next-smaller-element/
https://www.geeksforgeeks.org/previous-greater-element/
https://www.geeksforgeeks.org/find-the-nearest-smaller-numbers-on-left-side-in-an-array/

* Next Greater/Smaller element (NGE, NSE)
* Previous Greater/Smaller element (PGE, PSE)

Q: Why Stack, mono-increase vs descrease? loop normal or reverse?
"""


from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        def fxr():
            """
            Runtime: 302 ms, faster than 50.91% of Python3 online submissions for Next Greater Element II.
            AC in 1.
            """
            stk = []
            n = len(nums)
            ans = [-1] * n
            for ci in range(n * 2 - 1, -1, -1):
                i = ci % n
                while stk and nums[stk[-1]] <= nums[i]:
                    stk.pop()
                ans[i] = nums[stk[-1]] if stk else -1
                stk.append(i)
            return ans

        return fxr()


sl = Solution()
print(sl.nextGreaterElements(nums=[1, 2, 3, 4, 3]))
