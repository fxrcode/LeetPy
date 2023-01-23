"""
tag: easy, graph
date: 01232023
Daily Challenge (Jan 2)
"""

from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        def os_2arr():
            """
            Runtime: 732 ms, faster than 67.73% of Python3 online submissions for Find the Town Judge.
            T: O(E)
            """
            cnt = [0] * (N + 1)
            for i, j in trust:
                cnt[i] -= 1
                cnt[j] += 1
            for i in range(1, N + 1):
                if cnt[i] == N - 1:
                    return i
            return -1

        return os_2arr()


sl = Solution()
print(sl.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
print(sl.findJudge(1, []))
