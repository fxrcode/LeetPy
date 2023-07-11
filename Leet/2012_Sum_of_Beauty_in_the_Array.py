"""
Jingying Mock (Dec 7, 2021)
"""


from typing import List

INF = 1e6


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        def rock_premxmn():
            """
            Runtime: 1301 ms, faster than 35.67% of Python3 online submissions for Sum of Beauty in the Array.

            https://leetcode.com/problems/sum-of-beauty-in-the-array/discuss/1471979/JavaPython-3-O(n)-code%3A-running-maxmin-from-left-and-right-w-brief-explanation-and-analysis.

            Similar indexing as presum labuladong: left_mx[i]: max in nums[0...i-1]
            XXX: learned tilde python indexing, handy in reverse looping! ~0=-1, ~1=-2, ...
            """
            n, sm = len(nums), 0
            left_mx = [0] + [0] * n
            right_mn = [0] * n + [INF]
            for i, num in enumerate(nums):
                left_mx[i + 1] = max(left_mx[i], num)
                # Tilde Python indexing is COOOL
                right_mn[~i - 1] = min(right_mn[~i], nums[~i])
            for i in range(1, len(nums) - 1):
                # BUG: if left_mx[i] < nums[i] < right_mn[i]:
                #   careful, suffix right_mn[i] means minimum nums[i...-1], not same as left_mx[i]!
                if left_mx[i] < nums[i] < right_mn[i + 1]:
                    sm += 2
                elif nums[i - 1] < nums[i] < nums[i + 1]:
                    sm += 1
            return sm
