"""
✅ GOOD BFS
FB tag (6mo)

Meta-cognition: no idea how to brute force
"""
from collections import Counter, deque
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        def lee215_sort():
            # T: O(nlogn)
            target.sort()
            arr.sort()
            return target == arr

        def lee215_count():
            # T: O(n)
            cnt1 = Counter(target)
            cnt2 = Counter(arr)
            return cnt1 == cnt2

        return lee215_count()

    def minOpsEqual(self, target: List[int], arr: List[int]) -> int:
        """
        https://leetcode.com/discuss/interview-question/1137426/Facebook-or-Minimizing-Permutations
        related to 969. Pancake Sorting
        """
        arr = "".join([str(n) for n in arr])
        target = "".join([str(n) for n in target])
        l = len(arr)
        q = deque([arr])
        level = 0
        visited = set()

        while q:
            qlen = len(q)
            for _ in range(qlen):
                cur = q.popleft()
                if cur == target:
                    return level
                for i in range(l):
                    for j in range(i + 1, l):
                        # your BFS neighbor can be mutated from cur by reverse any subarr
                        permut = cur[:i] + cur[i : j + 1][::-1] + cur[j + 1 :]
                        if permut not in visited:
                            visited.add(permut)
                            q.append(permut)
            level += 1
        return -1


sl = Solution()
print(sl.canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
print(sl.minOpsEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
