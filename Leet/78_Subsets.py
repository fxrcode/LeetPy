"""
Daily Challenge (Feb 13, 2022)
tag: medium, Backtracking
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def os_backtrack():
            """
            generate power set by size order
            T: O(N*2^N)
            """

            def bt(first, cur):
                if len(cur) == k:
                    output.append(cur[:])
                    return
                for i in range(first, len(nums)):
                    bt(i + 1, cur + [nums[i]])

            output = []
            for k in range(len(nums) + 1):
                bt(0, [])
            return output

        return os_backtrack()

        def fxr_backtrack():
            """
            Runtime: 46 ms, faster than 50.10% of Python3 online submissions for Subsets.
            T: O(N*2^N)
            """

            def bt(start, path, res):
                res.append(path[:])
                for i in range(start, len(nums)):
                    bt(i + 1, path + [nums[i]], res)

            res = []
            bt(0, [], res)
            return res


sl = Solution()
print(sl.subsets(nums=[1, 2, 3]))
