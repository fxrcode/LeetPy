"""
✅ GOOD TopoSort
Tag: 
Lookback:
https://leetcode.com/explore/learn/card/graph/623/kahns-algorithm-for-topological-sorting/3909/
Leetcode Explore Graph: Topological Sort
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def bfs():
            """
            Your runtime beats 99.24 % of python3 submissions.

            AC in 1 after watched Neetcode & OS
            OS is good and rigorous, but Neet's analysis is good for time limited interview.
            OS showed both BFS and DFS, while Neet used DFS.
            But I prefer Neet's Adjacent list init, rather OS's init.
            """

            AL = {c: set() for w in words for c in w}  # Neet style
            indegree = {c: 0 for w in words for c in w}

            for fir, sec in zip(words, words[1:]):
                minlen = min(len(fir), len(sec))
                if len(fir) > len(sec) and fir[:minlen] == sec[:minlen]:
                    return ""
                for i in range(minlen):
                    if fir[i] != sec[i]:
                        AL[fir[i]].add(sec[i])
                        break

            for c, ds in AL.items():
                for d in ds:
                    indegree[d] += 1

            q = deque([c for c, deg in indegree.items() if deg == 0])
            toposort = []
            while q:
                c = q.popleft()
                toposort.append(c)
                if len(toposort) == len(indegree):
                    return "".join(toposort)
                for v in AL[c]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)

            return ""

        def dfs_3color():
            """
            Runtime: 57 ms, faster than 29.01% of Python3 online submissions for Alien Dictionary.

            2nd time using 3-color-variant DFS, because in toposort, we need to detect cycle so return False
            """

            AL = {c: set() for w in words for c in w}

            # step 1: build AL of char
            for fir, sec in zip(words, words[1:]):
                # XXX: for case ["abc","ab"]
                lenmin = min(len(fir), len(sec))
                if len(fir) > len(sec) and fir[:lenmin] == sec[:lenmin]:
                    return ""
                for c, d in zip(fir, sec):
                    if c != d:
                        AL[c].add(d)
                        break

            # step 2: CLRS 3-color DFS & post-order traversal for toposort/cycle detection
            WHITE, GRAY, BLACK = 0, 1, 2
            st = defaultdict(int)
            ts = []

            def dfs_color(c):
                if st[c] != WHITE:
                    return st[c] == BLACK  # if gray, then cycle detected
                st[c] = GRAY
                for v in AL[c]:
                    if st[v] == GRAY or not dfs_color(v):
                        return False  # cycle detected lower down
                st[c] = BLACK
                ts.append(c)
                return True  # write framework first, before recursion, as Neet does!

            # for DFS toposort, we need to call dfs on ALL nodes, just like CC!
            if not all(dfs_color(c) for c in AL):
                return ""
            return "".join(ts[::-1])

        return dfs_3color()


sl = Solution()
print(sl.alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"]))
print(sl.alienOrder(words=["z", "x", "z"]))
print(sl.alienOrder(words=["abc", "ab"]))


def snippet(words: List[str]):
    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words...
    for first_word, second_word in zip(words, words[1:]):
        print("[word]\t", first_word, second_word)
        for c, d in zip(first_word, second_word):
            if c != d:
                print("letter\t", c, d)


# snippet(words=["wrt", "wrf", "er", "ett", "rftt"])
