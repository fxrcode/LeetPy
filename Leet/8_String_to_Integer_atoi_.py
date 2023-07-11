"""
✅ GOOD FSM (DFA)
Amazon tag (easy)

Tip: Finite State Machine Designer
https://madebyevan.com/fsm/
"""
NINF, INF = -int(2**31), int(2**31 - 1)


class Solution:
    def myAtoi(self, s: str) -> int:
        def spencerwoo_dfa():
            """
            Runtime: 45 ms, faster than 29.95% of Python3 online submissions for String to Integer (atoi).

            https://leetcode.com/problems/string-to-integer-atoi/discuss/798380/Fast-and-simpler-DFA-approach-(Python-3)
            3 valid states for the DFA
            0: init
            1: got sign
            2: 0-9

            """
            v, st, sig = 0, 0, 1

            if not s:
                return 0

            for c in s:
                if st == 0:
                    if c == " ":
                        pass
                    elif c in "+-":
                        st = 1
                        if c == "-":
                            sig = -1
                    elif c.isdigit():
                        st = 2
                        v = v * 10 + int(c)
                    else:
                        return 0
                elif st == 1:
                    if c.isdigit():
                        st = 2
                        v = v * 10 + int(c)
                    else:
                        return 0
                elif st == 2:
                    if c.isdigit():
                        st = 2
                        v = v * 10 + int(c)
                    else:
                        # XXX: '-42 words' end FSM but return 0, so break rather return here
                        break
                else:
                    return 0
            # print(v)
            v = sig * v
            v = min(v, INF)
            v = max(NINF, v)
            return v

        return spencerwoo_dfa()


sl = Solution()
print(sl.myAtoi("42"))
print(sl.myAtoi("     -42"))
print(sl.myAtoi(s="4193 with words"))
print(sl.myAtoi("+-12"))
print(sl.myAtoi("00000-42a1234"))
print(sl.myAtoi("-42a1234"))
