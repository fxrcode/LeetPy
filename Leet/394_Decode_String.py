"""
✅ GOOD recursion (772. calculator family)
https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1379/
Leetcode explore Queue & Stack: Conclusion

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
"""
from collections import deque


class Solution:
    def decodeString_iter(self, s: str) -> str:
        """
        Runtime: 32 ms, faster than 58.89% of Python3 online submissions for Decode String.

        https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
        """
        stk = []
        cur_str = ""
        k = 0
        for c in s:
            if c == "[":
                stk.append((cur_str, k))
                cur_str, k = "", 0
            elif c == "]":
                last_str, last_k = stk.pop()
                # BUG: cur_string += last_str * last_k
                cur_str = last_str + last_k * cur_str
            elif c.isdigit():
                k = k * 10 + int(c)
            else:
                cur_str += c
        return cur_str

    def decodeString(self, s: str) -> str:
        """
        Your runtime beats 24.07 % of python3 submissions.

        https://leetcode.com/problems/decode-string/discuss/810400/Clean-Java-Solution-beats-100-oror-StringBuilder
        Recursive solution, use global i so you don't need to pop s as in labuladong calculator.

        """

        def recur(s):
            res = ""
            k = 0
            while s:
                c = s.popleft()
                if c == "[":
                    inner = recur(s)
                    res += k * inner
                    k = 0
                elif c.isalpha():
                    res += c
                elif c.isdigit():
                    k = k * 10 + int(c)
                else:  # ']'
                    break
            return res

        return recur(deque(s))


sl = Solution()
ss = [
    # "10[az]",
    "3[a]2[bc]",
    # "3[a2[c]]",
]
for s in ss:
    print(sl.decodeString(s))
