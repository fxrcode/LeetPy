"""
✅ GOOD UF!

https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3914/
Leetcode Explore Graph: Disjoint Set Union (DSU)

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

XXX: some post said it's too difficult for two coding questions in 45 min phone interview. BUt it is indeed asked in FB.
    So you have to have strategy and get prepared.
"""


from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        """
        REF: https://leetcode.com/problems/evaluate-division/discuss/270993/Python-BFS-and-UF(detailed-explanation)
        By: WangQiuc

        Augmented UF, so root[x] = (root(x), ratio)  # ratio = x/root(x)
        """
        uf = {}

        # XXX: I like her succinct naming: xr for x_ratio, pr for parent_ratio. KISS is yyds in interview.
        # xr = x/parent(x), pr = parent(x)/root(x), update xr to xr*pr = x/root(x)
        def find(x):
            # XXX: learned new API: dict.setdefault(key, defaultVal): set if key not exist. return value or defaultVal
            p, xr = uf.setdefault(x, (x, 1.0))
            if x != p:
                r, pr = find(p)
                uf[x] = (r, xr * pr)
            return uf[x]

        # if root(x) = root(y), equations "x / y" doable as (x/root(x)) / (y/root(y)) = xr / yr
        def union(x, y, ratio):
            root_x, xr = find(x)
            root_y, yr = find(y)
            # Neat!
            if not ratio:
                return xr / yr if root_x == root_y else -1.0
            if root_x != root_y:
                uf[root_x] = (root_y, yr / xr * ratio)

        # XXX: step 1. Build up UF
        for (x, y), v in zip(equations, values):
            union(x, y, v)

        # XXX: step 2. Query
        return [union(x, y, 0) if x in uf and y in uf else -1.0 for x, y in queries]

    def calcEquation_BFS():
        # TODO:
        pass


sl = Solution()
ret = sl.calcEquation(
    equations=[["a", "b"], ["b", "c"]],
    values=[2.0, 3.0],
    queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
)
print(ret)
