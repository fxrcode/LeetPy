"""
Daily Challenge (Jan 15)

✅ GOOD 2 pointer
✅ GOOD Coding Skill

https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions
"""

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        def zitaowang():
            """
            Runtime: 120 ms, faster than 98.50% of Python3 online submissions for Maximize Distance to Closest Person.

            XXX: zitao's 2 pointer idea is very clean!
            """
            prev = None
            res = 1
            for i, s in enumerate(seats):
                if s == 1:
                    # BUG: not prev means None and 0!!!
                    # if not prev:
                    if prev is None:
                        res = i
                    else:
                        dis = (i - prev) // 2
                        print(i, prev, dis)
                        res = max(res, dis)
                    prev = i
            res = max(res, len(seats) - 1 - prev)
            return res

        return zitaowang()
        """
        def fxr():
            ans = 0
            l = 0
            # if edge case 0000111 or 11100000,
            while l < len(seats):
                if seats[l] == 0:
                    ans += 1
            # now seats[l] is 1
            # general case
            for r, s in enumerate(seats, start=l+1):
                if s == 0:
                    ans = max(ans, r-l)
        """


sl = Solution()
ss = [
    # [0, 0, 0, 1],
    # [1, 1, 1, 0, 0],
    # [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1]
    [1, 0, 0, 0, 1, 0, 1]
]
for seats in ss:
    print(sl.maxDistToClosest(seats))
