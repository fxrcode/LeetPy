"""
https://leetcode.com/explore/learn/card/binary-search/137/conclusion/977/
Leetcode Explore: Binary Search - Conclusion

Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest character in the array that is larger than target.
"""


from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """
        Your runtime beats 59.16 % of python3 submissions.

        AC in 1.
        XXX: notice that template II doesn't ensure condition(k) is true after execution! Requires Post-processing
        eg. [1,2,4], target= 5
        """
        l, r = 0, len(letters) - 1
        while l < r:
            mi = (l + r) // 2
            if letters[mi] > target:
                r = mi
            else:
                l = mi + 1
        print(l, r)
        if l == len(letters) - 1 and letters[l] <= target:
            return letters[0]
        return letters[l]


sl = Solution()
print(sl.nextGreatestLetter(letters=["c", "f", "j"], target="z"))
