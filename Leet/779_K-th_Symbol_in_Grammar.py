"""
https://leetcode.com/explore/learn/card/recursion-i/253/conclusion/1675/
Leetcode Explore Recursion I - Conclusion

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        """[summary]
        Your runtime beats 17.86 % of python3 submissions.
        XXX: bad in 1-index. need to familiar with index, +1/-1.
        BUG: careful on trap of '01'[0] returned '0', not 0!
        """
        if n == 1 and k == 1:
            return 0
        prev = self.kthGrammar(n-1, (k+1)//2)  # prev 0,1
        if k % 2:
            i = 0
        else:
            i = 1
        if prev == 0:
            return int('01'[i])
        else:
            return int('10'[i])

    # TODO: lee215's math solution


sl = Solution()
print(sl.kthGrammar(3, 1))
