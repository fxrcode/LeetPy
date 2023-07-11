"""
✅ GOOD Graph DFS

https://leetcode.com/explore/learn/card/graph/619/depth-first-search-in-graph/3951/
Leetcode Explore Graph: DFS

XXX: OS: For cycle detection, We will be following the node-coloring variant of the
algorithm which is explained in the Introduction to Algorithms (CLRS) book.
OS explain is succinct in visualization: [why visited won't detect cycle](https://leetcode.com/problems/all-paths-from-source-lead-to-destination/Figures/1059/img1.png)
"""


from collections import defaultdict
from typing import List


class Solution:
    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        Your runtime beats 31.48 % of python3 submissions.

        REF: OS (synonyms for official solution)
        DFS: O(V+E)
        XXX: 1st time learning 3-color-variant DFS for cycle detection
        """
        GRAY, BLACK = 1, 2
        G = defaultdict(set)
        for v, w in edges:
            G[v].add(w)
        states = [None] * n

        def lead_to_dest(cur, states):
            if states[cur]:
                # if gray, then cycle detected => False
                return states[cur] == BLACK

            if len(G[cur]) == 0:
                # if leaf node but not destination => False
                return cur == destination

            # process cur node
            states[cur] = GRAY

            for neig in G[cur]:
                if not lead_to_dest(neig, states):
                    return False

            # finished process this node, mark BLACK
            states[cur] = BLACK
            return True

        return lead_to_dest(source, states)
