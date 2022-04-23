'''
Daily Challenge (Nov 24)
06:44:39 left
✅ GOOD Interval (intersect)

Metacognition: I came up with the direct not (not intersect) trick to get intersect result, then I directly update pointers.

Lookback: Colin Galen (wisdom?) #1: "If you can't re-solve a problem that you did before, you didn't learn enough from it"
<Candidate Master in 1 Year - This Strategy Works Amazingly> https://youtu.be/9M5voWYmie4?t=26
'''


from typing import List


class Solution:
    def intervalIntersection(self, fl: List[List[int]], sl: List[List[int]]) -> List[List[int]]:
        def os():
            f, s = 0, 0
            res = []
            while f < len(fl) and s < len(sl):
                f0, f1 = fl[f]
                s0, s1 = sl[s]
                lo = max(f0, s0)
                hi = min(f1, s1)
                if lo <= hi:
                    res.append([lo, hi])
                if f1 < s1:
                    f += 1
                else:
                    s += 1
            print(res)
            return res

        def fxr_WA():
            f, s = 0, 0
            res = []
            while f < len(fl) and s < len(sl):
                f0, f1 = fl[f]
                s0, s1 = sl[s]
                if not (f1 < s0 or s1 < f0):
                    res.append([max(s0, f0), min(s1, f1)])
                    f, s = f+1, s+1
                # BUG: no idea what's the condition for incr pointers
                elif f1 <= s0:
                    f += 1
                else:
                    s += 1

            if f < len(fl):
                print(fl[f:])
                res.append(fl[f:])
            if s < len(sl):
                print(sl[s:])
                res.append(sl[s:])

        return os()


sl = Solution()
sl.intervalIntersection(fl=[[0, 2], [5, 10], [13, 23], [24, 25]],
                        sl=[[1, 5], [8, 12], [15, 24], [25, 26]])
