"""
✅ GOOD Stack
Tag: Medium, Stack, Skill
Lookback:
- how to impl brute force?
- smart use of Stack
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        def rock_stack():
            """
            Runtime: 97 ms, faster than 98.54% of Python3 online submissions for Remove All Adjacent Duplicates in String II.
            T: O(N)
            """
            stk = []  # hold pair of [char, freq]
            for c in s:
                if not stk or stk[-1][0] != c:
                    stk.append([c, 1])
                else:
                    stk[-1][1] += 1
                    if stk[-1][1] == k:
                        stk.pop()
            return "".join(c * cnt for c, cnt in stk)

        return rock_stack()

        def sandyz1000_brute():
            """
            https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
            The expression list (in for/while statement) is evaluated ONCE! Careful when you need len and modify collections in loop.
            """
            nonlocal s
            i = 0
            while i <= len(s) - k:
                if s[i] * k in s:
                    s = s.replace(s[i] * k, "")
                    i = 0
                else:
                    i += 1
            return s


sl = Solution()
print(sl.removeDuplicates(s="abcd", k=2))
print(sl.removeDuplicates(s="deeedbbcccbdaa", k=3))
