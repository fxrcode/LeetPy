"""
tag: DFS, skills
Lookback:
- Tree => DFS! 
    * BFS is messy
- Binary Tree vs N-ary Tree (#297)
    
https://leetcode.com/explore/learn/card/n-ary-tree/132/conclusion/
N-ary Tree: Conclusion

Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree is a rooted tree in which each node has no more than N children. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that an N-ary tree can be serialized to a string and this string can be deserialized to the original tree structure.
Ref: https://leetcode.libaoj.in/serialize-and-deserialize-n-ary-tree.html
XXX: This is one of the most interesting problems on the leetcode platform simply because there are a lot of different ways of solving this problem. There is no incorrect approach here. Some approaches are much easier to code-up and are more efficient as opposed to others. However, the variations for serialization and deserialization are endless.
XXX: Neat trick which is to represent each number as a unicode character. `chr(48)`->0, `ord('0')`->48. So we don't need to parse DEL!

"""
from collections import deque


class Node(object):
    def __init__(self, val=None, kids=None):
        self.val = val
        self.kids = kids if kids is not None else []

    def __repr__(self) -> str:
        return str(self.val)


class Codec:
    """
    Runtime: 103 ms, faster than 75.26% of Python3 online submissions for Serialize and Deserialize N-ary Tree.

    https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/150790/Python-O(n)-recursive-both-functions/408260
    """

    def serialize(self, root):
        ser = []

        def dfs(T: Node):
            if not T:
                return
            ser.append(str(T.val))
            for k in T.kids:
                dfs(k)
            ser.append(
                "!"
            )  # indicates no more children, continue serialization from parent

        dfs(root)
        return ",".join(ser)

    def deserialize(self, data):
        """
        Runtime: 129 ms, faster than 49.53% of Python3 online submissions for Serialize and Deserialize N-ary Tree.
        https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/150790/Python-O(n)-recursive-both-functions/413868

        XXX: use iter rather allocate deque
        """
        if not data:
            return None

        def fn():
            v = next(it)
            if v != "!":
                node = Node(int(v))
                k = fn()
                while k:
                    node.kids.append(k)
                    k = fn()
                return node

        it = iter(data.split(","))
        return fn()

    def deserialize_deque(self, data):
        if not data:
            return None
        tokens = deque(data.split(","))

        def fn():
            if not tokens:
                return None
            node = Node(int(tokens.popleft()))
            while tokens[0] != "!":  # add child nodes with subtrees
                node.kids.append(fn())
            tokens.popleft()  # discard the '!'
            return node

        return fn()


"""
        1
    2   3   4
   5   6,7  8
          9
"""
codec = Codec()
root = Node(
    1,
    kids=[
        Node(2, kids=[Node(5)]),
        Node(3, kids=[Node(6), Node(7, kids=[Node(9)])]),
        Node(4, kids=[Node(8)]),
    ],
)
rs = codec.serialize(root)
rd = codec.deserialize(rs)
rrs = codec.serialize(rd)
print(rs)
print(rrs)

'''
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class LintCodec:
    """ Lintcode has predefined serialization format rather open question as in leetcode
    Solution 2: use [] to include children, so the deserialize is similar to 394. Decode String
    https://www.lintcode.com/problem/1532/solution/31131
    BUG: seems lintcode has test has issue, the root is a list rather node! so I didn't pass.
    [1 [3[5 6] 2 4]] means:
            1
        /   |   \
       3    2    4
     /   \
    5     6
    """

    def __init__(self) -> None:
        self.pos = 1

    def serialize(self, root: DirectedGraphNode) -> str:
        def dfs(root: DirectedGraphNode) -> str:
            res = []
            if not root:
                return "".join(res)
            res.append(str(root.label))
            res.append("[")
            nrn = len(root.neighbors)
            for i in range(nrn):
                res.append(dfs(root.neighbors[i]))
            res.append("]")
            return "".join(res)

    def deserialize(self, data: str) -> "DirectedGraphNode":
        def solve(data: str) -> DirectedGraphNode:
            num = 0
            node = None

            while data[self.pos].isdigit():
                num = num * 10 + int(data[self.pos])
                self.pos += 1
            node = DirectedGraphNode(num)

            while self.pos < len(data):
                if data[self.pos] == "[":
                    self.pos += 1
                    node.neighbors.append(solve(data))
                elif data[self.pos] == "]":
                    self.pos += 1
                    break
            return node

        if not data:
            return None
        return solve(data)

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))

'''
