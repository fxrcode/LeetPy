"""
Tag: DFS, BFS, Medium
Lookback:
+ indegree + dfs
* 1st time set.difference_udpate (vs difference, -)
+ careful on edge case: 4, [1, 0, 3, -1], [-1, -1, -1, -1]
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def rock_bfs():
            def find_root() -> int:
                nodes = set(range(n))
                # https://stackoverflow.com/questions/30986751/set-difference-versus-set-subtraction
                nodes.difference_update(leftChild + rightChild)
                return nodes.pop() if len(nodes) == 1 else -1

            def bfs(root: int) -> bool:
                q, vis = deque([root]), {root}
                while q:
                    u = q.popleft()
                    for v in leftChild[u], rightChild[u]:
                        if v >= 0:
                            if v in vis:
                                return False
                            vis.add(v)
                            q.append(v)
                return len(vis) == n

            root = find_root()
            return root >= 0 and bfs(root)

        return rock_bfs()

        def renhai_dfs():
            """
            Runtime: 292 ms, faster than 98.82% of Python3 online submissions for Validate Binary Tree Nodes.

            https://leetcode.com/problems/validate-binary-tree-nodes/discuss/939381/Python:-clean-BFS-96-faster-TimeComplexity:-O(n)-Space-Complexity:-O(n)/794077

            2 steps:
            a. find indegree,
            """
            ind = [0] * n
            for l, r in zip(leftChild, rightChild):
                if l != -1:
                    ind[l] += 1
                    if ind[l] > 1:
                        return False
                if r != -1:
                    ind[r] += 1
                    if ind[r] > 1:
                        return False

            if ind.count(0) != 1:
                return False

            # root's indegree === 0
            root = ind.index(0)

            # count nodes from root, if the total number is not n, it means there are islands, then return false.
            def count_nodes(r):
                if r == -1:
                    return 0
                return 1 + count_nodes(leftChild[r]) + count_nodes(rightChild[r])

            nodes = count_nodes(root)
            return nodes == n

        return renhai_dfs()


sl = Solution()
print(sl.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
print(sl.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
print(sl.validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1]))
print(sl.validateBinaryTreeNodes(4, [1, 0, 3, -1], [-1, -1, -1, -1]))
