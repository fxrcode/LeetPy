"""
✅ GOOD String (Parentheses)
FB tag (High Freq)
tag: medium, stack, greedy

Lookback
- Huifeng's greedy analysis is GREAT

Similar
- 301
- 1963
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        def rock_stk():
            """
            https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/181086/JavaPython-3-two-one-pass-codes-space-O(n)-and-O(1)-respectively
            1. if encounter '(', push '(' into stack;
            2. ow, ')', check if there is a matching '(' on top of stack; if no, increase the counter by 1; if yes, pop it out;
            4. after the loop, count in the un-matched characters remaining in the stack.
            """
            stk, cnt = [], 0
            for c in s:
                if c == "(":
                    stk.push(c)
                elif not stk:
                    cnt += 1
                else:
                    stk.pop()
            return cnt + len(stk)

        def huifeng_guan_greedy():
            """
            Runtime: 43 ms, faster than 48.43% of Python3 online submissions for Minimum Add to Make Parentheses Valid.

            https://www.youtube.com/watch?v=Sv5Xb-kfDok
            Q: How did Huifeng Guan analyze the Greedy correctness?
            A: Use concrete example: s = (()))((

            Stack: (**)
            Greedy:  count-> # un-matched left '('

            (( ...       count = 2
            (() ...      count = 1
            (()) ...     count = 0
            (())) ...    count = -1 => count = 0   (by +1 left)
            (()))( ...   count = 1
            (()))((      count = 2 => count = 0    (by +2 right)

            """
            count, ret = 0, 0
            for c in s:
                if c == "(":
                    count += 1
                else:
                    count -= 1
                if count == -1:
                    ret += 1
                    count = 0
            ret += count
            return ret
