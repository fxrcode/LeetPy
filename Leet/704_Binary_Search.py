"""
Daily Challenge (Mar 26, 2022)
tag: easy, bisect
Lookback:
- how to implement bisect_left, bisect_right
    - template w/ diff l,r,condition

https://leetcode.com/explore/learn/card/binary-search/138/background/1038/
Leetcode Explore: Binary Search - Background
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Your runtime beats 99.34 % of python3 submissions.

        [Python] Powerful Ultimate Binary Search Template. Solved many problems
        XXX: Minimize k, s.t. condition(k) is True
        https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
        https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101
        """

        def bs_left():
            """
            Runtime: 351 ms, faster than 40.96% of Python3 online submissions for Binary Search.

            lower_bound
            """
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                # BUG: if nums[mid] == target: Exact condition is the right condition to use! Since it'll lean left when match
                #       eg. [0,1] search 1 will fail!
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1

            # XXX: don't forget post-processing!
            if l < len(nums) and nums[l] == target:
                return l
            return -1

        def bs_right():
            """
            find last position of target
            zhijun_liao: The original search space is indeed [0, len(nums) - 1]. But we are returning left - 1, not left, so we need to set right = len(nums), otherwise, if we set right = len(nums) - 1, then len(nums) - 1 would never be returned, the maximum returned value is at most len(nums) - 2. That's not correct, since we don't include all possible values.
            """
            l, r = 0, len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1

            if l > 0 and nums[l - 1] == target:
                return l - 1
            else:
                return -1

        return bs_right()
        # return bs_left()


sl = Solution()
print(sl.search(nums=[-1, 0, 3, 5, 5, 5, 9, 12], target=5))
# print(sl.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
# print(sl.search(nums=[-1, 0], target=0))
# print(sl.search(nums=[-1, 0], target=4))
# print(sl.search(nums=[1], target=4))
