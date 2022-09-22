"""
Tag: Medium,
Lookback:
- VISUALIZATION so as to get clear logic.
- Actually the impl still has gem: unify logic rather blindly translate 4 cases as me...
"""

from typing import List


class Solution:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        def mengmamax():
            """
            This can be done by a linear scan without all the conditions, which is error-prone and tedious.
            We can process every interval in a uniform way. Just append the two intervals if not empty.
            """
            ans = []
            ta, tb = toBeRemoved
            for a, b in intervals:
                if (t := min(b, ta)) > a:
                    ans.append([a, t])
                if (t := max(a, tb)) < b:
                    ans.append([t, b])
            return ans

        def fxr_WA():
            """
            Notice: interval is [a,b), how to handle tangent edge?
            WA: [[0, 100]], [0, 50] => [0,0], [50,100]
            """
            res = []
            for iv in intervals:
                if iv[1] <= toBeRemoved[0] or iv[0] >= toBeRemoved[1]:
                    res.append(iv)
                elif toBeRemoved[0] <= iv[0] and iv[1] <= toBeRemoved[1]:
                    pass
                elif iv[0] <= toBeRemoved[0] and toBeRemoved[1] <= iv[1]:
                    res.append([iv[0], toBeRemoved[0]])
                    res.append([toBeRemoved[1], iv[1]])
                elif iv[0] <= toBeRemoved[0] <= iv[1] <= toBeRemoved[1]:
                    res.append([iv[0], toBeRemoved[0]])
                elif toBeRemoved[0] <= iv[0] <= toBeRemoved[1] <= iv[1]:
                    res.append([toBeRemoved[1], iv[1]])
            return res

        return fxr_WA()


sl = Solution()
print(sl.removeInterval(intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]))
print(sl.removeInterval(intervals=[[0, 5]], toBeRemoved=[2, 3]))
print(
    sl.removeInterval(
        intervals=[[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], toBeRemoved=[-1, 4]
    )
)
print(sl.removeInterval([[0, 100]], [0, 50]))
