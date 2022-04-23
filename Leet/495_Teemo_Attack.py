from typing import List


class Solution:
    def findPoisonedDuration_WRONG(self, timeSeries: List[int], duration: int) -> int:
        res = duration
        pre_l, pre_r = timeSeries[0], timeSeries[0]+duration
        for cur_l in timeSeries[1:]:
            if pre_r < cur_l:
                res += duration
            else:
                res += (cur_l - pre_l)

        return res

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """[summary]
        Runtime: 255 ms, faster than 53.69% of Python3 online submissions for Teemo
        Same idea of merge intervals
        https://leetcode.com/problems/teemo-attacking/discuss/97465/O(n)-Java-Solution-using-same-idea-of-merge-intervals
        """
        if len(timeSeries) < 1:
            return 0

        res, start, end = 0, timeSeries[0], timeSeries[0]+duration

        for i in range(1, len(timeSeries)):
            if timeSeries[i] > end:
                res += end - start
                start = timeSeries[i]  # if non-overlap, new start
            end = timeSeries[i] + duration

        res += end - start  # take care of the last interval
        return res


sl = Solution()
timeSeries = [1, 4]
duration = 2
print(sl.findPoisonedDuration(timeSeries, duration))

timeSeries = [1, 2, 3]
duration = 5
print(sl.findPoisonedDuration(timeSeries, duration))
