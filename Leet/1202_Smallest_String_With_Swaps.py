"""
✅ GOOD Graph (UF)
💡insight

https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3913/
Leetcode Explore Graph: Disjoint Set Union (DSU)
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
tag: medium, Union-Find
Lookback:
- logic thinking can give 1-second proof that "equal" chars can be sort! 
    * instinct logic as in 1443. Minimum walk = 2*(n-1)
"""


from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """
        Your runtime beats 78.30 % of python3 submissions.

        REF: https://leetcode.com/problems/smallest-string-with-swaps/discuss/387524/Short-Python-Union-find-solution-w-Explanation
        XXX: I got the blurred lemma that same group and exchange any 2. But not sure how to prove so as to use. Then I think about sort each group.
            Actually very intuitive. It's just like I want to swap things in diner with families. By swapping, any two of us can swap.
        XXX: Last step to sort group than similar to merge sort idea is cool.
        T: O(p + slogs). O(s)
        """
        fa = {i: i for i in range(len(s))}
        rank = [0] * len(s)

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            rx, ry = map(find, [x, y])
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                fa[rx] = ry
            else:
                fa[ry] = rx
                if rank[rx] == rank[ry]:
                    rank[rx] += 1

        for a, b in pairs:
            union(a, b)

        ret = []
        d = defaultdict(list)

        for i, c in enumerate(s):
            d[find(i)].append(c)
        for root in d:
            d[root].sort(reverse=True)
        for i in range(len(s)):
            c = d[find(i)].pop()
            ret.append(c)
        return "".join(ret)


sl = Solution()
print(sl.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]))
print(sl.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))
print(sl.smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]))
