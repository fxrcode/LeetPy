"""
Daily Challenge (Nov 29)

💡✅ GOOD DFS, UF

Lookback
- You can get answer only if you ask the correct Question (Modeling is important!)

Similar Tagged Problems : :
399. Evaluate Division - https://leetcode.com/problems/evaluate-division/
839. Similar String Groups - https://leetcode.com/problems/similar-string-groups/
928. Minimize Malware Spread II - https://leetcode.com/problems/minimize-malware-spread-ii/
1202. Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/
1559. Detect Cycles in 2D Grid - https://leetcode.com/problems/detect-cycles-in-2d-grid/
"""
from collections import defaultdict
from typing import List

"""
class UF:
    def __init__(self, n) -> None:
        self.f = {i: i for i in range(n)}

    def find(self, x):
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        fx, fy = map(self.find, [x, y])
        if fx == fy:
            return fx
        self.f[fy] = fx
        return fx
"""


class UF:
    def __init__(self, n) -> None:
        self.f = {i: i for i in range(n)}
        self.ranks = [0] * n
        self.sizes = [1] * n

    def find(self, x):
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, a, b):
        x, y = map(self.find, [a, b])
        if x == y:
            return x
        if self.ranks[x] > self.ranks[y]:
            x, y = y, x
        self.f[x] = y
        self.sizes[y] += self.sizes[x]
        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        return y


"""
# algs DPV
def dfs(u):
    visited.add(u)
    for v in AL[u]:
        if v not in visited:
            dfs(v)
"""


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def os_cc():
            """
            Runtime: 200 ms, faster than 80.96% of Python3 online submissions for Accounts Merge.

            XXX: When you see connectivity -> Graph CC: DFS or UF.
            济公学院: Every problems can be solved by UF, can always be solved by BFS/DFS as well.
            """

            def dfs(comp, u):
                """
                1st time CC using dfs
                """
                seen.add(u)
                comp.append(u)
                for v in AL[u]:
                    if v not in seen:
                        dfs(comp, v)

            AL = defaultdict(list)
            seen = set()
            merged = []

            # build AL (star model, so first_email as root, and K-1 edges for each sub-graph)
            # 1st time: unpack w/ star
            for a, *e in accounts:
                fir_email = e[0]
                rest_emails = e[1:]
                AL[fir_email].extend(rest_emails)
                [AL[e].append(fir_email) for e in rest_emails]

            # Traverse over all th accounts to store components
            ans = []
            for name, *e in accounts:
                fir = e[0]
                if fir in seen:
                    continue
                merged = []
                dfs(merged, fir)
                merged.sort()
                ans.append([name] + merged)
            return ans

        def fxr_uf():
            """
            Runtime: 216 ms, faster than 61.40% of Python3 online submissions for Accounts Merge.

            AC in 1 (30min coding)
            Metacognition:
                1. Need to find overlap of emails to detect same account, so I want to use UF
                2. #id as the usual UF node, and common email is the edge to union #id.
                3. To get common email, I built e2p (email to ppl id). Then loop through to union ids based on common email
                4. I built p2e based on UF to get emails belong to real account
                5. To build result, I loop through p2e and sorted emails.

            T: O(N), M: O(N)

            """
            n = len(accounts)
            dsu = UF(n)
            e2p = defaultdict(list)
            for i in range(n):
                for e in accounts[i][1:]:
                    e2p[e].append(i)
            print(e2p)
            for e, se in e2p.items():
                for j in range(len(se) - 1):
                    dsu.union(se[j], se[j + 1])
            p2e = defaultdict(set)
            for k in range(n):
                root = dsu.find(k)
                for e in accounts[k][1:]:
                    p2e[root].add(e)
            print(p2e)
            res = []
            for r, e in p2e.items():
                res.append([accounts[r][0]] + sorted(list(e)))
            return res

        # return fxr_uf()
        return os_cc()


sl = Solution()
print(
    sl.accountsMerge(
        accounts=[
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["John", "johnsmith@mail.com", "john00@mail.com"],
            ["Mary", "mary@mail.com"],
            ["John", "johnnybravo@mail.com"],
        ]
    )
)
