"""
💡✅ GOOD Logic
tag: sort, Kevin, FB, Greedy
Lookback:

[ ] REDO
"""

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def os():
            """
            Runtime: 175 ms, faster than 30.78% of Python3 online submissions for Queue Reconstruction by Height.

            Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
            T: O(NlogN)
            """
            people.sort(key=lambda x: (-x[0], x[1]))
            ans = []
            for p in people:
                ans.insert(p[1], p)
            return ans

        return os()

        def ye15_otherway():
            """
            @ye15： If we go the other direction (in Python 3),

            https://leetcode.com/problems/queue-reconstruction-by-height/discuss/89359/Explanation-of-the-neat-Sort+Insert-solution/569092
            """
            people.sort(key=lambda x: (x[0], -x[1]))
            ans = [None] * len(people)
            idx = list(range(len(people)))

            for p in people:
                ans[idx.pop(p[1])] = p
            return ans


sl = Solution()
print(sl.reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
