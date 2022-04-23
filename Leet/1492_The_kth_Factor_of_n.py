"""
tag: medium, heapq, Amazon
Lookback:
- min-k => max-heap; max-k => min heap
"""


from heapq import heappop, heappush


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        def os_mx_heap():
            """
            Runtime: 28 ms, faster than 96.30% of Python3 online submissions for The kth Factor of n.

            """

            def heappush_k(n):
                heappush(heap, -n)
                if len(heap) > k:
                    heappop(heap)

            heap = []
            for x in range(1, int(n**0.5) + 1):
                if n % x == 0:
                    heappush_k(x)
                    if x != n // x:
                        heappush_k(n // x)
            return -heappop(heap) if k == len(heap) else -1

        def os_brute():
            kk = k
            for x in range(1, n // 2 + 1):
                if n % x == 0:
                    kk -= 1
                    if kk == 0:
                        return x
            return n if k == 1 else -1
