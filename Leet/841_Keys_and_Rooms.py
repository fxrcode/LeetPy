"""
✅ GOOD Implicit DFS

https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1391/
Leetcode explore Queue & Stack: Conclusion
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

"""


from typing import List


class Solution:
    def canVisitAllRooms_iter(self, rooms: List[List[int]]) -> bool:
        def prune_iter():
            """[summary]
            https://leetcode.com/problems/keys-and-rooms/discuss/133855/Straight-Forward
            """
            dfs = [0]
            seen = set(dfs)
            while dfs:
                cur = dfs.pop()
                for j in rooms[cur]:
                    if j not in seen:
                        dfs.append(j)
                        seen.add(j)
                        # prune as soon as visited all rooms
                        if len(seen) == len(rooms):
                            return True
            return len(seen) == len(rooms)

        def fxr_dfs():
            """[summary]
            AC in 1st try: it's easy for me to see the implicit graph
            Your runtime beats 80.92 % of python3 submissions.
            T: O(N+E), N = # rooms, E = # keys
            """
            visited = set()

            def dfs(rooms, i, visited):
                if i in visited:
                    return
                visited.add(i)
                for neig in rooms[i]:
                    if neig in visited:
                        continue
                    dfs(rooms, neig, visited)

            dfs(rooms, 0, visited)
            return len(visited) == len(rooms)

        prune_iter()
