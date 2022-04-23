"""
✅ GOOD bisect (k-th min/max/freq) in set.
💡insight
tag: medium, bisect
Lookback:
- Daily Challenge (Nov 15)
- 济公学院: https://www.youtube.com/watch?v=DD8RD7tx6V4
similar: 
- 774
"""
from collections import deque
from heapq import heapify, heappop, heappush


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def os_bisect():
            """
            Runtime: 1076 ms, faster than 33.80% of Python3 online submissions for Kth Smallest Number in Multiplication Table.

            ✅ 济公学院: https://www.youtube.com/watch?v=DD8RD7tx6V4
            XXX: this is not hard if you really understand generic binary search and pattern
            * k-th xxx (max/min/freq) in set => Given constant X, search if exists subset that total number of (v<=X) >= k.

            XXX: this reduce the origin search space to mono-space: FFFTTT. So we can use binary search to find the 1st T!
            """

            def enough(X):
                # x is
                count = 0
                for i in range(1, m + 1):
                    if X // i == 0:
                        break
                    count += min(X // i, n)
                return count >= k

            l, r = 1, m * n
            while l < r:
                mid = (l + r) // 2
                if enough(mid):
                    r = mid
                else:
                    l = mid + 1
            return l

        def os_next_heap():
            """
            XXX: Good use of heap as k-merge, the heapq element (val,root) is COOL

            """
            heap = [(i, i) for i in range(1, m + 1)]
            heapify(heap)

            for _ in range(k):
                val, root = heappop(heap)
                nxt = root + val
                if nxt <= root * n:
                    heappush(heap, (nxt, root))
            return val

        def os_brute_sort():
            """
            M: O(m*n), T: O(m*n log(m*n))
            Since m,n = 4*10^4. so m*n is 10^9 => TLE
            """
            tbl = [i * j for i in range(1, m + 1) for j in range(1, n + 1)]
            tbl.sort()
            return tbl[k - 1]

        def fxr_WA():
            """
            WA: 5x5, 12th should be 6!

            metacognition:
            1. BFS + sort q, since maxlen of q = diagnol = max(m,n), so O(m*n + mlogm)
            2. sorted, kth => quick select?
            """
            seen = set((0, 0))
            q = deque([(0, 0)])
            nonlocal k
            while q:
                qlen = len(q)
                for _ in range(qlen):
                    x, y = q.popleft()
                    k -= 1
                    if k == 0:
                        print(x, y)
                        return (x + 1) * (y + 1)
                    if y + 1 < n and (x, y + 1) not in seen:
                        seen.add((x, y + 1))
                        q.append((x, y + 1))
                    if x + 1 < m and (x + 1, y) not in seen:
                        seen.add((x + 1, y))
                        q.append((x + 1, y))
                qq = deque(sorted(list(q), key=lambda tu: (tu[0] + 1) * (tu[1] + 1)))
                q = qq
            return -1
