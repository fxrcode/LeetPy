"""
✅ GOOD Math
tag: math, medium
Similar:
- Doordash: sqrt(long str), combination of 43 + 69

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def os_digits(A, B):
            """
            Runtime: 196 ms, faster than 32.64% of Python3 online submissions for Multiply Strings.

            """
            if A == "0" or B == "0":
                return "0"
            res = [0] * (len(A) + len(B))
            for i, x in enumerate(A[::-1]):
                for j, y in enumerate(B[::-1]):
                    xy = int(x) * int(y) + res[i + j]
                    ten, one = divmod(xy, 10)
                    res[i + j + 1] += ten
                    res[i + j] = one
            return "".join(map(str, res[::-1])).lstrip("0")
            # while res[-1] == 0:
            #     res.pop()
            # return "".join(map(str, res[::-1]))

        return os_digits(num1, num2)

        def fxr(l1, r1, l2, r2) -> str:
            """
            Runtime: 40 ms, faster than 65.93% of Python3 online submissions for Multiply Strings.

            TODO: https://en.wikipedia.org/wiki/Karatsuba_algorithm
                can be optimize to be O(n^log3)
            """
            print("fxr", l1, r1, l2, r2)
            if r1 - l1 < 6 or r2 - l2 < 6:
                prod = int(num1[l1 : r1 + 1]) * int(num2[l2 : r2 + 1])
                return str(prod)

            m1, m2 = (l1 + r1) // 2, (l2 + r2) // 2
            # n1_h,n1_l = num1[l1:m1+1], num1[m1+1:r1+1]
            # n2_h, n2_l = num2[l2:m2+1], num2[m2+1:r2+1]

            nh1_nh2 = fxr(l1, m1, l2, m2)
            nh1_nl2 = fxr(l1, m1, m2 + 1, r2)
            nl1_nh2 = fxr(m1 + 1, r1, l2, m2)
            nl1_nl2 = fxr(m1 + 1, r1, m2 + 1, r2)
            print(nh1_nh2, nh1_nl2, nl1_nh2, nl1_nl2)

            ans = int(nh1_nh2) * pow(10, ((r1 - (m1 + 1) + 1) + (r2 - (m2 + 1) + 1))) + int(nh1_nl2) * pow(10, (r1 - (m1 + 1) + 1)) + int(nl1_nh2) * pow(10, (r2 - (m2 + 1) + 1)) + int(nl1_nl2)
            return str(ans)

        # return fxr(0, len(num1) - 1, 0, len(num2) - 1)


sl = Solution()
print(sl.multiply("9133", "1"))
print(sl.multiply("123", "456"))
print(sl.multiply("98765", "43210"))
