"""
tag: Hard
Lookback:
- sweep-line + BST as in 253 (@zzhai)
"""


from sortedcontainers import SortedDict


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: "[[Interval]]") -> "[Interval]":
        def fxr():
            """
            Runtime: 222 ms, faster than 7.08% of Python3 online submissions for Employee Free Time.

            REF: https://leetcode.com/problems/employee-free-time/discuss/175081/Sweep-line-Java-with-Explanations
            https://leetcode.com/problems/meeting-rooms-ii/discuss/203658/HashMapTreeMap-resolves-Scheduling-Problem
            Sweep-line + BST
            """
            sd = SortedDict()
            for sch in schedule:
                for itv in sch:
                    s, f = itv.start, itv.end
                    sd[s] = sd.setdefault(s, 0) + 1
                    sd[f] = sd.setdefault(f, 0) - 1
            res = []
            start, score = -1, 0
            for k, v in sd.values():
                score += v
                if score == 0 and start == -1:
                    start = k
                elif start != -1 and score != 0:
                    res.append(Interval(start, k))
                    start = -1
            return res
