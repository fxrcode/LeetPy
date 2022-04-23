'''
Daily Challenge (Dec 9)

✅ GOOD Graph (DFS/BFS)
💡insight: Graph modeling since problem has "relation" property.
    DFS with visited can detect/prevent cycle!
'''
from typing import List
from functools import cache


class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:

        def dfs(cur):
            """
            Your runtime beats 43.15 % of python3 submissions.
            XXX: validation check asap into dfs

            💡insight: virtually model the problem as Graph due to connectivity property, then we directly found solution: reachability

            Don't assume input can't be modified! you can mark it negative for visitied in DFS
            """
            if not 0 <= cur < len(arr) or arr[cur] < 0:
                return False
            if arr[cur] == 0:
                return True
            # mark visited
            arr[cur] *= -1
            return dfs(cur + arr[cur]) or dfs(cur - arr[cur])

        @cache
        def reach(cur: int) -> bool:
            """
            Runtime: 328 ms, faster than 32.55% of Python3 online submissions for Jump Game III.

            XXX: DPV dfs-explore template: validation check when calling recursion
            """
            if arr[cur] == 0:
                return True
            jump = arr[cur]
            arr[cur] *= -1  # mark visited
            ans = False
            for j in [jump, -jump]:
                if not 0 <= cur + j < len(arr) or arr[cur + j] < 0:
                    continue
                ans |= reach(cur + j)
            return ans

        return reach(start)

        def fxr_brute():
            """
            Runtime: 316 ms, faster than 38.93% of Python3 online submissions for Jump Game III.

            T: O(2^n)
            """

            # unhashable argument: set()! so can't use @cache
            # @cache
            def bt(pos: int, seen: set[int]) -> bool:
                # base
                if arr[pos] == 0:
                    return True

                # recur
                ans = False
                for jump in [arr[pos], -arr[pos]]:
                    newpos = pos + jump
                    if newpos in seen:
                        continue
                    if 0 <= newpos < len(arr):
                        seen.add(newpos)
                        ans |= bt(newpos, seen)
                        seen.remove(newpos)
                return ans

            return bt(start, set())
