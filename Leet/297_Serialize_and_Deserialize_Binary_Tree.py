"""
tag: Hard, Tree, DFS
Lookback:
- compare N-ary vs Binary Codec

https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/995/
Leetcode explore Binary Tree: Conclusion
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

"""
# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode(object):
    def __init__(self, x: int, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


SEP, NIL = ",", "x"


class Codec:
    """
    Runtime: 265 ms, faster than 56.30% of Python3 online submissions for Serialize and Deserialize Binary Tree.

    T: O(N)
    """

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "x"
        else:
            return ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        def dfs():
            # v = q.popleft()
            v = next(it)
            if v == "x":
                return None
            root = TreeNode(int(v))
            root.left = dfs()
            root.right = dfs()
            return root

        # q = deque(data.split(","))
        it = iter(data.split(","))
        return dfs()


class Codec_Pre_Order_SelfData:
    """
    https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/396124/Python-very-easy-to-understand-recursive-preorder-with-comments
    XXX: When I do 652. Find Duplicate Subtree, I don't know other single
     traversal encoding can re-construct Binary Tree other than level order. So My impl is Too Slow!!!
     So you'd better impl various approach, not only for this very problem, but also for future puzzles!!!
    NOTE: https://www.geeksforgeeks.org/if-you-are-given-two-traversal-sequences-can-you-construct-the-binary-tree/
        If there's no 'x' indicate null, you must have combination of at least 2 traversals to reconstruct.
        But you have 'x' indicate null, then any one traversal encoding can be deserialized to binary tree!
    """

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return "x"
        else:
            return ",".join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        # XXX: Crux: updating global data!
        self.data = data
        if self.data[0] == "x":
            return None

        # node = TreeNode(self.data[:self.data.find(',')])
        node = TreeNode(int(data[0]))
        # XXX: Crux: shift to next number in data string
        node.left = self.deserialize(self.data[self.data.find(",") + 1 :])
        # XXX: Curx of Crux: this data has is not the same data as in 47! since node.left cursion has
        #  update global data! basically finish buildup left subtree, and removed left subtree from the data!
        node.right = self.deserialize(self.data[self.data.find(",") + 1 :])

        return node


class Codec_Level_Order:
    """
    Your runtime beats 76.82 % of python3 submissions.

    AC in 1st try
    """

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ""
        res = []
        q = deque([root])
        while q:
            qlen = len(q)
            for _ in range(qlen):
                cur = q.popleft()
                if cur:
                    res.append(str(cur.val))
                    q.append(cur.left)
                    q.append(cur.right)
                else:
                    res.append(NIL)
        return SEP.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return None
        nodes = data.split(SEP)
        root = TreeNode(nodes[0])
        q = deque([root])

        i = 1
        while i < len(nodes):
            qlen = len(q)
            for _ in range(qlen):
                cur = q.popleft()
                lv = nodes[i]
                i += 1
                if lv != NIL:
                    cur.left = TreeNode(lv)
                    q.append(cur.left)
                rv = nodes[i]
                i += 1
                if rv != NIL:
                    cur.right = TreeNode(rv)
                    q.append(cur.right)
        return root


# root = TreeNode(1,
#                 left=TreeNode(2,
#                               left=TreeNode(4)),
#                 right=TreeNode(3,
#                                left=TreeNode(2,
#                                              left=TreeNode(4)),
#                                right=TreeNode(4)))

root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))


codec = Codec()

ser = codec.serialize(root)
print(ser)

des = codec.deserialize(ser)
ser2 = codec.serialize(des)
print(ser2)
