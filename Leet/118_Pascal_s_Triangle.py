"""
https://leetcode.com/study-plan/dynamic-programming/?progress=edfymn3
Study Plan: Dynamic Programming

https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1170/
Explore Array & String: 2D Array

tag: easy, dp

"""


from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Your runtime beats 87.38 % of python3 submissions.
        AC in 1. Used trick from ??? to append dummy 0 in both end to generalize the pre[i]+pre[i+1]
        """
        res = [[1]]

        for l in range(1, numRows):
            new_level = []
            pre = [0] + res[-1] + [0]
            for i in range(len(pre) - 1):
                new_level.append(pre[i] + pre[i + 1])
            # done this new level
            res.append(new_level)
        return res


sl = Solution()
print(sl.generate(5))
