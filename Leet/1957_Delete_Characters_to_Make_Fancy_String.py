"""
tag: easy
Lookback:
- neat logic in rock
"""


class Solution:
    def makeFancyString(self, s: str) -> str:
        def rock():
            """
            Runtime: 769 ms, faster than 59.22% of Python3 online submissions for Delete Characters to Make Fancy String.

            https://leetcode.com/problems/delete-characters-to-make-fancy-string/discuss/1389256/JavaPython-3-Count-put-into-StringBuilderlist-and-join-it.
            T: O(N)
            """
            cnt, a = 0, []
            for i, c in enumerate(s):
                if i > 0 and c == s[i - 1]:
                    cnt += 1
                else:
                    cnt = 1
                if cnt < 3:
                    a.append(c)
            return "".join(a)

        def fxr():
            """
            Runtime: 1193 ms, faster than 24.08% of Python3 online submissions for Delete Characters to Make Fancy String.
            T: O(N)
            """
            l = r = 0
            cnt = 0
            ls = list(s)

            while l < len(ls):
                while r < len(ls) and ls[r] == ls[l]:
                    if cnt >= 2:
                        ls[r] = ""
                    r += 1
                    cnt += 1
                # r oor or ls[r] != ls[l], found segment [l:r]
                cnt = 0
                l = r

            return "".join(ls)

        return fxr()


sl = Solution()
print(sl.makeFancyString("leeetcode"))
print(sl.makeFancyString("aaabaaaa"))
print(sl.makeFancyString("aab"))
