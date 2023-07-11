"""
Lookback:
3/4
Q1-Q3 => 30min
Q4 stuck for TLE, even w/ Trie
"""


from collections import Counter, defaultdict
from typing import List


class Solution:
    class Encrypter:
        def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
            self.mp = {k: v for k, v in zip(keys, values)}
            self.rev = defaultdict(list)
            for v, k in zip(values, keys):
                self.rev[v].append(k)
            self.d = set(dictionary)
            self.root = {}

            def insert(s):
                cur = self.root
                for c in s:
                    cur = cur.setdefault(c, {})
                cur["#"] = s

            for s in dictionary:
                insert(s)

        def encrypt(self, word1: str) -> str:
            res = []
            for w in word1:
                res.append(self.mp[w])
            return "".join(res)

        def decrypt(self, word2: str) -> int:
            def find(s):
                cur = self.root
                for c in s:
                    if c not in cur:
                        return False
                    cur = cur[c]
                return True

            q = []
            for i in range(0, len(word2), 2):
                q.append(word2[i : i + 2])

            def bt(i, path):
                if i == len(q):
                    p = "".join(path)
                    # print(p)
                    if p in self.d:
                        nonlocal res
                        res += 1
                    return
                for k in self.rev[q[i]]:
                    pre = "".join(path + [k])
                    if not find(pre):
                        print(pre)
                        continue
                    bt(i + 1, path + [k])

            res = 0
            bt(0, [])
            return res

    def maximumCandies(self, candies: List[int], k: int) -> int:
        def feasible(x):
            kids = 0
            for can in candies:
                kids += can // x
                if kids >= k:
                    return True
            return False

        if sum(candies) < k:
            return 0
        l, r = 1, sum(candies) // k + 1
        while l < r:
            mid = (l + r) // 2
            if not feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l - 1

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        DEG = Counter()
        for w, l in matches:
            DEG[l] += 1
            if w not in DEG:
                DEG[w] = 0
        ans = [[], []]
        for p, l in DEG.items():
            if l == 0:
                ans[0].append(p)
            if l == 1:
                ans[1].append(p)
        ans[0].sort()
        ans[1].sort()
        return ans

    def convertTime(self, current: str, correct: str) -> int:
        def c2m(s):
            s = s.split(":")
            hh, mm = int(s[0]), int(s[1])
            t = hh * 60 + mm
            return t

        delta = c2m(correct) - c2m(current)
        res = 0

        for d in [60, 15, 5, 1]:
            res += delta // d
            delta %= d
        return res


sl = Solution()
codec = sl.Encrypter(
    keys=["a", "b", "c", "d"],
    values=["ei", "zf", "ei", "am"],
    dictionary=["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"],
)
print(codec.encrypt("abcd"))
print(codec.decrypt("eizfeiam"))
# print(sl.maximumCandies(candies=[5, 8, 6], k=3))
# print(sl.maximumCandies(candies=[2, 5], k=11))
# print(sl.maximumCandies([4, 7, 5], 16))
# print(sl.findWinners(matches=[[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
# print(sl.findWinners(matches=[[2, 3], [1, 3], [5, 4], [6, 4]]))
# print(sl.convertTime(current="02:30", correct="04:35"))
# print(sl.convertTime(current="11:00", correct="11:01"))
