"""
✅ GOOD BFS
FB tag
tag: hard, Backtrack, BFS

Lookback:
- parentheses problems can be O(N) determined how much `(` & `)` need to be removed/insert to be valid.
- normal backtracking to find all answer
- 1st time saw BFS can be used to find ALL valid answer!

similar: 
- 921 (prerequisite for all Parentheses problem: Huifeng Guan)
- 2116
"""

from collections import deque
from functools import cache
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def os_backtrack():
            """
            Runtime: 824 ms, faster than 42.65% of Python3 online submissions for Remove Invalid Parentheses.

            Approach 2: Limited Backtracking!
            T: O(2^N) # worst case s = ')))))'
            """

            def count_bads(s):
                l, r = 0, 0
                for c in s:
                    if c == "(":
                        l += 1
                    elif c == ")":
                        r += 1
                        if l > 0:
                            l, r = l - 1, r - 1
                return l, r

            L, R = count_bads(s)

            ans = set()

            @cache
            def bt(s, l, r):
                if l == r == 0:
                    if (0, 0) == count_bads(s):
                        ans.add(s)
                        return
                for i in range(len(s)):
                    if s[i] in "()":
                        nei = "".join(s[:i] + s[i + 1 :])
                        if l > 0:
                            bt(nei, l - 1, r)
                        if r > 0:
                            bt(nei, l, r - 1)

            bt(s, L, R)
            return ans

        def gracemeng_bfs():
            """
            Runtime: 664 ms, faster than 44.20% of Python3 online submissions for Remove Invalid Parentheses.

            T: O(2^N)
            """

            def isval(p):
                bal = 0
                for c in p:
                    if c == "(":
                        bal += 1
                    elif c == ")":
                        bal -= 1
                        if bal < 0:
                            return False
                return bal == 0

            ans = []  # !indicate whether a valid node has been met as well
            seen = set([s])
            q = deque([(s, 0)])
            while q:
                for _ in range(len(q)):
                    cur, rm = q.popleft()
                    if isval(cur):
                        ans.append(cur)

                    if not ans:  # ! if not valid node has been met
                        for i in range(len(cur)):
                            nei = "".join(cur[:i] + cur[i + 1 :])
                            if nei not in seen:
                                q.append((nei, rm + 1))
                                seen.add(nei)
                if ans:  # ! if valid node met, other valid nodes also in same level, so we can terminate after this level
                    break
            return ans

        return gracemeng_bfs()


sl = Solution()
print(sl.removeInvalidParentheses(s="())"))
# print(sl.removeInvalidParentheses(s="()())()"))
# print(sl.removeInvalidParentheses(s="(a)())()"))
# print(sl.removeInvalidParentheses(s=")))))))))"))
