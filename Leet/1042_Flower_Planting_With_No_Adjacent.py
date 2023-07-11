"""
Jingying Mock (Dec 9, 2021)
Q1

✅ GOOD Backtrack (actually NEVER backtrack due to property)
💡insight M-Coloring Problem, given constraint (M=4 and max degree = 3)

"""


from turtle import reset
from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        def os_greedy():
            """
            When you see 'relation' in problem, ring the bell of graph model! Then you'll find solution easily.
            Metacognition: I canme up with CC (dfs/UF) at first, but this problem is not CC!
                Then I coded up in backtracking, but TLE! So I know must optimize it with property, but not able to insight...

                OS: the given constraint: All gardens have at most 3 edges, so you're safe to traverse any order to plant!
                Therefore, no need of backtrack.
            """
            res = [0] * N
            G = [[] for i in range(N)]
            for x, y in paths:
                G[x - 1].append(y - 1)
                G[y - 1].append(x - 1)
            for i in range(N):
                newSet = set()
                for j in G[i]:
                    newSet.add(res[j])

                defaultSet = {1, 2, 3, 4}

                unused = defaultSet - newSet
                popedElement = min(unused)
                res[i] = popedElement
            return res

        def Master_Bruce_backtrack():
            """
            Runtime: 460 ms, faster than 52.75% of Python3 online submissions for Flower Planting With No Adjacent.

            https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/711468/JAVA-BackTracking-(but-wont-backtrack-at-all)
            JAVA [BackTracking] (but wont backtrack at all)

            XXX: As the constraints(M=4 and Max Degree=3) always guarantee an extra color to paint for any vertex, the code will not backtrack at all and will reach the solution in the first take. This is exactly why the Greedy Algorithm works for this problem.
            """
            res = [0] * N
            G = [[] for i in range(N)]
            for x, y in paths:
                G[x - 1].append(y - 1)
                G[y - 1].append(x - 1)

            def valid(u, c):
                for v in G[u]:
                    if c == res[v]:
                        return False
                return True

            def bt(u):
                if u == N:
                    return True
                for c in range(1, 4 + 1):
                    if valid(u, c):
                        res[u] = c
                        # XXX: first time seeing linear type recursion, actually still regular recursion, just neighbor = n+1
                        if bt(u + 1):
                            return True
                        res[u] = 0
                return False

            bt(0)
            return res
