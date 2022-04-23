"""
✅ GOOD Heapq
✅ GOOD Sort
tag: Medium, Sort, Heapq, Google
Lookback: 
- same as merge k sorted list
Similar:
- 378. 
[ ] REDO
"""

from heapq import heappop, heappush
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def os_pq():
            """
            Runtime: 888 ms, faster than 81.58% of Python3 online submissions for Campus Bikes.
            T: O(NMlogM)
            XXX: disguise of merge k sorted list!
            """
            worker_to_bike_list = []
            pq = []
            for i, (x, y) in enumerate(workers):
                cur_worker_pairs = []
                for j, (u, v) in enumerate(bikes):
                    d = abs(x - u) + abs(y - v)
                    cur_worker_pairs.append((d, i, j))
                # sort the worker_to_bike list for the current worker in reverse order
                cur_worker_pairs.sort(reverse=True)
                # add the closest bike for this worker to the pq
                heappush(pq, cur_worker_pairs.pop())
                # store the remaining options for the current worker in worker_to_bike_list
                worker_to_bike_list.append(cur_worker_pairs)

            result = [-1] * len(workers)
            used_bikes = set()

            while pq:
                if len(used_bikes) == len(bikes):
                    break
                d, w, b = heappop(pq)
                if b not in used_bikes:
                    used_bikes.add(b)
                    result[w] = b
                else:
                    next_closest_bike = worker_to_bike_list[w].pop()
                    heappush(pq, next_closest_bike)
            return result

        return os_pq()

        def os_sort():
            """
            Runtime: 2012 ms, faster than 20.44% of Python3 online submissions for Campus Bikes.

            REF: https://leetcode.com/problems/campus-bikes/discuss/308738/C++-bucket-sort-O(M*N)-time-and-space-solution/350163
            https://leetcode.com/problems/campus-bikes/discuss/341433/Python-simple-and-fast-solution
            T: O(mnlogmn)
            """
            # distances = [[] for _ in range(2001)]
            distances = []
            for i, (x, y) in enumerate(workers):
                for j, (u, v) in enumerate(bikes):
                    d = abs(x - u) + abs(y - v)
                    distances.append((d, i, j))

            distances.sort()

            used_bikes = set()
            result = [-1] * len(workers)
            for dist, i, j in distances:
                if len(used_bikes) == len(workers):
                    break
                # print(dist, i, j)
                if result[i] == -1 and j not in used_bikes:
                    used_bikes.add(j)
                    result[i] = j
            return result


sl = Solution()
print(sl.assignBikes(workers=[[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]))
print(sl.assignBikes(workers=[[0, 0], [1, 1], [2, 0]], bikes=[[1, 0], [2, 2], [2, 1]]))
