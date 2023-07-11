"""
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
leetcode explore: Array 101. Conclusion
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

* similar: 628. Maximum Product of Three Numbers

"""


from heapq import heappop, heappush, heappushpop
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        Your runtime beats 90.16 % of python3 submissions.

        https://leetcode.com/problems/third-maximum-number/discuss/90207/Intuitive-and-Short-Python-solution
        Extended version of staging WWE (find max value)

        CS Dojo: <5 Problem Solving Tips for Cracking Coding Interview Questions>
        Tip #1: Come up with a brute-force solution - 1:23
        Tip #2: Think of a simpler version of the problem - 2:34
        Tip #3: Think with simpler examples -> try noticing a pattern - 5:54
        Tip #4: Use some visualization - 10:10
        Tip #5: Test your solution on a few examples - 15:09
        """
        # 1st max, 2nd max, 3rd max
        v = [float("-inf")] * 3
        for n in nums:
            # diff from 628. Maximum Product of Three Numbers, which don't need to check if n in v
            if n in v:
                continue

            if n > v[0]:
                v = [n, v[0], v[1]]
            elif n > v[1]:
                v = [v[0], n, v[1]]
            elif n > v[2]:
                v = [v[0], v[1], n]
        if float("-inf") in v:
            return max(nums)
        else:
            return v[2]

    def thirdMax_minpq(self, nums: List[int]) -> int:
        """
        Your runtime beats 75.41 % of python3 submissions.

        XXX: Classic usage of bounded pq as 9chap taught
        We maintain size-3 minpq (note: the nature order is increasing, so pq's top is minimum, so default pq is minheap in all PL)
        after len(pq) = 3, whenever we encounter a new item, just check if exists, if not, we compare the item with pq[0] (min), it the item
            is greater than pq[0], then we heappushpop(item).
            The loop invariant is: we use size-3 minheap to keep the largest 3 items
        T: O(N * log3) M: O(3)
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        pq = []
        for n in nums:
            if len(pq) < 3 and n not in pq:
                heappush(pq, n)
            else:
                if n > pq[0] and n not in pq:
                    heappushpop(n)
        if len(pq) >= 3:
            return pq[0]
        while len(pq) > 1:
            heappop(pq)
        return pq[0]

    def thirdMax_fxr(self, nums: List[int]) -> int:
        """
        AC in 1st try: Brute-force solution
        """
        tmp = sorted(set(nums), reverse=True)
        if len(tmp) < 3:
            return tmp[0]
        return tmp[3 - 1]


sl = Solution()
nn = [[3, 2, 1], [1, 2], [2, 2, 3, 1], [1, 1, 2]]
for nums in nn:
    print(sl.thirdMax_minpq(nums))
