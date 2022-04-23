'''
✅ GOOD LIS (Binary Search)
2111. Minimum Operations to Make the Array K-Increasing

https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/discuss/1635013/C%2B%2BPython-Longest-Non-Decreasing-Subsequence-Clean-and-Concise


To find the Longest Non-Decreasing Subsequence of an array, you can check following posts for more detail:

300. Longest Increasing Subsequence - Longest Increasing Subsequence
1964. Find the Longest Valid Obstacle Course at Each Position - Longest Non-Decreasing Subsequence

'''


from typing import List
from bisect import bisect_right


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        def fxr_dp():
            """
            TLE: 58 / 78 test cases passed.

            T: O(N^2)
            """
            m = len(obstacles)
            T = {i: 1 for i in range(m)}
            for i in range(1, m):
                for j in range(i):
                    if obstacles[j] <= obstacles[i]:
                        T[i] = max(T[i], T[j]+1)
            return list(T.values())

        def patience_sort():
            """
            Runtime: 1508 ms, faster than 96.08% of Python3 online submissions for Find the Longest Valid Obstacle Course at Each Position.

            https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/discuss/1390159/C%2B%2BPython-Same-with-Longest-Increasing-Subsequence-problem-Clean-and-Concise
            """
            m = len(obstacles)
            lis = []
            ans = [-1] * m
            for i, x in enumerate(obstacles):
                if not lis or lis[-1] <= x:
                    lis.append(x)
                    ans[i] = len(lis)
                else:
                    # Find the index of the smallest number > x
                    j = bisect_right(lis, x)
                    lis[j] = x
                    ans[i] = j + 1
            return ans

        return patience_sort()


sl = Solution()
print(sl.longestObstacleCourseAtEachPosition(obstacles=[3, 1, 5, 6, 4, 2]))
