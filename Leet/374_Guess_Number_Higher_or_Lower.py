'''
https://leetcode.com/explore/learn/card/binary-search/125/template-i/951/
Leetcode Explore: Binary Search - Template I
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

pick = 6


class Solution:
    def guessNumber(self, n: int) -> int:
        """
        Your runtime beats 95.17 % of python3 submissions.
        zhijun_liao's Most generalized binary search.

        XXX: understand API before you use it!
        """
        def guess(num):
            if num == pick:
                return 0
            elif num > pick:
                return -1
            else:
                return 1
        l, r = 1, n
        while l < r:
            mid = (l+r)//2
            # if guess(mid) in [0, -1]:
            if guess(mid) <= -1:
                r = mid
            else:
                l = mid + 1
        return l


sl = Solution()
print(sl.guessNumber(10))
