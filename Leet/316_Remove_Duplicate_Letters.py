"""
✅ GOOD Stack
✅ GOOD Greedy
tag: medium, greedy, stack, hash
Lookback:
* same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

古城算法: 基础算法(六) -- 单调栈
Daily challenge & TuSimple phone screen
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def os_greedy():
            """
            Runtime: 39 ms, faster than 84.59% of Python3 online submissions for Remove Duplicate Letters.
            T: O(N)
            """
            stk = []
            in_stk = set()
            last_pos = {c: i for i, c in enumerate(s)}

            for i, c in enumerate(s):
                # this is to maintain only one of each character
                if c in in_stk:
                    continue

                # piecewise mono-incr stack
                while stk and c < stk[-1] and i < last_pos[stk[-1]]:
                    in_stk.remove(stk.pop())
                stk.append(c)
                in_stk.add(c)

            return "".join(stk)

        return os_greedy()


sl = Solution()
print(sl.removeDuplicateLetters(s="bcabc"))
print(sl.removeDuplicateLetters(s="cbacdcbc"))
