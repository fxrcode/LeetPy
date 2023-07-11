"""
Daily Challenge (Jan 5)
小而美的算法技巧: 差分数组

"""

from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        def labuladong():
            """
            Runtime: 1415 ms, faster than 8.52% of Python3 online submissions for Corporate Flight Bookings.

            T: O(#bookings + n)
            """
            res = [0] * n
            for f, l, s in bookings:
                f, l = f - 1, l - 1
                res[f] += s
                if l + 1 < n:
                    res[l + 1] -= s

            for i in range(1, n):
                res[i] += res[i - 1]

            return res

        return labuladong()


sl = Solution()
print(sl.corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
