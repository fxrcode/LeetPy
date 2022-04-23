'''
Q1,Q2 AC
Q3 TLE
Q4 WA
'''

from collections import defaultdict
from typing import List


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int,
                   hashValue: int) -> str:
        """
        Runtime: 8547 ms, faster than 9.09% of Python3 online submissions for Find Substring With Given Hash Value.

        XXX: got TLE in contest, due to power ** i (operator ** is costly, not O(1))
        """
        h = 0
        i = 0
        p = 1
        while i < k:
            h += (ord(s[i]) - ord('a') + 1) * p
            i += 1
            p *= power

        p //= power
        # h %= modulo
        print('\t', h)

        if h % modulo == hashValue:
            return s[:k]

        while i < len(s):
            h -= (ord(s[i - k]) - ord('a') + 1)
            h //= power
            h += (ord(s[i]) - ord('a') + 1) * p
            print(h)
            if h % modulo == hashValue:
                return s[i - k + 1:i + 1]
            i += 1

    def groupStrings(self, words: List[str]) -> List[int]:
        """
        WA: 72 / 97 test cases passed.

        input: [["umeihvaq","ezflcmsur","ynikwecaxgtrdbu","u","q","gwrv","ftcuw",...............]
        output: [191,21]
        expected: [190,21]
        """
        n = len(words)
        fa = {i: i for i in range(n)}
        rank = [0] * n
        cnt = n

        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        def union(x, y):
            rx, ry = map(find, [x, y])
            if rx == ry:
                return

            if rank[rx] < rank[y]:
                fa[rx] = ry
            else:
                fa[ry] = rx
                if rank[rx] == rank[ry]:
                    rank[rx] += 1
            nonlocal cnt
            cnt -= 1

        ws = [set(w) for w in words]
        print(ws)
        for i in range(len(ws)):
            for j in range(i + 1, len(ws)):
                x = ws[i]
                y = ws[j]
                # add, reomve 1
                if len(x) + 1 == len(y) and x.intersection(y) == x\
                    or len(x) - 1 == len(y) and y.intersection(x) == y:
                    # print('\t', i, j)
                    union(i, j)
                # replace
                if len(x) == len(y) and len(x.intersection(y)) == len(x) - 1:
                    # print(i, j)
                    union(i, j)

        fas = defaultdict(list)
        mxs = 1
        for i in range(n):
            fas[find(i)].append(i)
            mxs = max(mxs, len(fas[find(i)]))

        ans = [cnt, mxs]
        return ans


sl = Solution()
print(sl.subStrHash('leetcode', 7, 20, 2, 0))
print(sl.subStrHash(s="fbxzaad", power=31, modulo=100, k=3, hashValue=32))
# print(sl.groupStrings(words=["a", "b", "ab", "cde"]))
# print(sl.groupStrings(words=["a", "ab", "abc"]))
