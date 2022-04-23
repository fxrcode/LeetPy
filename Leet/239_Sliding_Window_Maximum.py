"""
tag: Hard, Deque
Lookback:
- classic usage of mono-deque
- used in 1696. Jump Game VI
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def dbabichev():
            """
            https://leetcode.com/problems/sliding-window-maximum/discuss/871317/Clear-thinking-process-with-PICTURE-brute-force-to-mono-deque-pythonjavajavascript
            Runtime: 1708 ms, faster than 93.64% of Python3 online submissions for Sliding Window Maximum.

            """
            deq, n, ans = deque(), len(nums), []

            for i in range(n):
                while deq and nums[i] >= nums[deq[-1]]:
                    deq.pop()
                deq.append(i)
                while deq and deq[0] <= i - k:
                    deq.popleft()
                if i >= k - 1:
                    ans.append(nums[deq[0]])
            return ans

        return dbabichev()


sl = Solution()
print(sl.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
print(sl.maxSlidingWindow(nums=[1], k=1))
