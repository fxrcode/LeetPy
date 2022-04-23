'''
https://leetcode.com/explore/featured/card/graph/618/disjoint-set/3845/
Leetcode Explore Graph: Disjoint Set

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

TODO: As 济公学院 says, there's no problems in Leetcode can be solved in UF only. It can always be solved by BFS/DFS.
'''


from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Your runtime beats 94.51 % of python3 submissions.

        REF: https://leetcode.com/problems/number-of-provinces/discuss/152441/Python-Union-Find-solution

        """
        n = len(isConnected)
        # union find: init bi-directional mapping of object to array. In impl, we dict is neat
        uf = {i: i for i in range(n)}

        def find(x) -> int:
            """
            Three loc: path compression in find
            """
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        # In implementation, we don't necessory create a dedicate UF class, implement find/union/connected/rank[], etc.
        #   eg. in here, we just need to implement find. And just `run` union once when traverse right upper cornor of Matrix!
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    # uf[find(i)] = find(j)
                    # set y parent to x
                    uf[find(j)] = find(i)

        print(uf)

        # XXX: here what I got confused in begin. By traverse the matrix to union. Notice in quick union with path compression
        #  in find, it might still skew. And uf[] is parent array, not root! To get root, you always need find(x)
        #  However, we just need to count # of group, so # of roots!
        return sum(i == root for i, root in uf.items())


class UF:
    def __init__(self, size) -> None:
        self.root = {i: i for i in range(size)}

    def find(self, x) -> int:
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y) -> None:
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.root[ry] = rx
        print(self.root)


uf = UF(4)
uf.union(0, 1)
uf.union(2, 0)
uf.union(3, 1)
# uf.union(1, 3)
