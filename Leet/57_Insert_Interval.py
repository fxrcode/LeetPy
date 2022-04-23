"""
Tag: Medium, Interval
Lookback:
- intervals 3 types: 1288, 56, 986
- crystal clear logic, auto handle initial.
https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def pochmann():
            """
            Runtime: 72 ms, faster than 96.86% of Python3 online submissions for Insert Interval.

            XXX: careful on append vs extend!
                append a list to list[list]
                extend a list[list] to list[list]
            """
            s, e = newInterval
            left, right = [], []
            for itv in intervals:
                if itv[1] < s:
                    left.append(itv)
                elif itv[0] > e:
                    right.append(itv)
                else:
                    s = min(itv[0], s)
                    e = max(itv[1], e)
            # print(left, [s, e], right)
            left.append([s, e])
            left.extend(right)
            return left

        def fxr():
            """
            Runtime: 80 ms, faster than 77.24% of Python3 online submissions for Insert Interval.

            Not bug free in 1.
            Over-engineered: helper func defined ahead has limited my mindset!
            """

            def overlap(i1, i2):
                if i1[1] < i2[0] or i1[0] > i2[1]:
                    return False
                return True

            def merge(i1, i2):
                # assume overlap
                return [min(i1[0], i2[0]), max(i1[1], i2[1])]

            ans = []
            merged = newInterval
            for i, intv in enumerate(intervals):
                if overlap(intv, newInterval):
                    # ans.append(merge(intv, newInterval))
                    merged = merge(intv, merged)

                elif newInterval[0] > intv[1]:
                    ans.append(intv)
                    continue
                elif newInterval[1] < intv[0]:
                    if merged:
                        ans.append(merged)
                        merged = None
                    ans.extend(intervals[i:])
                    break
            if merged:
                ans.append(merged)
            return ans

        # return fxr()
        return pochmann()


sl = Solution()
print(sl.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]))
