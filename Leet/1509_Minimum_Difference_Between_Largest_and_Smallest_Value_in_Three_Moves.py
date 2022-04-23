"""
tag: Medium, Logic
Lookback:
- piecewise analysis CRUX: cover all cases!
Similar: 
910. Smallest Range I/II
821. Shortest Distance to a Character
1838. Frequency of the Most Frequent Element
"""

from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        def lee215():
            """
            https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/discuss/730567/JavaC%2B%2BPython-Straight-Forward

            Runtime: 344 ms, faster than 97.99% of Python3 online submissions for Minimum Difference Between Largest and Smallest Value in Three Moves.
            XXX: missed (1,2), (2,1) combination until WA
            """
            if len(nums) < 4:
                return 0
            nums.sort()
            # kill 3 smallest
            fir3 = nums[-1] - nums[3]
            # kill 3 biggest
            las3 = nums[-4] - nums[0]
            # kill 2 biggest + 1 smallest
            fir1las2 = nums[-3] - nums[1]
            # kill 1 biggest + 2 smallest
            fir2las1 = nums[-2] - nums[2]

            return min(fir3, las3, fir1las2, fir2las1)

        return lee215()


sl = Solution()
print(sl.minDifference(nums=[5, 3, 2, 4]))
print(sl.minDifference(nums=[1, 5, 0, 10, 14]))
print(sl.minDifference(nums=[2, 3, 100, 1000, 10000]))
print(sl.minDifference(nums=[1, 100, 1000, 10000, 10001]))
print(sl.minDifference([82, 81, 95, 75, 20]))
