"""
Daily Challenge (Nov 23)
01:26:14 left

✅ GOOD UF, Prime-decompose

NOTE: Problems based on the intuition of Union and Find (basically always labelled as Hard) :
803. Bricks Falling When Hit - https://leetcode.com/problems/bricks-falling-when-hit/
947. Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
990. Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/
1579. Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/
1627. Graph Connectivity With Threshold - https://leetcode.com/problems/graph-connectivity-with-threshold/
1697. Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
1722. Minimize Hamming Distance After Swap Operations - https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/
1998. GCD Sort of an Array - https://leetcode.com/problems/gcd-sort-of-an-array/
2076. Process Restricted Friend Requests - https://leetcode.com/problems/process-restricted-friend-requests/
"""


import math
from collections import defaultdict
from typing import List


class UF:
    def __init__(self, n) -> None:
        self.p = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n

    def find(self, i) -> int:
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, i, j) -> int:
        x, y = map(self.find, [i, j])
        if x == y:
            return y
        if self.ranks[x] > self.ranks[y]:
            x, y = y, x
        self.p[x] = y
        if self.ranks[x] == self.ranks[y]:
            self.ranks[y] += 1
        self.sizes[y] += self.sizes[x]
        return y

    def setSize(self, i):
        return self.sizes[self.find(i)]


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def os_prime_factors():
            """
            Runtime: 9061 ms, faster than 5.08% of Python3 online submissions for Largest Component Size by Common Factor.

            XXX: OS optimized UF with primes factors!
                Took me 1hr to understand to logic of union adjacent prime factors, and the 1-to-1 relation: num -> prime_factor -> group_id

            """
            dsu = UF(max(nums) + 1)
            num_factor_map = {}

            def primefactors(n):
                d = 2
                primes = set()
                while n >= d**2:
                    if n % d == 0:
                        n //= d
                        primes.add(d)
                    else:
                        d += 1
                primes.add(n)
                return list(primes)

            for n in nums:
                factors = primefactors(n)
                num_factor_map[n] = factors[0]
                for i in range(len(factors) - 1):
                    dsu.union(factors[i], factors[i + 1])

            mx = 0
            group_cnt = defaultdict(int)
            for n in nums:
                group_id = dsu.find(num_factor_map[n])
                group_cnt[group_id] += 1
                mx = max(mx, group_cnt[group_id])
            return mx

        def rishabh_devbanshi_1():
            def recur(node, mp, vis):
                vis.add(node)
                for v in mp[node]:
                    if v not in vis:
                        recur(v, mp, vis)

            def dfs(mp):
                res, prev = 0, 0
                vis = set()
                for k, v in mp.items():
                    if k not in vis:
                        recur(k, mp, vis)

                    l = len(vis) - prev
                    res = max(l, res)
                    prev = len(vis)
                return res

            mp = defaultdict(list)
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if math.gcd(nums[i], nums[j]) > 1:
                        mp[nums[i]].append(nums[j])
                        mp[nums[j]].append(nums[i])
            return dfs(mp)

        def ans_dfs():
            """
            Runtime: 3389 ms, faster than 67.26% of Python3 online submissions for Largest Component Size by Common Factor.
            Memory Usage: 43.1 MB, less than 8.93% of Python3 online submissions for Largest Component Size by Common Factor.
            """
            from time import time

            dt = time()

            n = len(nums)
            edges = {}

            prime_i_node = {}
            # print(num_primes)

            def primeFactors(n):  # Prime factor decomposition
                out = set()
                while n % 2 == 0:
                    out.add(2)
                    n //= 2
                for i in range(3, int(n**0.5) + 1, 2):
                    if n % i == 0:
                        out.add(i)
                    while n % i == 0:
                        # out.add(i)
                        n //= i
                if n > 2:
                    out.add(n)
                return out

            def find_edges():
                for i, num in enumerate(nums):
                    # fac_pms = get_prime_fac(num)
                    fac_pms = primeFactors(num)
                    for fac in fac_pms:
                        if fac not in prime_i_node:
                            prime_i_node[fac] = []
                        prime_i_node[fac].append(i)
                # print(prime_i_node)
                print("time:", (time() - dt) * 1000)
                for prime, inodes in prime_i_node.items():
                    if len(inodes) <= 1:
                        continue
                    for i in range(len(inodes)):
                        if inodes[i] not in edges:
                            edges[inodes[i]] = set()
                        edges[inodes[i]].add(inodes[(i + 1) % len(inodes)])

            def dfs(i, visited):
                if i in visited:
                    return 0
                res = 1
                visited.add(i)
                for i_nx in edges.get(i, []):
                    if i_nx not in visited:
                        res += dfs(i_nx, visited)
                return res

            find_edges()
            # print("time:", (time() - dt)*1000)
            # print(edges)
            sz_max = 0
            visited = set()
            for i in range(n):
                if i not in visited:
                    sz = dfs(i, visited)
                    sz_max = max(sz_max, sz)

            # print("time:", (time() - dt)*1000)

            return sz_max

        def fxr_uf():
            """
            Runtime: 4147 ms, faster than 39.88% of Python3 online submissions for Largest Component Size by Common Factor.
            Memory Usage: 276.8 MB, less than 5.36% of Python3 online submissions for Largest Component Size by Common Factor.
            """
            nums.sort()
            print(nums)
            # uf = {v: v for v in nums}
            # rank = {v: 0 for v in nums}
            uf = {v: v for v in range(1, max(nums) + 1)}
            rank = {v: 0 for v in range(1, max(nums) + 1)}

            def find(x):
                # BUG: while x != uf[x]:
                if x != uf[x]:
                    uf[x] = find(uf[x])
                return uf[x]

            def union(x, y):
                fx, fy = map(find, [x, y])
                # if fx != fy:
                #     uf[fy] = fx
                if fx == fy:
                    return
                if rank[fx] < rank[fy]:
                    uf[fx] = fy
                else:
                    uf[fy] = fx
                    if rank[fx] == rank[fy]:
                        rank[fx] += 1

            def common(x, y):
                if x > y:
                    return common(y, x)
                for v in range(2, x + 1):
                    if x % v + y % v == 0:
                        return v
                return 0

            def primeDecompose(num):
                """decompose any positive number into
                    a series of prime factors.
                e.g. 12 = 2 * 2 * 3
                """
                factor = 2
                prime_factors = []
                while num >= factor * factor:
                    if num % factor == 0:
                        prime_factors.append(factor)
                        num = num // factor
                    else:
                        factor += 1
                prime_factors.append(num)
                return prime_factors

            """
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    x, y = nums[i], nums[j]
                    # print(x, y)
                    if common(x, y):
                        print('union', x, y)
                        union(x, y)

            mx = 0
            groups = defaultdict(int)
            for v in nums:
                groups[uf[v]] += 1
                mx = max(mx, groups[uf[v]])
            print(groups)
            return mx
            """
            num_factor_map = {}
            for n in nums:
                prime_factors = list(set(primeDecompose(n)))
                num_factor_map[n] = prime_factors[0]
                for i in range(len(prime_factors) - 1):
                    union(prime_factors[i], prime_factors[i + 1])

            # print(uf)
            max_size = 0
            group_count = defaultdict(int)
            for num in nums:
                group_id = find(num_factor_map[num])
                group_count[group_id] += 1
                max_size = max(max_size, group_count[group_id])
            return max_size

        # return fxr_uf()
        # return ans_dfs()
        # return rishabh_devbanshi_1()
        return os_prime_factors()


sl = Solution()
print(sl.largestComponentSize(nums=[4, 6, 15, 35]))
# print(sl.largestComponentSize([20, 50, 9, 63]))
# print(sl.largestComponentSize(nums=[2, 3, 6, 7, 4, 12, 21, 39]))
print(sl.largestComponentSize([65, 35, 43, 76, 15, 11, 81, 22, 55, 92, 31]))
print(sl.largestComponentSize([99, 68, 70, 77, 35, 52, 53, 25, 62]))
print(
    sl.largestComponentSize(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    )
)
