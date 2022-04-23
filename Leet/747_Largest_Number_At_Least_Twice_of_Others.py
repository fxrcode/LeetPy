'''
Explore Array & String
https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
'''


from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """
        Your runtime beats 65.71 % of python3 submissions.
        T: O(n), M: O(1)
        XXX: similar to 414. Third Maximum Number, and 628. Maximum Product of Three Numbers
        """
        v = [-1, -1]
        max_idx = 0
        for i, n in enumerate(nums):
            if n in v:
                continue
            if n > v[0]:
                v = [n, v[0]]
                max_idx = i
            elif n > v[1]:
                v = [v[0], n]
        # print(v)
        if v[0] < v[1]*2:
            max_idx = -1
        return max_idx

    def dominantIndex_fxr_1(self, nums: List[int]) -> int:
        """
        Runtime: 36 ms, faster than 65.71% of Python3 online submissions for Largest Number At Least Twice of Others.

        T: O(nlogn), M: O(2n)
        AC in 1. my actual first idea
        """
        if not nums or len(nums) == 1:
            return -0
        n2i = [(n, i) for i, n in enumerate(nums)]
        n2i.sort(key=lambda tu: tu[0])
        if n2i[-1][0] >= 2*n2i[-2][0]:
            return n2i[-1][1]
        return -1

    def dominantIndex_BUG(self, nums: List[int]) -> int:
        # BUG: red flag!!! I saw this trick in 414. Third Maximum Number, but I didn't really understand it!!!
        v = [-1, -1]  # max, second_max
        max_idx = 0
        for i, n in enumerate(nums):
            # BUG: need to check if n in v. if existed, don't do the v update since the tops won't change!
            #       eg. v=[3,2], then n = 3, it'll update v to [3,3]!
            if n > v[0]:
                # not only substitute, but also shift previous largest to second!
                v = [n, v[1]]
                max_idx = i
            elif n > v[1]:
                v = [v[0], n]
        print(v)


sl = Solution()
numss = [[3, 6, 1, 0], [1, 2, 3, 4], [1]]
for nums in numss:
    print(sl.dominantIndex(nums))
