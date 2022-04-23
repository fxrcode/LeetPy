"""
✅ GOOD Divide & Conquer
tag: easy, D&C
Lookback:
- Damn, unable to solve easy problem after 800 solved. Not able to find recurrence relation
    - more like #23. (draw out the s with multi-bad char)
- trick of str
    - str.swapcase()
    - set(s) == set(s.swapcase())
    - max(iter, key=len)
    
[ ] REDO
"""


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def pasher13_dc():
            """
            Runtime: 75 ms, faster than 55.26% of Python3 online submissions for Longest Nice Substring.

            https://leetcode.com/problems/longest-nice-substring/discuss/1074569/Python-Fast-and-Simple-Recursive-Function%3A-Split-if-invalid-character-is-found
            T: O(n)
            """

            def dc(s):
                if len(s) < 2:
                    return ""
                ss = set(s)
                for i, c in enumerate(s):
                    if c.swapcase() not in ss:
                        nl = dc(s[:i])
                        nr = dc(s[i + 1 :])
                        return max(nl, nr, key=len)
                return s

            return dc(s)

        return pasher13_dc()

        def ye15_brute():
            """
            Runtime: 208 ms, faster than 29.02% of Python3 online submissions for Longest Nice Substring.
            T: O(N^2)
            """
            ans = ""
            for j in range(len(s)):
                for i in range(j):
                    t = s[i : j + 1]
                    if set(t) == set(t.swapcase()):
                        ans = max(ans, t, key=len)
            return ans

        """
        def fxr_WA():
            def is_nice(win):
                for c in win:
                    if not (c.lower() in win and c.upper() in win):
                        return False
                return True

            chars = set(s)
            good = set()
            for c in chars:
                if c.lower() in chars and c.upper() in chars:
                    good.add(c)
            win = set()
            mxlen = 0
            ans = ""
            l, r = 0, 0
            while r < len(s):
                c = s[r]
                r += 1
                if c in good:
                    win.add(c)
                    if is_nice(win) and r - l > mxlen:
                        print(l, r)
                        mxlen = r - l
                        ans = s[l:r]
                else:
                    # update win, len, l
                    l = r
                    win.clear()
            return ans
        """


sl = Solution()
# print(sl.longestNiceSubstring(s="YazaAay"))
print(sl.longestNiceSubstring(s="YazyaAayz"))
# print(sl.longestNiceSubstring(s="Bb"))
# print(sl.longestNiceSubstring(s="c"))
