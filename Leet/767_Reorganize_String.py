"""
✅ GOOD Priority Queue
Top Amazon
tag: medium, greedy, priority-queue
Lookback
- not familiar with list[(chr,freq)] vs pq, latter one is good for dynamic!
- clever use double heappop() as good candidate!
"""
from collections import Counter
from heapq import heapify, heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        def os_pq():
            """
            Runtime: 43 ms, faster than 65.99% of Python3 online submissions for Reorganize String.

            REF: https://leetcode-cn.com/problems/reorganize-string/solution/zhong-gou-zi-fu-chuan-by-leetcode-solution/
            T: O(nlog26)
            """
            pq = [(-f, c) for c, f in Counter(s).items()]
            heapify(pq)
            mx_cnt = pq[0][0]
            print(-mx_cnt)
            if -mx_cnt > (len(s) + 1) // 2:
                return ""
            res = []
            while len(pq) >= 2:
                f0, c0 = heappop(pq)
                f1, c1 = heappop(pq)
                res.append(c0)
                res.append(c1)
                f0 += 1
                f1 += 1
                if -f0 > 0:
                    heappush(pq, (f0, c0))
                if -f1 > 0:
                    heappush(pq, (f1, c1))
            if pq:
                f, c = heappop(pq)
                res.append(c)
            return "".join(res)

        return os_pq()


sl = Solution()
s = "aaabbc"
s = "aaab"
print(sl.reorganizeString(s))
