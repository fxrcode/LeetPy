"""
https://leetcode.com/company/google/
Easy

[ ] REDO

Lookback: once I saw hint: use stack, I come up with the similar as os. But a bit buggy since I didn't have algs yet when coding.
"""
from string import ascii_lowercase


class Solution:
    def removeDuplicates(self, s: str) -> str:
        def os_replace():
            """
            TLE: 104 / 106 test cases passed.

            Onion while/for loops.
            T: O(N^2)
            """
            nonlocal s
            dups = {2 * ch for ch in ascii_lowercase}
            prev_len = -1

            # similar to ballman-ford, terminate if no optimize in last action
            while prev_len != len(s):
                prev_len = len(s)
                for d in dups:
                    # XXX: 1st time using s.replace()
                    s = s.replace(d, "")
            return s

        def os_stack():
            """
            Runtime: 104 ms, faster than 38.78% of Python3 online submissions for Remove All Adjacent Duplicates In String.
            T: O(N)
            """
            st = []
            i = 0
            while i < len(s):
                if st and s[i] == st[-1]:
                    st.pop()
                else:
                    st.append(s[i])
                i += 1
            return "".join(st)

        return os_stack()

        def fxr2_WA():
            """
            LOOKBACK: after re-read the description, I followed previous thought and modify it.
            XXX: Think outside the box!
            """
            n = len(s)
            de = set()

            def dedup():
                i = 0
                cnt = 0
                while i < n:
                    if i in de:
                        i += 1
                        continue
                    c = s[i]
                    cnt = 1
                    j = i + 1
                    while j < n and (s[j] == c or j in de):
                        if s[j] == c:
                            cnt += 1
                        j += 1
                    if cnt >= 2:
                        [de.add(k) for k in range(i, j)]
                        print(de)
                        return
                    i = j

            for i in range(n):
                dedup()

            ans = []
            for i in range(n):
                if i not in de:
                    ans.append(s[i])
            return "".join(ans)

        def fxr_WA():
            """
            BUG: without read through the whole problem, I start coding, totally misunderstood the problem!
            DON'T do it anymore
            """
            res = []
            i, n = 0, len(s) - 1
            while i < n:
                c = s[i]
                j = i + 1
                while j < n and s[j] == c:
                    j += 1
                if j == n:
                    break
                i = j
                res.append(c)
            return res


sl = Solution()
print(sl.removeDuplicates(s="abbaca"))
print(sl.removeDuplicates(s="azxxzy"))
print(sl.removeDuplicates("aaaaaaaa"))
print(sl.removeDuplicates("aababaab"))
