'''
tag: Medium, Greedy, Sorting
'''

from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        def lee215_greedy():
            count = sorted(c - r for c,r in zip(capacity, rocks))[::-1]
            x = additionalRocks
            while count and x and count[-1] <= x:
                x -= count.pop()
            return len(rocks) - len(count)

        return lee215_greedy()

sl = Solution()
print(sl.maximumBags(capacity = [2,3,4,5], rocks = [1,2,4,4], additionalRocks = 2))
print(sl.maximumBags(capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100))
