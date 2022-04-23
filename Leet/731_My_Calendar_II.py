"""
tag: medium, BST
Lookback:
- 253 template: sortedContainers
729
"""


from sortedcontainers import SortedDict


class MyCalendarTwo:
    """
    Runtime: 3778 ms, faster than 11.46% of Python3 online submissions for My Calendar II.

    https://leetcode.com/problems/my-calendar-ii/discuss/1536272/Python-2-solutions-Clean-and-Concise
    https://leetcode.com/problems/meeting-rooms-ii/discuss/203658/HashMapTreeMap-resolves-Scheduling-Problem
    """

    def __init__(self):
        self.delta = SortedDict()

    def book(self, start: int, end: int) -> bool:
        self.delta[start] = self.delta.setdefault(start, 0) + 1
        self.delta[end] = self.delta.setdefault(end, 0) - 1

        peak = 0
        for d in self.delta.values():
            peak += d
            if peak >= 3:
                self.delta[start] -= 1
                self.delta[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
