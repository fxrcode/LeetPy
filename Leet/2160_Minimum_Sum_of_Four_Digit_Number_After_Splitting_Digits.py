"""
tag: easy, math, DFS

similar: 258.Add Digits
Lookback
- find pattern before coding!
- math problem generally can solve with logic, rather brute force enumeration 
"""

from itertools import permutations


class Solution:
    def minimumSum(self, num: int) -> int:
        def fatamorgana_math():
            """
            Runtime: 43 ms, faster than 59.57% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.

            Assume they are a <= b <= c <= d, the sum is minimum when new1 = ac and new2 = bd.
            REF: https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/discuss/1747018/Python-simple-and-fast-with-explanation-no-permutation
            """
            # A = sorted([int(c) for c in str(num)])
            # return sum([A[0] * 10 + A[1] * 10 + A[2] + A[3]])
            A = sorted([int(c) for c in str(num)], reverse=True)
            res = 0
            even_iter = False
            pos = 0
            for v in A:
                res += v * (10**pos)
                if even_iter:
                    pos += 1
                    even_iter = False
                else:
                    even_iter = True
            return res

        return fatamorgana_math()

        def fxr():
            """
            Runtime: 44 ms, faster than 56.09% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.

            """

            def sum2slice(lis):
                # return sum(int(''.join(map(int, lis))))
                return sum(int("".join(map(str, li))) for li in lis)

            def bt(A, used, news, res):
                if len(used) == 4:
                    mn = min(sum2slice((news[:i], news[i:])) for i in range(1, 4))
                    print(used, news, mn)
                    res.append(mn)
                    return
                for i in range(4):
                    if i > 0 and A[i - 1] == A[i] and i - 1 not in used:
                        continue
                    if i not in used:
                        used.add(i)
                        bt(A, used, news + [A[i]], res)
                        used.remove(i)

            A = [int(c) for c in str(num)]
            A.sort()
            res = []
            bt(A, set(), [], res)
            return min(res)
            """
            Runtime: 79 ms, faster than 5.30% of Python3 online submissions for Minimum Sum of Four Digit Number After Splitting Digits.

            perms = permutations([int(c) for c in str(num)])

            mn = 9999
            for p in perms:
                mn = min(mn,
                         min(sum2slice((p[:i], p[i:])) for i in range(1, 4)))
            return mn
            """

        return fxr()


sl = Solution()
# num = 2932
# num = 4009
num = 2436
print(sl.minimumSum(num))
