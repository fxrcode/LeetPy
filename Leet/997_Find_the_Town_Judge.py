"""
Daily Challenge (Jan 2)
"""

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        def os_2arr():
            """
            Runtime: 732 ms, faster than 67.73% of Python3 online submissions for Find the Town Judge.
            T: O(E)
            """
            if len(trust) < n - 1:
                return -1
            indegree = [0] * (n + 1)
            outdegree = [0] * (n + 1)
            for a, b in trust:
                outdegree[a] += 1
                indegree[b] += 1

            for i in range(1, n + 1):
                if indegree[i] == n - 1 and outdegree[i] == 0:
                    return i
            return -1

        return os_2arr()


sl = Solution()
print(sl.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
print(sl.findJudge(1, []))

