"""
✅ GOOD Greedy (heapq, use interval end)
tag: medium, heapq, greedy, sweep-line
Lookback:
- Greedy: sort start time (Princeton 4.1 Interval Partitioning proof)

Similar: 
56. Merge Intervals
57. Insert Interval (hard)
252. Meeting Rooms
253. Meeting Rooms II
729. My Calendar I
731. My Calendar II
732. My Calendar III (hard)
759. Employee Free Time (hard) 
1094. Car Pooling


https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75
"""

import heapq
from typing import List

from sortedcontainers import SortedDict


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        def os_greedy():
            """
            Runtime: 116 ms, faster than 46.38% of Python3 online submissions for Meeting Rooms II.
            """
            # stores the end time of intervals
            pq = []
            for s, f in sorted(intervals, key=lambda x: x[0]):
                if pq and s >= pq[0]:
                    # means two intervals can use the same room
                    heapq.heappushpop(pq, f)
                else:
                    # a new room is allocated
                    heapq.heappush(pq, f)
            # Q: why len here, rather check max during push/pop?
            #   ans: I pop when course with no conflict, rather course in heapq finished!
            #       so heapq will record max depth of open intervals (Def from Princeton lec)
            return len(pq)

        def chap9_sweep_line():
            """
            XXX: 使用九章算法强化班中讲到的扫描线算法
            REF: Neetcode. Why 1 for start, -1 for end? Since [3,9], [9,10] is not overlap, to break tie, We need to make end 9 before start 9.
                By given +/- 1 in the tuple, we make the sort that can break the tie correctly.
            """
            points = []
            for meet in intervals:
                points.append((meet[0], 1))
                points.append((meet[1], -1))

            meeting_rooms = 0
            ongoing_meetings = 0
            for _, delta in sorted(points):
                ongoing_meetings += delta
                meeting_rooms = max(meeting_rooms, ongoing_meetings)

            return meeting_rooms

        def zzhai_bst():
            """
            Runtime: 119 ms, faster than 43.18% of Python3 online submissions for Meeting Rooms II.

            HashMap/TreeMap resolves Scheduling Problem

            https://leetcode.com/problems/meeting-rooms-ii/discuss/203658/HashMapTreeMap-resolves-Scheduling-Problem
            """
            sd = SortedDict()
            for s, f in intervals:
                sd[s] = sd.setdefault(s, 0) + 1
                sd[f] = sd.setdefault(f, 0) - 1
            room, k = 0, 0
            for _, v in sd.items():
                room += v
                k = max(k, room)
            return k


sl = Solution()
# meetings = [[1, 4], [2, 8], [5, 7], [5, 9], [3, 4]]
meetings = [[0, 30], [5, 10], [15, 20]]
print(sl.minMeetingRooms(meetings))
