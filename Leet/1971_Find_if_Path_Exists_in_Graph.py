"""
tag: UF
✅ GOOD Graph DFS

https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3893/
Leetcode Explore Graph: DFS
https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3894/
Leetcode Explore Graph: BFS

Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

TODO: connectivity should instinct to UF.
"""


from collections import defaultdict, deque
from typing import List


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                root_x, root_y = root_y, root_x
            # Modify the root of the smaller group as the root of the
            # larger group, also increment the size of the larger group.
            self.rank[root_y] += self.rank[root_x]
            self.root[root_x] = root_y


class Solution:
    def validPath_UF(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a, b)

        return uf.find(source) == uf.find(destination)

    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        """
        Your runtime beats 73.72 % of python3 submissions.

        """
        G = defaultdict(set)
        for v, w in edges:
            G[v].add(w)
            # BUG: forgot to add both direction edge into G...
            G[w].add(v)

        def bfs(v):
            q = deque([v])
            visited = set([v])

            while q:
                qlen = len(q)
                for _ in range(qlen):
                    cur = q.popleft()
                    if cur == end:
                        return True
                    for neig in G[cur]:
                        if neig not in visited:
                            q.append(neig)
                            # after push into q, also update visited
                            visited.add(neig)
            return False

        def dfs(v, visited) -> bool:
            """
            Runtime: 2942 ms, faster than 17.55% of Python3 online submissions for Find if Path Exists in Graph.

            XXX: for explicit graph, just use DFS rather Backtracking.
            T: O(V+E), M: O(V+E)
            """
            if v == end:
                return True
            # process curr node
            visited.add(v)
            for neig in G[v]:
                if neig in visited:
                    continue
                if dfs(neig, visited):  # speedup via early termination
                    return True
            return False

        # return dfs(start, set())
        return bfs(start)

        '''
        def bt(v, path, visited):
            """
            1st try: TLE.  12 / 25 test cases passed.
            XXX: Why bt TLE? because it backtrack and un-choose!

            End is not in B's subgraph, So the bt(B) will un-choose B, and then try start's another neigh: C.
            However, unlike other backtrack problems (subsets/permutations/etc), there's link between chooses!
            So C will recursive on B's subgraph although there's no End there. Therefore it wastes so much time.

            eg.
                 start
              /    |    \
             B  -  C  - End
            /     /
            X..  Y...

            XXX: The key is the un-choose, will undo the visited set, so in the end, the visited is empty in backtracking,
            while the visited in DFS is all marked with DFS's routes.
            """
            if v == end:
                return True
            for neig in g[v]:
                if neig in visited:
                    continue
                visited.add(neig)
                if bt(neig, path+[neig], visited):
                    return True
                visited.remove(neig)
            return False
        '''

        """
        # build graph
        g = defaultdict(set)
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
            if end in g[start]:
                return True
        return bt(start, [start], set([start]))
        """


sl = Solution()
print(sl.validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], start=0, end=2))
print(sl.validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], start=0, end=5))
print(
    sl.validPath(
        100,
        [
            [3, 12],
            [26, 84],
            [10, 43],
            [68, 47],
            [33, 10],
            [87, 35],
            [41, 96],
            [70, 92],
            [38, 31],
            [88, 59],
            [7, 30],
            [89, 26],
            [95, 25],
            [66, 28],
            [14, 24],
            [86, 11],
            [83, 65],
            [14, 4],
            [67, 7],
            [89, 45],
            [52, 73],
            [47, 85],
            [86, 53],
            [68, 81],
            [43, 68],
            [87, 78],
            [94, 49],
            [70, 21],
            [11, 82],
            [60, 93],
            [22, 32],
            [69, 99],
            [7, 1],
            [41, 46],
            [73, 94],
            [98, 52],
            [68, 0],
            [69, 89],
            [37, 72],
            [25, 50],
            [72, 78],
            [96, 60],
            [73, 95],
            [7, 69],
            [97, 19],
            [46, 75],
            [8, 38],
            [19, 36],
            [64, 41],
            [61, 78],
            [97, 14],
            [54, 28],
            [6, 18],
            [25, 32],
            [34, 77],
            [58, 60],
            [17, 63],
            [98, 87],
            [13, 76],
            [58, 53],
            [81, 74],
            [29, 6],
            [37, 5],
            [65, 63],
            [89, 56],
            [61, 18],
            [23, 34],
            [76, 29],
            [73, 76],
            [11, 63],
            [98, 0],
            [54, 14],
            [63, 7],
            [87, 32],
            [79, 57],
            [72, 0],
            [94, 16],
            [85, 16],
            [12, 91],
            [14, 17],
            [30, 45],
            [42, 41],
            [82, 69],
            [24, 28],
            [31, 59],
            [11, 88],
            [41, 89],
            [48, 12],
            [92, 76],
            [84, 64],
            [19, 64],
            [21, 32],
            [30, 19],
            [47, 43],
            [45, 27],
            [31, 17],
            [53, 36],
            [88, 3],
            [83, 7],
            [27, 48],
            [13, 6],
            [14, 40],
            [90, 28],
            [80, 85],
            [29, 79],
            [10, 50],
            [56, 86],
            [82, 88],
            [11, 99],
            [37, 55],
            [62, 2],
            [55, 92],
            [51, 53],
            [9, 40],
            [65, 97],
            [25, 57],
            [7, 96],
            [86, 1],
            [39, 93],
            [45, 86],
            [40, 90],
            [58, 75],
            [99, 86],
            [82, 45],
            [5, 81],
            [89, 91],
            [15, 83],
            [93, 38],
            [3, 93],
            [71, 28],
            [11, 97],
            [74, 47],
            [64, 96],
            [88, 96],
            [4, 99],
            [88, 26],
            [0, 55],
            [36, 75],
            [26, 24],
            [84, 88],
            [58, 40],
            [77, 72],
            [58, 48],
            [50, 92],
            [62, 68],
            [70, 49],
            [41, 71],
            [68, 6],
            [64, 91],
            [50, 81],
            [35, 44],
            [91, 48],
            [21, 37],
            [62, 98],
            [64, 26],
            [63, 51],
            [77, 55],
            [25, 13],
            [60, 41],
            [87, 79],
            [75, 17],
            [61, 95],
            [30, 82],
            [47, 79],
            [28, 7],
            [92, 95],
            [91, 59],
            [94, 85],
            [24, 65],
            [91, 31],
            [3, 9],
            [59, 58],
            [70, 43],
            [95, 13],
            [30, 96],
            [51, 9],
            [16, 70],
            [29, 94],
            [37, 22],
            [35, 79],
            [14, 90],
            [75, 9],
            [2, 57],
            [81, 80],
            [61, 87],
            [69, 88],
            [98, 79],
            [18, 70],
            [82, 19],
            [36, 27],
            [49, 62],
            [67, 75],
            [62, 77],
            [83, 96],
            [92, 37],
            [95, 22],
            [46, 97],
            [35, 0],
            [44, 79],
            [82, 89],
            [68, 94],
            [96, 31],
            [92, 34],
            [25, 0],
            [46, 36],
            [38, 84],
            [21, 0],
            [0, 80],
            [72, 44],
            [56, 97],
            [86, 26],
            [94, 57],
            [25, 6],
            [81, 13],
            [66, 63],
            [57, 5],
            [72, 49],
            [46, 86],
            [95, 16],
            [95, 37],
            [14, 89],
            [44, 22],
            [60, 39],
            [37, 47],
            [58, 86],
            [89, 96],
            [38, 83],
            [51, 91],
            [72, 70],
            [14, 82],
            [60, 30],
            [58, 39],
            [57, 22],
            [95, 70],
            [44, 76],
            [5, 68],
            [15, 69],
            [33, 61],
            [81, 32],
            [21, 68],
            [73, 20],
            [22, 72],
            [83, 8],
            [15, 54],
            [93, 42],
            [68, 95],
            [55, 72],
            [33, 92],
            [5, 49],
            [17, 96],
            [44, 77],
            [24, 53],
            [2, 98],
            [33, 81],
            [32, 43],
            [20, 16],
            [67, 84],
            [98, 35],
            [58, 11],
            [72, 5],
            [3, 59],
            [78, 79],
            [6, 0],
            [26, 71],
            [96, 97],
            [18, 92],
            [1, 36],
            [78, 0],
            [63, 15],
            [20, 43],
            [32, 73],
            [37, 76],
            [73, 16],
            [76, 23],
            [50, 44],
            [68, 2],
            [14, 86],
            [69, 65],
            [95, 98],
            [53, 64],
            [6, 76],
            [7, 11],
            [14, 84],
            [62, 50],
            [83, 58],
            [78, 92],
            [37, 0],
            [13, 55],
            [12, 86],
            [11, 59],
            [41, 86],
            [27, 26],
            [94, 43],
            [20, 78],
            [0, 73],
            [58, 90],
            [69, 36],
            [62, 34],
            [65, 26],
            [32, 85],
        ],
        20,
        53,
    )
)
print(
    sl.validPath_UF(
        10,
        [
            [0, 7],
            [0, 8],
            [6, 1],
            [2, 0],
            [0, 4],
            [5, 8],
            [4, 7],
            [1, 3],
            [3, 5],
            [6, 5],
        ],
        7,
        5,
    )
)
