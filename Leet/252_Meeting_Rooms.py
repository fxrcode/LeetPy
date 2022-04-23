"""
tag: easy, sort, interval
Lookback:
- all interval schedule can be solved by TreeMap: https://leetcode.com/problems/meeting-rooms-ii/discuss/203658/HashMapTreeMap-resolves-Scheduling-Problem
- compare 253, latter is interval partitioning, Greedy: sort by start time.

https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75
"""

from typing import List

from sortedcontainers import SortedDict


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def fxr():
            """
            Runtime: 131 ms, faster than 27.62% of Python3 online submissions for Meeting Rooms.

            Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
            Tag: interval

            Similar: 56. Merge Intervals
            """
            intervals.sort(key=lambda x: (x[0], -x[1]))
            for prev, cur in zip(intervals, intervals[1:]):
                # BUG: equal is allowed
                if prev[1] > cur[0]:
                    return False
            return True

        def zzhai_bst():
            """
            Runtime: 117 ms, faster than 41.12% of Python3 online submissions for Meeting Rooms.

            HashMap/TreeMap resolves Scheduling Problem

            https://leetcode.com/problems/meeting-rooms-ii/discuss/203658/HashMapTreeMap-resolves-Scheduling-Problem
            """
            sd = SortedDict()
            for s, f in intervals:
                sd[s] = sd.setdefault(s, 0) + 1
                sd[f] = sd.setdefault(f, 0) - 1
            room = 0
            for _, v in sd.items():
                room += v
                if room > 1:
                    return False
            return True


sl = Solution()
meetings = [[0, 30], [5, 10], [15, 20]]
print(sl.canAttendMeetings(meetings))
meetings = [[7, 10], [2, 4]]
print(sl.canAttendMeetings(meetings))
