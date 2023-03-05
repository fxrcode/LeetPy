"""
date: 03052023
✅ GOOD BFS (bi-directional)
Tag: BFS, Hard
Daily Challenge (Jan 15)
Lookback: last we saw an array problem that can jump if same val (door vs key) is also a Graph!
    What's the logic: RELATION <=> GRAPH!!!!
    So same idea here...
    Don't go directly to shallow similarity and choose DP...

similar:
841. Keys and Rooms (array => graph BFS/DFS)
127. Word Ladder (array => graph => begin/end Bi-BFS)
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # def fxr_dp():
        def os_bi_bfs():
            """
            Runtime: 891 ms, faster than 26.19% of Python3 online submissions for Jump Game IV.

            T: O(N)
            """
            n = len(arr)
            if n <= 1:
                return 0
            G = defaultdict(list)
            for i, v in enumerate(arr):
                G[v].append(i)

            step = 0
            front, end = set([0]), set([n - 1])
            vis = set([0, n - 1])
            while front:
                if len(front) > len(end):
                    front, end = end, front
                print(front, end)

                front_next = set()
                for cur in front:
                    """
                    24 / 32 test cases passed: [-76,3,66,-32,64,2,-19,-8,-5,-93,80,-5,-76,-78,64,2,16]

                    BUG: if pop from set, not in order, so the qlen trick doesn't work! Have to use another set to save front's expand!
                    cur = front.pop()
                    """
                    v = arr[cur]

                    # option 3
                    for i in G[v]:
                        if i in end:
                            return step + 1
                        if i not in vis:
                            vis.add(i)
                            front_next.add(i)

                    # clear the list to prevent redundant search
                    # del G[v]
                    G[v].clear()

                    # option 1,2
                    for i in {cur - 1, cur + 1}:
                        if i in end:
                            return step + 1
                        if 0 <= i < n and i not in vis:
                            vis.add(i)
                            front_next.add(i)

                front = front_next
                """
                BUG: 127. Word Ladder's Bi-BFS not working here, since frontiers in front/end are in vis
                if front & end:
                    return step + 1
                """
                step += 1
            return -1

        def os_bfs():
            """
            Runtime: 1060 ms, faster than 17.10% of Python3 online submissions for Jump Game IV.

            T: O(N)
            """
            n = len(arr)
            if n <= 1:
                return 0
            G = defaultdict(list)
            for i, v in enumerate(arr):
                G[v].append(i)

            step = 0
            q = deque([0])
            vis = set()
            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur == n - 1:
                        return step

                    v = arr[cur]
                    # add all same v's index
                    for i in G[v]:
                        if i not in vis:
                            vis.add(i)
                            q.append(i)

                    del G[v]
                    for i in {cur - 1, cur + 1}:
                        if 0 <= i < n and i not in vis:
                            vis.add(i)
                            q.append(i)
                step += 1

            # BFS always return -1! since BFS visits ALL node before exit
            return -1

        return os_bi_bfs()
        # return os_bfs()


sl = Solution()
arr = [-76, 3, 66, -32, 64, 2, -19, -8, -5, -93, 80, -5, -76, -78, 64, 2, 16]
# arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
print(sl.minJumps(arr))
