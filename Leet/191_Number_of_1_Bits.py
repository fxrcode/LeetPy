"""
https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75

tag: easy, bit manipulation
Lookback
- bit manipulation common in DP/DFS (bitmask)
"""


class Solution:

    def hammingWeight(self, n: int) -> int:
        """
        Runtime: 49 ms, faster than 41.30% of Python3 online submissions for Number of 1 Bits.

        XXX: Brian Kernighan method: turn off rightmost set bit. 
        !Common snipppet used in RodCut, ReverseLL (Iter/Recur), LIS, Eulerian circuit, 3-color DFS, etc
        REF: this trick can be used in 338. Counting Bits, 847. Bitmask DFS/BFS

        T: O(logn)! because 2^n-1 > x (#ones) => n >= log(x+1)
        """
        ones = 0
        while n:
            ones += 1
            n &= (n - 1)
        return ones
