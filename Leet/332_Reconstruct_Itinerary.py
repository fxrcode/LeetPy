"""
✅ GOOD Graph (Eulerian Path)
💡insight

Tag: Medium,
Lookback:
- graph path problem

https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3901/
Leetcode Explore Graph: DFS
"""


from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List


class Solution:
    def findItinerary_Hierholzer(self, tickets: List[List[str]]) -> List[str]:
        """
        Runtime: 95 ms, faster than 50.60% of Python3 online submissions for Reconstruct Itinerary.

        XXX: OS II: Hierholzer's algorithm. Also learned from WilliamFiset's pov & example for `subtour`
        The OS explain is so good, give more insights into the algorithms, so I fully understand it:
        step 1: DFS from cur node, until we stuck with no unvisited (aka removed from pq)
        """

        def bt(G, res: deque[int], cur: str) -> None:
            # XXX: when no choice to make, regular backtrack requires this update sol step, but here we don't need
            # NOOPS

            # BUG: why I got IndexError: index out of range by using len loop?
            # qlen = len(G[cur])
            # for _ in range(qlen):

            while G[cur]:
                neig = heappop(G[cur])
                bt(G, res, neig)
            res.appendleft(cur)

        G = defaultdict(list)
        for s, e in tickets:
            heappush(G[s], e)
        res = deque()

        bt(G, res, "JFK")
        return list(res)

    def findItinerary_bt(self, tickets: List[List[str]]) -> List[str]:
        """
        Runtime: 130 ms, faster than 21.85% of Python3 online submissions for Reconstruct Itinerary.

        Official solution I: Backtracking + Greedy strategy
        XXX: Q: how to mark visited flights? Ans: use bitmap since G's value is sorted!
        Q: when do we stop? A: when all flights visited once and only once: by counting routes. Notice the #routes === #tickets + 1.
            Think about word break: there's a break between any two destination, so we have T tickets/flights, then T+1 destinations!
            eg. JFK -> ANU -> JFK -> EZE->...
                    F       F      F
        """
        G = defaultdict(list)
        # Edges = set()
        visitedMap = defaultdict(list)
        for s, e in tickets:
            G[s].append(e)
            # Edges.add((s, e))

        for s, dests in G.items():
            dests.sort()
            # XXX: since there're duplicate edges, how to mark edge visited? So we use index.
            visitedMap[s] = [False] * len(dests)

        def bt(cur, routes, res):
            if len(routes) == len(tickets) + 1:
                res.append(routes[:])
                return True
            for i, neig in enumerate(G[cur]):
                if not visitedMap[cur][i]:
                    visitedMap[cur][i] = True
                    if bt(neig, routes + [neig], res):
                        return True
                    visitedMap[cur][i] = False
            return False

        res = []
        bt("JFK", ["JFK"], res)
        return res[0]

        """
        BUG: flights may contains duplicate: this TSP has 2 same flights in diff time (TIA, ANU)

        defaultdict(int,
            {('EZE', 'AXA'): 1,
             ('TIA', 'ANU'): 2,
             ('ANU', 'JFK'): 1,
             ('JFK', 'ANU'): 1,
             ('ANU', 'EZE'): 1,
             ('AXA', 'TIA'): 1,
             ('TIA', 'JFK'): 1,
             ('ANU', 'TIA'): 1,
             ('JFK', 'TIA'): 1})

        def bt(cur, egs, path, res):
            print(f'bt: {egs} \n\t{path}')
            if len(egs) == len(Edges):
                res.append(path[:])
                return True
            for neig in sorted(G[cur]):
                e = (cur, neig)
                if e in egs:
                    continue
                egs.add(e)
                if bt(neig, egs, path+[neig], res):
                    return True
                egs.remove(e)
            return False
        res = []
        bt('JFK', set(), ['JFK'], res)
        return res[0]
        """

    '''
    def findItinerary_fxr_WA(self, tickets: List[List[str]]) -> List[str]:
        """
        BUG: Totally misunderstood the problem!
        tickets = [["JFK","SFO"],["JFK","ATL"],[
            "SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

        Output: ["JFK","ATL","SFO","SFO"]
        Expect: ["JFK","ATL","JFK","SFO","ATL","SFO"]
        """
        G = defaultdict(list)
        STOPS = set()
        for s, e in tickets:
            G[s].append(e)
            STOPS.add(s)
            STOPS.add(e)

        def dfs(cur, visited, path):
            print('dfs', id(path), path)
            if len(path) == len(STOPS):
                return
            # if cur in visited:
            #     return False
            visited.add(cur)
            for neig in sorted(G[cur]):
                if neig in visited:
                    continue
                path.append(neig)
                dfs(neig, visited, path)

                # BUG: dfs(neig, visited, path+[neig], res)
                #  classical bug, everytime list+[xx], you got a new list! Visualize in pythontutor

        path = ['JFK']
        print(id(path), path)
        dfs('JFK', set(path), path)
        return path
    '''


sl = Solution()
print(
    sl.findItinerary_Hierholzer(
        tickets=[
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ]
    )
)

# print(sl.findItinerary_Hierholzer([["EZE", "AXA"], ["TIA", "ANU"], ["ANU", "JFK"], ["JFK", "ANU"], [
#       "ANU", "EZE"], ["TIA", "ANU"], ["AXA", "TIA"], ["TIA", "JFK"], ["ANU", "TIA"], ["JFK", "TIA"]]))
