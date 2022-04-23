"""
tag: medium, sweep-line, BST
Lookback:
- 253 template
"""

from sortedcontainers import SortedList


class MyCalendar:
    """
    Runtime: 582 ms, faster than 37.64% of Python3 online submissions for My Calendar I.

    https://leetcode.com/problems/my-calendar-i/discuss/1646158/Python-O(n-*-log-n)-using-SortedList
    T: O(logn)
    """

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        def __overlap(e1, e2) -> bool:
            if e1[1] <= e2[0] or e1[0] >= e2[1]:
                return False
            return True

        event = (start, end)
        i = self.calendar.bisect_left(event)

        n = len(self.calendar)
        # similar to closest item in sorted list
        if (i < n and __overlap(event, self.calendar[i])) or (i > 0 and __overlap(event, self.calendar[i - 1])):
            return False
        self.calendar.add(event)
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
assert obj.book(10, 20) == True
assert obj.book(15, 25) == False
assert obj.book(20, 30) == True
