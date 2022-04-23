'''
Leetcode explore N-ary Tree: Recursion
https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
Design an algorithm to encode an N-ary tree into a binary tree and decode the binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. Similarly, a binary tree is a rooted tree in which each node has no more than 2 children. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that an N-ary tree can be encoded to a binary tree and this binary tree can be decoded to the original N-nary tree structure.
'''

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def encode(self, root: 'Node') -> TreeNode:
        # beat 70.59% in lintcode: 1530 · Encode N-ary Tree to Binary Tree
        # Encodes an n-ary tree to a binary tree.
        # https://leetcode.libaoj.in/encode-n-ary-tree-to-binary-tree.html
        # first kid as left child, and this kid's right chain subtree is it's origin siblings
        # Same as Huahua's 116. Populating Next Right Pointers in Each Node's Local view: we need preorder recursion
        if not root:
            return None

        rootNode = TreeNode(root.val)
        if root.children:
            first_kid = root.children[0]
            rootNode.left = self.encode(first_kid)

        # the parent of the rest of children
        cur = rootNode.left
        for sibling in root.children[1:]:
            node = self.encode(sibling)
            cur.right = node
            cur = cur.right

        return root

    def decode(self, data: TreeNode) -> 'Node':
        # Decodes your binary tree to an n-ary tree.
        if not data:
            return None
        rootNode = Node(data.val, [])
        cur = data.left
        while cur:
            node = self.decode(cur)
            rootNode.children.append(node)
            cur = cur.right
        return rootNode

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
