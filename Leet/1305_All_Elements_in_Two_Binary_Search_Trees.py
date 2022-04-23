'''
FB tag
tag: Medium, DFS
'''

from typing import List
from heapq import merge


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def os_iter():
            """
            Runtime: 428 ms, faster than 51.29% of Python3 online submissions for All Elements in Two Binary Search Trees.

            One-pass
            [ ] REDO
            """
            stk1, stk2, res = [], [], []
            r1, r2 = root1, root2
            while r1 or r2 or stk1 or stk2:
                # update both stacks
                # by going left till possible
                while r1:
                    stk1.append(r1)
                    r1 = r1.left
                while r2:
                    stk2.append(r2)
                    r2 = r2.left

                # Add the smallest value into output,
                # pop it from the stack,
                # and then do one step right
                if not stk2 or (stk1 and stk1[-1].val <= stk2[-1].val):
                    r1 = stk1.pop()
                    res.append(r1.val)
                    r1 = r1.right

                else:
                    r2 = stk2.pop()
                    res.append(r2.val)
                    r2 = r2.right
            return res

        def DBabichev():
            """
            Runtime: 434 ms, faster than 49.47% of Python3 online submissions for All Elements in Two Binary Search Trees.

            https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/829720/Python-O(n1-%2B-n2)-inorder-traversal-explained
            T: O(N+M)
            """
            def ino(r: TreeNode, lst: list[int]):
                if r:
                    ino(r.left, lst)
                    lst.append(r.val)
                    ino(r.right, lst)

            li1, li2 = [], []
            ino(root1, li1)
            ino(root2, li2)

            L1, L2 = len(li1), len(li2)
            i, j = 0, 0
            ans = []
            while i < L1 and j < L2:
                if li1[i] < li2[j]:
                    ans.append(li1[i])
                    i += 1
                else:
                    ans.append(li2[j])
                    j += 1
            return ans + li1[i:] + li2[j:]

        return DBabichev()

        def fxr():
            """
            Runtime: 3908 ms, faster than 5.03% of Python3 online submissions for All Elements in Two Binary Search Trees.

            https://leetcode.com/problems/all-elements-in-two-binary-search-trees/discuss/464167/Why-is-Python-generator-based-inorder-traversal-so-slow
            """
            def it(r: TreeNode):
                if r:
                    yield from it(r.left)
                    yield r.val
                    yield from it(r.right)

            gen1, gen2 = it(root1), it(root2)

            return list(merge(gen1, gen2))

        # return fxr()


sl = Solution()
root1 = TreeNode(2, left=TreeNode(1), right=TreeNode(4))
root2 = TreeNode(1, left=TreeNode(0))
print(sl.getAllElements(root1, root2))
