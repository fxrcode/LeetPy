'''
✅ GOOD Hash (Counter)
tag: medium, hash

Lookback:
- Do Smart, not simulation!
'''

from collections import Counter
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def lee215():
            """
            https://leetcode.com/problems/friends-of-appropriate-ages/discuss/127029/C%2B%2BJavaPython-Easy-and-Straight-Forward
            Runtime: 501 ms, faster than 59.49% of Python3 online submissions for Friends Of Appropriate Ages.

            T: 0(N^2)
            """
            def req(a, b):
                return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)

            c = Counter(ages)
            return sum(c[a] * (c[b] - (a == b)) for a in c for b in c
                       if req(a, b))

        return lee215()

        def fxr():
            """
            TLE: 73 / 89 test cases passed.

            T: O(N^2)
            """
            reqs = set()
            for x in range(len(ages)):
                for y in range(len(ages)):
                    if x == y:
                        continue
                    a, b = ages[x], ages[y]
                    if (x, y) in reqs:  # or (b, a) in reqs:
                        continue

                    if not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100):
                        reqs.add((x, y))
            print(reqs)
            return len(reqs)


sl = Solution()
print(sl.numFriendRequests(ages=[16, 16]))
print(sl.numFriendRequests(ages=[20, 30, 100, 110, 120]))
