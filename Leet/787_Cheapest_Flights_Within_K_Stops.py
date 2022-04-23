'''
✅ GOOD Dijkstra/Bellman-Ford SSSP

https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3866/
Leetcode Explore Graph: SSSP

TODO: Dijkstra, BFS. Check OS
'''


from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        REF: https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaC%2B%2BPython-Priority-Queue-Solution-(TLE-now)

        bwv988: Some explanation.
        Because there could be routes which their length is shorter but pass more stops, and those routes don't
        necessarily constitute the best route in the end. To deal with this, rather than maintain the optimal
        routes with 0..K stops for each node, the solution simply put all possible routes into the priority queue,
        so that all of them has a chance to be processed. IMO, this is the most brilliant part.
        """
        f = defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]  # (dist, node, stops)
        while heap:
            p, i, k = heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heappush(heap, (p + f[i][j], j, k - 1))
        return -1

    def findCheapestPrice_dijkstra_OS(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the adjacency matrix
        AL = defaultdict(dict)
        for s, d, w in flights:
            AL[s][d] = w

        # Shortest distances array
        dist = [float("inf") for _ in range(n)]
        current_stops = [float("inf") for _ in range(n)]
        dist[src], current_stops[src] = 0, 0

        # Data is (cost, stops, node)
        minHeap = [(0, 0, src)]

        while minHeap:

            cost, stops, node = heappop(minHeap)

            # If destination is reached, return the cost to get here
            if node == dst:
                print(dist)
                return cost

            # XXX: If there are no more steps left, continue
            if stops == k + 1:
                continue

            # BUG: Never use/modify code before fully understand its logic!
            # if cost > distances[node]:
            #     continue

            for v in AL[node]:
                # XXX: naming clearly is yyds
                dU, dV, wUV = cost, dist[v], AL[node][v]
                # Better cost?
                if dU + wUV < dV:
                    dist[v] = dU + wUV
                    heappush(minHeap, (dU + wUV, stops + 1, v))
                elif stops < current_stops[v]:
                    #  Better steps?
                    heappush(minHeap, (dU + wUV, stops + 1, v))

                current_stops[v] = stops

        print('\t', dist)
        return -1 if dist[dst] == float("inf") else dist[dst]

    def findCheapestPrice_bfs(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pass

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        Runtime: 330 ms, faster than 21.58% of Python3 online submissions for Cheapest Flights Within K Stops.
        REF: https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115596/c%2B%2B-8-line-bellman-ford
        T: O(KE)
        """
        INF = 1e9
        dist = [INF] * n
        dist[src] = 0
        for i in range(k+1):
            next = dist[:]
            for u, v, w in flights:
                next[v] = min(next[v], dist[u]+w)
            dist = next

        if dist[dst] == INF:
            return -1
        return dist[dst]

        '''
        # CP4: why not working?
        G = defaultdict(list)
        for u, v, p in flights:
            G[u].append((v, p))

        # for i in range(n-1):
        for i in range(k+1):
            modified = False
            for u in range(n):
                if dist[u] != INF:
                    for v, p in G[u]:
                        if dist[u] + p >= dist[v]:
                            continue
                        dist[v] = dist[u] + p
                        modified = True
            if not modified:
                break
        '''


sl = Solution()
print(sl.findCheapestPrice_dijkstra_OS(n=3,
                                       flights=[[0, 1, 100], [1, 2, 100], [
                                           0, 2, 500]], src=0, dst=2, k=1))
print(sl.findCheapestPrice_dijkstra_OS(n=3, flights=[
      [0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))

print(sl.findCheapestPrice_dijkstra_OS(n=4, flights=[[0, 1, 1], [
      0, 2, 5], [1, 2, 1], [2, 3, 1]], src=0, dst=3, k=1))

print(sl.findCheapestPrice_dijkstra_OS(13, [[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8], [0, 12, 54], [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64], [6, 3, 88], [8, 5, 80], [11, 10, 91], [10, 0, 60], [8, 7, 92], [12, 6, 78], [6, 2, 8], [4, 3, 54], [3, 11, 76], [3, 12, 23], [11, 6, 79], [6, 12, 36], [2, 11, 100], [2, 5, 49], [7, 0, 17], [5, 8, 95], [3, 9, 98], [8, 10, 61], [
      2, 12, 38], [5, 7, 58], [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7], [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90], [0, 5, 43], [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94], [2, 7, 38], [3, 7, 88], [9, 12, 20], [12, 0, 26], [10, 5, 38], [12, 8, 50], [0, 2, 77], [11, 0, 13], [9, 10, 76], [2, 6, 67], [5, 6, 34], [9, 7, 62], [5, 3, 67]], 10, 1, 10))
