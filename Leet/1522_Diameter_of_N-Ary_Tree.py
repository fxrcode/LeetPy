"""
✅ GOOD Tree DFS
tag: DFS, Tree
Lookback
- WeRide VO2

Weekly Special (Nov 15)
Day 15
NOTE:
# two insights
* 1. Longest path in a tree can only happen between two leaves nodes or between a leaf node and the root node.
* 2. Each non-leaf node acts as a bridge for the paths between its descendant leaves nodes.
    * If we pick two longest sub-paths from a non-leaf node to its descendant leavest nodes, and combine them together,
    then the resulting path would be the longest path among all possible ones that are bridged by this non-leaf node.

# Algs
* Diameter: longest path between any two nodes in the N-ary tree.
* 1st glance: we might have to enumerate all pairs of nodes, in order to find out the longest path.
* With above 2 insights, it suffices to enumerate all non-leaf nodes and select the top-2 longest sub-paths bridged by each non-leaf node.

# two properties of Tree (both count #edges, but one goes down (and pick the largest), other goes up (single src/dest))
* `height` of a node: length of the longest downward path to a leaf node from that node.
* `depth` of a node: length of the path to the ROOT node.

# Two approaches
* 1. Distance with Height
* 2. Distance with Depth

----
XXX: Similar questions on LeetCode:

104. Maximum Depth of Binary Tree
110. Balanced Binary Tree
111. Minimum Depth of Binary Tree
124. Binary Tree Maximum Path Sum
298. Binary Tree Longest Consecutive Sequence
543. Diameter of Binary Tree
559. Maximum Depth of N-ary Tree
654. Maximum Binary Tree
998. Maximum Binary Tree II
1245. Tree Diameter

"""
# Definition for a Node.


class Node:
    # XXX: classic define of Node init()!
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: "Node") -> int:
        self.diam = 0

        def os_approach1_height():
            """
            Runtime: 48 ms, faster than 71.01% of Python3 online submissions for Diameter of N-Ary Tree.

            XXX: height is easier than depth in this problem
            T: O(n) enumerate each node once and only once via recursion, M: O(H)
            """

            def dfs(nod: Node):
                fir = sec = 0
                for k in nod.children:
                    dep = dfs(k)
                    if dep > fir:
                        fir, sec = dep, fir
                    elif dep > sec:
                        sec = dep
                self.diam = max(self.diam, fir + sec)
                return fir + 1

            dfs(root)
            return self.diam

        def os_approach2_depth():
            """
            Runtime: 52 ms, faster than 42.58% of Python3 online submissions for Diameter of N-Ary Tree.

            T: O(n), M: O(H)
            """

            def mx_depth(node: Node, cur_dep: int):
                if len(node.children) == 0:
                    return cur_dep
                # select top 2 depths from its children
                mx_dep = [0, 0]
                for kid in node.children:
                    dep = mx_depth(kid, cur_dep + 1)
                    if dep > mx_dep[0]:
                        mx_dep = [dep, mx_dep[0]]
                    elif dep > mx_dep[1]:
                        mx_dep = [mx_dep[0], dep]

                # calculate the distance between the two farthest leaves nodes
                distance = mx_dep[0] + mx_dep[1] - 2 * cur_dep
                self.diam = max(self.diam, distance)
                return mx_dep[0]

            mx_depth(root, 0)
            return self.diam

        def fxr_brute():
            """
            Runtime: 124 ms, faster than 5.02% of Python3 online submissions for Diameter of N-Ary Tree.

            useful case: [3,null,1,null,5]

            XXX: this brute force is 2-layer DFS, enumerate all paths!
            """
            self.ans = -1

            def hgt(cur: Node) -> int:
                # print(cur.val)
                if not cur:
                    return -1

                kid_hgt_max = -1
                for kid in cur.children:
                    kid_hgt_max = max(kid_hgt_max, hgt(kid))
                h = kid_hgt_max + 1
                # print(' ',cur.val, 'hgt', h)
                return h

            def dfs(cur: Node) -> int:
                # print('dfs',cur.val)
                kids_hght = []
                # route via cur
                for kid in cur.children:
                    kids_hght.append(hgt(kid))
                mx = sum(sorted(kids_hght, reverse=True)[:2])
                mx += min(2, len(cur.children))

                # print('\troute', cur.val, mx)

                self.ans = max(self.ans, mx)

                # route via kid
                for kid in cur.children:
                    dfs(kid)

            dfs(root)
            return self.ans
