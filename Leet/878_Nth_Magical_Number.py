'''
✅ GOOD Binary Search (generic bisect)

Division problems:
* Wood cut
* Split Array Largest Sum
* Three Equal parts

Kth object problems:
* Find K-th smallest pair distance
* K-th smallest prime fraction
* K-th smallest Number in Multiplication table
* N-th Magical Number

Daily Challenge (Dec 11)

A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 10^9 + 7.
'''

from math import lcm


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def jigong_bisect():
            """
            Runtime: 32 ms, faster than 67.26% of Python3 online submissions for Nth Magical Number.

            济公学院: 2/4 -- 二分搜索例题精讲
            https://www.youtube.com/watch?v=jTiki726mpI
            """
            def f(v, n, A, B):
                """
                !if there're >= N magicall int which are <= v
                Go for an example, ie a,b=4,2. Then you can easily find math of #count
                """
                return v//A + v//B - v//lcm(A, B) >= n

            l, r = 0, n*min(a, b)
            while l < r:
                m = (l+r)//2
                if f(m, n, a, b):
                    r = m
                else:
                    l = m + 1
            return l

        return jigong_bisect()

        def fxr_brute():
            """
            TLE: 44 / 70 test cases passed.
            Last executed input:
            1000000000
            40000
            40000
            """
            nonlocal a, b
            if a > b:
                a, b = b, a
            i, j, k = 1, 1, 0
            v = None
            while k < n:
                ia, jb = i * a, j * b
                if ia < jb:
                    v = ia
                    i += 1
                    k += 1
                elif ia > jb:
                    v = jb
                    j += 1
                    k += 1
                else:
                    i += 1
            return v


sl = Solution()
print(sl.nthMagicalNumber(1, 2, 3))
print(sl.nthMagicalNumber(5, 2, 4))
