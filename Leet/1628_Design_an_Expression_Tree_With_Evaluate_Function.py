"""
tag: medium, OOP, dfs, stack
Lookback:
- 1st time: ABC, abstractmethod 
- use dict as switch (pythonic)
- postfix => Stack (LIFO)

# Runtime: 83 ms, faster than 5.24% of Python3 online submissions for Design an Expression Tree With Evaluate Function.

"""


from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a // b,
        }
        op = ops[self.val]
        return op(self.left.evaluate(), self.right.evaluate())

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> "Node":
        cur, stack = None, []
        for c in postfix:
            cur = TreeNode(c)
            if not c.isdigit():
                cur.right = stack.pop()
                cur.left = stack.pop()
            stack.append(cur)
        return cur


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
