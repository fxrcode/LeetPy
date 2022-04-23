"""
✅ GOOD BFS (bi-directional)
Tag: Medium, BFS
Lookback:
- bi-directional BFS (expand smaller q)
- How to prune?
Similar:
- Frog jump, Knight Tour, Open Lock, Word Ladder
"""

from collections import deque
from operator import add, sub, xor
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        def os_word_ladder():
            """
            Runtime: 2479 ms, faster than 74.19% of Python3 online submissions for Minimum Operations to Convert Number.

            https://leetcode-cn.com/problems/minimum-operations-to-convert-number/solution/gong-shui-san-xie-shuang-xiang-bfs-mo-ba-uckg/1239705
            """
            q1, q2 = set([start]), set([goal])
            step = 0
            vis = set([start, goal])
            while q1:
                # 交换队列大小，保证BFS总是展开小的那一侧
                if len(q1) > len(q2):
                    q1, q2 = q2, q1
                q1_nxt = set()
                for v in q1:
                    # BUG:
                    # if v in q2:
                    #     return step
                    for n in nums:
                        for vv in (v + n, v - n, v ^ n):
                            if vv in q2:
                                return step + 1
                            if vv in vis or not 0 <= vv <= 1000:
                                continue
                            vis.add(vv)
                            q1_nxt.add(vv)
                q1 = q1_nxt
                step += 1
            return -1

        return os_word_ladder()

        def fxr():
            """
            Runtime: 6171 ms, faster than 28.91% of Python3 online submissions for Minimum Operations to Convert Number.

            """
            q = deque([(start, 0)])
            vis = set(q)

            while q:
                for _ in range(len(q)):
                    v, s = q.popleft()
                    if v == goal:
                        return s
                    if not (0 <= v <= 1000):
                        continue
                    for n in nums:
                        for vv in (v + n, v - n, v ^ n):
                            # for op in (add, sub, xor):
                            #     vv = op(v, n)
                            if vv not in vis:
                                vis.add(vv)
                                q.append((vv, s + 1))
            return -1

        return fxr()


sl = Solution()
print(sl.minimumOperations(nums=[2, 4, 12], start=2, goal=12))
print(sl.minimumOperations(nums=[3, 5, 7], start=0, goal=-4))
print(sl.minimumOperations(nums=[2, 8, 16], start=0, goal=1))
