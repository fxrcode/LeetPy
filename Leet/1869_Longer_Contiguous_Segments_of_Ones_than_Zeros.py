"""
tag: easy, skills
Lookback:
- TODO: more practice
"""


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def os_cn():
            # Runtime: 62 ms, faster than 11.06% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.
            mx0, mx1 = 0, 0
            cnt = 0
            prev = "#"
            for c in s + "#":
                if prev == c:
                    cnt += 1
                else:
                    if prev == "0":
                        mx0 = max(mx0, cnt)
                    elif prev == "1":
                        mx1 = max(mx1, cnt)
                    cnt = 1
                prev = c
            print(mx1, mx0)
            return mx1 > mx0

        return os_cn()

        def antonyakoviev():
            # Runtime: 39 ms, faster than 66.01% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.
            mx_one, mx_zero, cur_one, cur_zero = 0, 0, 0, 0
            for c in s:
                if c == "1":
                    cur_zero = 0
                    cur_one += 1
                else:
                    cur_zero += 1
                    cur_one = 0

                mx_one = max(mx_one, cur_one)
                mx_zero = max(mx_zero, cur_zero)
            return mx_one > mx_zero

        def fxr():
            """
            Runtime: 44 ms, faster than 52.64% of Python3 online submissions for Longer Contiguous Segments of Ones than Zeros.

            """
            ones, zeros = 0, 0
            l, r = 0, 0

            o, z = False, False
            while l < len(s):
                if s[l] == "1":
                    o = True
                    z = False
                else:
                    z = True
                    o = False
                cnt = 0
                while r < len(s) and s[r] == s[l]:
                    cnt += 1
                    r += 1
                # now r out of range or switch 0 <-> 1
                if o:
                    ones = max(ones, r - l)
                if z:
                    zeros = max(zeros, r - l)
                l = r
            print(ones, zeros)
            return ones > zeros

        return fxr()


sl = Solution()
for s in ["1101", "111000", "110100010", "01111110"]:
    print(sl.checkZeroOnes(s))
