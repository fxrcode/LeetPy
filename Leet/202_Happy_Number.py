"""
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
Leetcode Explore: Hash Table. Practical Application - HashSet

tag: easy
Lookback
- modularize helper snippet: nex(n)
- detect cycle: floyd slow/fast pointer. 
- #digits(val) = log10(val)+1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Based on our exploration so far, we'd expect continually following links to end in one of three ways.
        1) It eventually gets to 1.
        2) It eventually gets stuck in a cycle.
        3) It keeps going higher and higher, up towards infinity.

        XXX: For a number with 3 digits, it's impossible for it to ever go larger than 243.
            This means it will have to either get stuck in a cycle below 243 or go down to 1. Numbers with 4
            or more digits will always lose a digit at each step until they are down to 3 digits. So we know that
            at worst, the algorithm might cycle around all the numbers under 243 and then go back to one it's
            already been to (a cycle) or go to 1. But it won't go on indefinitely, allowing us to rule out the 3rd option.
        """
        pass

        def nex(n: int) -> int:
            r = 0
            while n:
                n, dig = divmod(n, 10)
                r += dig**2
            return r

        def os_set() -> bool:
            """
            Your runtime beats 86.64 % of python3 submissions.

            Given the analysis that once a number is below 243, it's impossible to back up above 243. So it won't go more than 243 steps before goto 1 or loop.
            XXX: how to calculate Time complexity? It's a good practice!
            Since max step is 243 in the loop or reach 1, and the # digits of num is logN (base e or 2 or 10 is same).
            We get T = O(243*3 + logN + loglogN + ...) = O(logN).
            """
            seen = set()
            while n != 1 and n not in seen:
                seen.add(n)
                n = nex(n)
            return n == 1

        def folyd() -> bool:
            """
            Your runtime beats 15.38 % of python3 submissions.
            if cycle, s/f will meet and there's no 1.
            if no cycle, must stays in 1, so f will get to 1 before s.
            """
            s = f = n
            while f != 1:  # why f!= 1 rather s!=1?
                s = nex(s)
                f = nex(nex(f))
                if s == f:
                    break
            return f == 1

        return folyd()


sl = Solution()
for n in [28, 7, 1, 3, 2]:
    print(sl.isHappy(n))
# print(sl.play_999999())
# print(sl.play_116(116, 30))
# print(sl.play_116(2, 30))
