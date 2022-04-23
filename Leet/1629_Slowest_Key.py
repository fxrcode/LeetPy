"""
tag: easy, skills
Lookback:
- similar to #697. One-pass is sufficient!
"""

from collections import defaultdict
from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        def hiepit_1pass():
            ansKey = keysPressed[0]
            ansDuration = releaseTimes[0]
            for i in range(1, len(keysPressed)):
                key = keysPressed[i]
                duration = releaseTimes[i] - releaseTimes[i - 1]
                if duration > ansDuration or duration == ansDuration and key > ansKey:
                    ansKey = key
                    ansDuration = duration
            return ansKey

        return hiepit_1pass()

        def fxr():
            """
            Runtime: 89 ms, faster than 40.86% of Python3 online submissions for Slowest Key.

            T: O(nlogn)
            2-pass!
            """
            c2d = defaultdict(int)
            prev = 0
            mxdur = 0
            for t, c in zip(releaseTimes, keysPressed):
                dura = t - prev
                mxdur = max(mxdur, dura)
                prev = t
                c2d[c] = max(c2d[c], dura)
            for c in sorted(keysPressed, reverse=True):
                if c2d[c] == mxdur:
                    return c


sl = Solution()
assert sl.slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd") == "c"
assert sl.slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda") == "a"
