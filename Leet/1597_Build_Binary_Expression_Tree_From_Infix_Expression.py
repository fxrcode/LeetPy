"""
✅ GOOD Recursion 
✅ GOOD Stack
tag: hard, stack, dfs
Lookback:
- do more practice in recursion, as well as stack. 
    So many hidden gem in details
TODO: Followup: how to handle space and multi-digit numbers as in 772?
[ ] REDO
Similar:
-772. Basic Calculator III
"""


from collections import deque


class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        if not self:
            return ""
        l, r = "", ""
        if self.left:
            l = repr(self.left)
        if self.right:
            r = repr(self.right)
        return f"{l}{self.val}{r}"
        #! Why recursion not work in __repr__? it prints sth like: None3None4
        # return f"left={repr(self.left)}, v={self.val}, right={repr(self.right)}"


class Solution:
    def expTree(self, s: str) -> "Node":
        def ruiqin():
            """
            Runtime: 64 ms, faster than 10.50% of Python3 online submissions for Build Binary Expression Tree From Infix Expression.

            https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/discuss/1058622/similar-to-Basic-Calculator-III-recursion-%2B-Queue-%2B-Deque
            it's very similar to Basic Calculator III. In both questions, when we encounter a * or /, we have to keep processing it until the multiplication or division ends.
            """

            def dfs(q):
                # keep a deque of nums nodes, + and - nodes
                deq = deque()
                while q:
                    c = q.popleft()
                    if c.isdigit():
                        deq.append(Node(c))
                    elif c == "(":
                        sub = dfs(q)
                        deq.append(sub)
                    elif c == ")":
                        break
                    elif c in "+-":
                        deq.append(Node(c))
                    else:  # c in '*/'
                        """
                        * or / cannot be pushed to the deque directly
                        its left child node is the top node in the deque
                        its right child node is the next node
                        """
                        node = Node(c)
                        node.left = deq.pop()

                        # right child node might be a simple digit, might be a node in parenthesis
                        next = q.popleft()
                        if next == "(":
                            node.right = dfs(q)
                        else:
                            node.right = Node(next)
                        deq.append(node)

                """
                it's easy to reconstruct a tree when there are only nums, + and - nodes 
                always use + or - as the root node
                """
                root = deq.popleft()
                while deq:
                    node = deq.popleft()
                    node.left = root
                    node.right = deq.popleft()
                    root = node
                return root

            q = deque(s)
            return dfs(q)

        return ruiqin()

        def keren3():
            ops, nums = [], []

            def mock_compute():
                op = ops.pop()
                r = nums.pop()
                l = nums.pop()
                nums.append(Node(val=op, left=l, right=r))

            for ch in s:
                if ch.isdigit():
                    nums.append(Node(val=ch))
                elif ch in ["+", "-"]:
                    if ops and ops[-1] in ["+", "-", "*", "/"]:
                        mock_compute()
                    ops.append(ch)
                elif ch in ["*", "/"]:
                    if ops and ops[-1] in ["*", "/"]:
                        mock_compute()
                    ops.append(ch)
                elif ch == "(":
                    ops.append(ch)
                elif ch == ")":
                    while ops[-1] != "(":
                        mock_compute()
                    ops.pop()
            while ops:
                mock_compute()
            return nums[0]


sl = Solution()
# s = "3*4-2*5"
# s = "3-4"
s = "2-3/(5*2)+1"
root = sl.expTree(s)
print(root)
