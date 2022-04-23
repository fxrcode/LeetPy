'''
Top Interview Questions
tag: math, Easy

[ ] TODO: base conversion
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def archit91():
            """
            https://leetcode.com/problems/power-of-three/discuss/1178701/Power-Of-Three-or-Loops-Recursive-Direct-Approach-or-Multiple-Solutions-Explained-w-Clean-Code
            Runtime: 111 ms, faster than 45.60% of Python3 online submissions for Power of Three.
            T: O(log3(n))， M: O(1)
            """
            def iter(n):
                if n < 1:
                    return False
                while n % 3 == 0:
                    n //= 3
                return n == 1

            return iter(n)

        return archit91()

        def fxr():
            """
            Runtime: 174 ms, faster than 13.53% of Python3 online submissions for Power of Three.
            T: O(log3(n))， M: O(log3(n))
            """
            def rec(n):
                if n <= 1: return n == 1
                return n % 3 == 0 and rec(n // 3)

            return rec(n)


sl = Solution()
for n in [0, 9, 27, 28]:
    print(sl.isPowerOfThree(n))