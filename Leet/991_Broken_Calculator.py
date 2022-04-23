"""
✅ GOOD Logic (Backward)
tag: medium, logic
Lookback:
- Work Backwards!

Similar:
1654.
Daily Challenge (Mar 23, 2022)

"""

from collections import deque
from math import log


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        def dbabichev_greedy():
            """
            Runtime: 41 ms, faster than 60.27% of Python3 online submissions for Broken Calculator.

            T: O(logTarget)
            """

            def rec(t):
                if t == startValue:
                    return 0
                if t < startValue:
                    return startValue - t
                if t % 2 == 1:
                    return 1 + rec(t + 1)
                else:
                    return 1 + rec(t // 2)

            return rec(target)

        return dbabichev_greedy()

        """
        def fxr_WA():
            start = startValue
            ops = 0
            if target > 2 * startValue:
                ops = int(log((target - 1) // startValue, 2))
                start = pow(2, ops) * startValue
            elif target < startValue:
                return startValue - target

            q = deque([(start, ops)])
            print(q)
            seen = set([start])

            while q:
                for _ in range(len(q)):
                    cur, ops = q.popleft()
                    if cur == target:
                        return ops
                    for neig in [cur * 2, cur - 1]:
                        if neig in seen:
                            continue
                        # if abs(neig - target) > 2 * abs(cur - target):
                        #     continue
                        if neig > target:
                            q.append((target, ops + neig - target))
                        else:
                            q.append((neig, ops + 1))
                            seen.add(neig)
            return -1
        """

        return fxr()


sl = Solution()
print(sl.brokenCalc(startValue=2, target=3))
print(sl.brokenCalc(startValue=3, target=10))
print(sl.brokenCalc(startValue=1024, target=1))
print(sl.brokenCalc(startValue=1, target=1000000000))
