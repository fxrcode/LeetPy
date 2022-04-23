"""
tag: medium, dfs

Lookback:
- from 1367
- Follow up: what if the tree also contains `-`?
    - sign trick: +1/-1, if -1, so combination of +/- will make odd minus into a minus.
    - sign parent only affect rhs
"""


from collections import Counter, deque
from re import L


class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return self.val


class Solution:
    def checkEquivalence(self, root1: "Node", root2: "Node") -> bool:
        def alanlzl():
            """
            When traverse the first tree, we do dic[node.val] += 1. And when traverse the second tree, we do dic[node.val] -= 1. If two trees are equivalent, all dic values should be 0 at the end.

            This method extends nicely to the follow-up question. If there's a minus sign, we simply revert the increment value (sign) of the right child.
            """

            def dfs(node, sign):
                if not node:
                    return
                if node.val == "+":
                    dfs(node.left, sign)
                    dfs(node.right, sign)
                elif node.val == "-":
                    dfs(node.left, sign)
                    dfs(node.right, -sign)
                else:
                    dic[node.val] += sign

            dic = Counter()
            dfs(root1, 1)
            dfs(root2, -1)
            return all(x == 0 for x in dic.values())

        def fxr_eval():
            """
            Runtime: 580 ms, faster than 85.15% of Python3 online submissions for Check If Two Expression Trees are Equivalent.

            """

            def dfs(r, sign, mp):
                if not r:
                    return
                if r.val.isalpha():
                    k = r.val if sign == 1 else "-" + r.val
                    mp[k] += 1
                # extend(l,r): no return, it only in-place l = l+r
                if r.val in "+-":
                    """
                    How to proof recursion corrective?
                        - simply focus on local view
                    Left child wont have any effect of sign
                    Right subtree elements have their signed parents in front of them hence reverse sign for right subtree if current node is negative
                    """
                    dfs(r.left, sign, mp)
                    sign *= -1 if r.val == "-" else 1
                    dfs(r.right, sign, mp)
                # return [r.val] if sign == 1 else ["-" + r.val]

            c1, c2 = Counter(), Counter()
            dfs(root1, 1, c1)
            dfs(root2, 1, c2)
            print(c1, c2)
            return c1 == c2

        return fxr_eval()

        '''
        def fxr_WA():
            """
            22 / 84 test cases passed.

            [+,+,+,e,e,+,+,null,null,null,null,f,n,s,q]
            [+,+,n,+,q,null,null,+,+,null,null,e,f,e,s]
            expected: True
            """

            def dfs(r1, r2):
                if r1 and r2:
                    if r1.val != r2.val:
                        return False
                    return dfs(r1.left, r2.left) and dfs(r1.right, r2.right) or dfs(r1.left, r2.right) and dfs(r1.right, r2.left)
                return r1 == r2 == None

            return dfs(root1, root2)
        '''


def build_tree(s):
    root = Node(s.popleft())
    q = deque([root])
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if s:
                c = s.popleft()
                if c:
                    l = Node(c)
                    cur.left = l
                    q.append(l)
            if s:
                c = s.popleft()
                if c:
                    r = Node(c)
                    cur.right = r
                    q.append(r)
    return root


sl = Solution()
root1 = ["-", "a", "-", "", "", "b", "c"]
root2 = ["+", "+", "a", "b", "c"]
r1, r2 = map(build_tree, map(deque, [root1, root2]))

# print(r1, r2)
print(sl.checkEquivalence(r1, r2))
