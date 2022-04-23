"""
✅ GOOD DFS (pre-order) & prefix-sum!


https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E9%80%92%E5%BD%92%E8%AF%A6%E8%A7%A3.md
"""


from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def os_prefixsum(root: TreeNode) -> int:
            def preorder(node: TreeNode, curr_sum) -> None:
                nonlocal count
                if not node:
                    return

                # current prefix sum
                curr_sum += node.val

                # here is the sum we're looking for
                if curr_sum == k:
                    count += 1

                # number of times the curr_sum − k has occurred already,
                # determines the number of times a path with sum k
                # has occurred up to the current node
                count += h[curr_sum - k]

                # add the current sum into hashmap
                # to use it during the child nodes processing
                h[curr_sum] += 1

                # process left subtree
                preorder(node.left, curr_sum)
                # process right subtree
                preorder(node.right, curr_sum)

                # remove the current sum from the hashmap
                # in order not to use it during
                # the parallel subtree processing
                h[curr_sum] -= 1

            count, k = 0, targetSum
            h = defaultdict(int)
            preorder(root, 0)
            return count

        def wonderlives_bruteforce(root: TreeNode):
            """
            Runtime: 920 ms, faster than 14.84% of Python3 online submissions for Path Sum III.

            REF: https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
            Method 1: Brute-force DFS
            XXX: Two layer DFS. 1st dfs traverse each node O(N), 2nd dfs get all paths from each given node O(N)->O(logn)
            So T: O(N^2) to O(nlogn)
            """

            def test(node: TreeNode, target: int):
                # 2nd layer dfs:
                if not node:
                    return
                # if target == 0:
                if node.val == target:
                    self.num_paths += 1

                test(node.left, target - node.val)
                test(node.right, target - node.val)

            def dfs(node: TreeNode):
                # 1st layer dfs: traverse each node once
                if not node:
                    return
                test(node, targetSum)
                dfs(node.left)
                dfs(node.right)

            self.num_paths = 0
            dfs(root)
            return self.num_paths

        return wonderlives_bruteforce(root)

        """
        def dfs(cur: TreeNode, path, res, use):
            if not cur:
                return
            if use:
                path += [cur]
            addall = 0
            for nod in path:
                addall += nod.val
            if addall == targetSum:
                res.append(1)

            for n in [cur.left, cur.right]:
                for u in [0, 1]:
                    dfs(n, path, res, u)

        def bt(cur: TreeNode, path, res):
            if not cur:
                return
            addall = 0
            for nod in path:
                addall += nod.val
            if addall == targetSum:
                res.append(1)
                # return
            for n in [cur.left, None, cur.right, None]:
                # use
                bt(n, path + [n], res)

        res = []
        dummy = TreeNode(None, left=root)
        # bt(dummy, [], res)
        dfs(root, [], res)
        return sum(res)
        """
