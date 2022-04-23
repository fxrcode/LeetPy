'''

GOOD (Rejection Sampling)
Tag: Probability and Statistics

[ ] REDO
'''


class Solution:

    @staticmethod
    def rand7():
        # The rand7() API is already defined for you.
        # @return a random integer in the range 1 to 7
        return 0.5

    def rand10(self):
        """
        Runtime: 319 ms, faster than 96.76% of Python3 online submissions for Implement Rand10() Using Rand7().

        DBabichev: https://leetcode.com/problems/implement-rand10-using-rand7/discuss/816210/Python-rejection-sampling-2-lines-explained
        """
        idx, r, c = 0, 0, 0
        r = rand7()
        c = rand7()
        idx = (r - 1) * 7 + c - 1
        if idx >= 40:
            return self.rand10()
        return idx % 10 + 1
