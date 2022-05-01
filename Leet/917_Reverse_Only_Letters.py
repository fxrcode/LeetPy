"""
✅ GOOD Hoare partition
Tag: Easy, 2ptr, Skills
Lookback:
- Don't code before fully understand problem
- Hoare partition
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def lee215_2ptr_1pass():
            """
            Runtime: 44 ms, faster than 43.33% of Python3 online submissions for Reverse Only Letters.
            T: O(N)
            """
            A, i, j = list(s), 0, len(s) - 1
            while i < j:
                while i < j and not A[i].isalpha():
                    i += 1
                while i < j and not A[j].isalpha():
                    j -= 1
                A[i], A[j] = A[j], A[i]
                i, j = i + 1, j - 1
            return "".join(A)

        return lee215_2ptr_1pass()

        def fxr_2ptr():
            """
            Runtime: 37 ms, faster than 65.98% of Python3 online submissions for Reverse Only Letters.

            T: O(2N)
            """
            ci = [i for i, c in enumerate(s) if c.isalpha()]
            l, r = 0, len(ci) - 1
            lc = list(s)
            while l < r:
                i, j = ci[l], ci[r]
                lc[i], lc[j] = lc[j], lc[i]
                l, r = l + 1, r - 1
            return "".join(lc)

        return fxr_2ptr()

        def fxr_1():
            sb = []
            for c in s:
                if c.isalpha():
                    sb.append(c)
            # sb.sort()
            res = []
            for i, c in enumerate(s):
                if c.isalpha():
                    res.append(sb.pop())
                else:
                    res.append(c)
            return "".join(res)

        return fxr()


sl = Solution()
print(sl.reverseOnlyLetters(s="ab-cd"))
print(sl.reverseOnlyLetters(s="a-bC-dEf-ghIj"))
print(sl.reverseOnlyLetters(s="Test1ng-Leet=code-Q!"))
