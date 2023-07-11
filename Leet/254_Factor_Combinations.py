"""
https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 15: Memoization

TODO: DP
"""


from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def eigenvec(n):
            """
            Runtime: 92 ms, faster than 85.91% of Python3 online submissions for Factor Combinations.

            XXX: beautiful implemtation!
            https://leetcode.com/problems/factor-combinations/discuss/172675/python3-solution-beat-100
            """

            def bt(start, target, path, res):
                if len(path) > 0:
                    res.append(path + [target])
                    # XXX: no return here, since we add all valid path! Draw the recursion tree to understand path+[target]
                    # res.append(path[:])
                    # return
                # control the choices range!
                for i in range(start, int(target**0.5) + 1):
                    if target % i == 0:
                        path.append(i)
                        bt(i, target // i, path, res)
                        path.pop()

            res = []
            bt(2, n, [], res)
            return res

        return eigenvec(n)


sl = Solution()
print(sl.getFactors(n=32))
