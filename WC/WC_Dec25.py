from collections import defaultdict
from typing import List


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if num % 10 == 0:
            return False
        return True

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        ans = [0] * len(s)
        for i in range(len(s)):
            x, y = startPos
            for j in range(i, len(s)):
                op = s[j]
                dx, dy = 0, 0
                if op == "L":
                    dx, dy = 0, -1
                elif op == "R":
                    dx, dy = 0, 1
                elif op == "U":
                    dx, dy = -1, 0
                else:
                    dx, dy = 1, 0
                x, y = x + dx, y + dy
                if 0 <= x < n and 0 <= y < n:
                    ans[i] += 1
                else:
                    break
        return ans

    def getDistances(self, arr: List[int]) -> List[int]:
        """
        TLE
        """
        d = defaultdict(set)
        for i, n in enumerate(arr):
            d[n].add(i)
        ans = [0] * len(arr)
        for n in d:
            diffs = list(d[n])
            for i in d[n]:
                ans[i] = sum(diffs)
        return ans

    def recoverArray(self, nums: List[int]) -> List[int]:
        snums = sorted(list(set(nums)))
        mn_mx = min(snums) + max(snums)
        kmax = (max(snums) - min(snums)) // 2
        mn_mn = min(snums) + 1
        mx_mx = max(snums) - kmax
        N = len(nums) // 2
        ans = []

        for k in range(1, kmax):
            for v in range(mn_mn, mx_mx + 1):
                for i in range(-(N - 1), (N + 1)):
                    n = v + k * i
                    if n < mn_mn or n > mx_mx:
                        break
                    if n not in snums:
                        break
                    ans.append(n)
                if len(ans) == N:
                    return ans
                ans = []
        return []


sl = Solution()
# print(sl.isSameAfterReversals(526))
# print(sl.executeInstructions(3, [0, 1], 'RRDDLU'))
print(sl.recoverArray([2, 10, 6, 4, 8, 12]))
