"""
✅ GOOD BFS (bi-directional)
Tag: Medium, BFS
Lookback:
Similar:
- Frog jump, Minimum Knight Moves, 2059, Word Ladder
"""

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def dbabichev_bi_direction():
            """
            Runtime: 110 ms, faster than 99.85% of Python3 online submissions for Open the Lock.

            """
            dead = set(deadends)
            if "0000" in dead:
                return -1
            q1, q2 = set(["0000"]), set([target])
            vis = set(["0000", target, *deadends])
            ops = 0
            while q1:
                if len(q1) > len(q2):
                    q1, q2 = q2, q1
                q1_nxt = set()
                for code in q1:
                    # option1: allow q1 as candidate
                    if code in q2:
                        return ops
                    for i in range(4):
                        d = int(code[i])
                        for k in (d - 1) % 10, (d + 1) % 10:
                            cand = code[:i] + str(k) + code[i + 1 :]
                            # option2: must be q1's neighbor as candidate
                            if cand in q2:
                                return ops + 1
                            if cand not in vis:
                                vis.add(cand)
                                q1_nxt.add(cand)
                q1 = q1_nxt
                ops += 1
            return -1

        def dbabichev():
            """
            Runtime: 1152 ms, faster than 31.44% of Python3 online submissions for Open the Lock.

            """
            dead = set(deadends)
            q = deque([(0, "0000")])
            if "0000" in dead:
                return -1
            while q:
                steps, code = q.popleft()
                if code == target:
                    return steps

                for i in range(4):
                    d = int(code[i])
                    for k in (d - 1) % 10, (d + 1) % 10:
                        cand = code[:i] + str(k) + code[i + 1 :]
                        if cand not in dead:
                            dead.add(cand)
                            q.append((steps + 1, cand))
            return -1

        # return dbabichev()
        return dbabichev_bi_direction()


sl = Solution()
print(sl.openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))
print(sl.openLock(deadends=["8888"], target="0009"))
print(sl.openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888"))
print(sl.openLock(["0201", "0101", "0102", "1212", "2002"], "0000"))
