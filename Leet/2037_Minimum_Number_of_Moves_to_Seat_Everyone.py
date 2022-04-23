"""
tag: easy, sort
Lookback:
- simple logic => 1-to-1 mapping
"""

from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        def fxr():
            # Runtime: 106 ms, faster than 33.62% of Python3 online submissions for Minimum Number of Moves to Seat Everyone.
            nonlocal seats, students
            seats.sort()
            students.sort()
            return sum(abs(e - t) for e, t in zip(seats, students))

        return fxr()


sl = Solution()
print(sl.minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]))
assert sl.minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]) == 7
assert sl.minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]) == 4
