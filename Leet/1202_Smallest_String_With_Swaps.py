"""
✅ GOOD Graph (UF)
💡insight
tag: Medium, UF, DFS
Lookback:
- logic thinking can give 1-second proof that "equal" chars can be sort! 
    * instinct logic as in 1443. Minimum walk = 2*(n-1)
- Snippet: sort and assign group

https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3913/
Leetcode Explore Graph: Disjoint Set Union (DSU)
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
"""


from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def otoc_dfs():
            """
            Runtime: 945 ms, faster than 48.65% of Python3 online submissions for Smallest String With Swaps.

            https://leetcode.com/problems/smallest-string-with-swaps/discuss/387589/Simple-Python-DFS-solution-with-explanation
            """

            def dfs(i):
                vis.add(i)
                group.append(i)
                for j in AL[i]:
                    if j not in vis:
                        dfs(j)

            vis = set()
            n = len(s)
            AL = defaultdict(list)
            for i, j in pairs:
                AL[i].append(j)
                AL[j].append(i)
            lst = list(s)
            for i in range(n):
                if i not in vis:
                    group = []
                    dfs(i)
                    group.sort()
                    chars = [lst[k] for k in group]
                    chars.sort()
                    for i in range(len(group)):
                        lst[group[i]] = chars[i]
            return "".join(lst)

        return otoc_dfs()

        def fxr_uf():
            """
            Your runtime beats 78.30 % of python3 submissions.

            REF: https://leetcode.com/problems/smallest-string-with-swaps/discuss/387524/Short-Python-Union-find-solution-w-Explanation
            XXX: I got the blurred lemma that same group and exchange any 2. But not sure how to prove so as to use. Then I think about sort each group.
                Actually very intuitive. It's just like I want to swap things in diner with families. By swapping, any two of us can swap.
            XXX: Last step to sort group than similar to merge sort idea is cool.
            T: O(p + slogs). O(s)
            """
            pa = {i: i for i in range(len(s))}
            sz = [1] * len(s)

            def find(i):
                if pa[i] != i:
                    pa[i] = find(pa[i])
                return pa[i]

            def union(i, j):
                x, y = map(find, [i, j])
                if x == y:
                    return
                if sz[x] > sz[y]:
                    x, y = y, x
                pa[x] = y
                sz[y] += sz[x]

            def get_group() -> dict:
                """
                1. find each index's group, build a mapping: root index: list of children's char
                2. sort reversely, so we can pop to get the min and use it, so no need of iter
                """
                d = defaultdict(list)
                for i, c in enumerate(s):
                    d[find(i)].append(c)
                for root in d:
                    d[root].sort(reverse=True)

            sb = []

            # join all groups (by index)
            for i, j in pairs:
                union(i, j)
            """
            !goal: sort each group
            3loop s, for each index, find the corresponding group's min and use it.
            """
            d = get_group()
            for i in range(len(s)):
                c = d[find(i)].pop()
                sb.append(c)
            return "".join(sb)

        return fxr_uf()


sl = Solution()
print(sl.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))
print(sl.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))
print(sl.smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]))
