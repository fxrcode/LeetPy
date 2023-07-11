"""
https://leetcode.com/discuss/interview-question/354854/Facebook-or-Phone-Screen-or-Cut-Wood
Leetcode Explore: Binary Search - More Practice II

Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.

Example 1:
Input: wood = [5, 9, 7], k = 3
Output: 5
Explanation:
5 -> 5
9 -> 5 + 4
7 -> 5 + 2

Example 2:
Output: 4
Explanation:
5 -> 4 + 1
9 -> 4 * 2 + 1
7 -> 4 + 3

Example 3:
Input: wood = [1, 2, 3], k = 7
Output: 0
Explanation: We cannot make it.

Example 4:
Input: wood = [232, 124, 456], k = 7
Output: 114
Explanation: We can cut it into 7 pieces if any piece is 114 long, however we can't cut it into 7 pieces if any piece is 115 long.
"""


from typing import List


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L: List[int], k: int) -> int:
        """
        def f(c) -> bool:
            # BUG: This makes f(c) into F,F,F,T,T,T model, so align with zhijun_liao's template: minimum k, s.t f(k) is True
            count = 0
            for l in L:
                count += l // c
            if count <= k:
                return True
            return False

        def bin_search_WA():
            l, r = 1, min(L)
            while l < r:
                mid = (l+r)//2
                if f(mid):
                    r = mid
                else:
                    l = mid+1
            return l
        """

        def f_fxr(c) -> bool:
            count = 0
            for l in L:
                count += l // c
                # This >= logic follows same defination as given in question, but need to tune zhijun's template!
                if count >= k:
                    return True
            return False

        def bin_search():
            l, r = 1, min(L)
            res = 0
            while l < r:
                mid = (l + r) // 2
                if f_fxr(mid):
                    # trick: https://leetcode.com/discuss/interview-question/354854/Facebook-or-Phone-Screen-or-Cut-Wood/352665
                    # still using zhijun's template,
                    res = mid
                    l = mid + 1
                else:
                    r = mid
            return res

        def bin_search_fxr():
            """
            XXX: must be clear, what is constant, what is variable in terms of bool func f!!!

            According to f_fxr definition (same defination as given in question), larger k <=> less c.
            So f_fxr makes c's search space into c=[1,2,3,4,5,...] => [T,T,T,F,F,F,...] given L=[5,9,7],k=3.
            Since template II's return is 1st valid, so first not(f_fxr), therefore, the right answer is l-1!

            """
            l, r = 1, min(L) + 1
            while l < r:
                c = (l + r) // 2
                if f_fxr(c):
                    l = c + 1
                else:  # in terms of zhijun_liao's template === if not f_fxr(c)
                    r = c
            return l - 1

        def bf():
            c_mn, c_mx = 1, min(L)
            for c in range(c_mx, c_mn - 1, -1):
                count = 0
                for l in L:
                    count += l // c
                if count >= k:
                    return c
            return 0

        # return bf()
        return bin_search()


sl = Solution()
print(sl.woodCut(L=[1, 2, 3], k=7))
print(sl.woodCut(L=[232, 124, 456], k=7))
print(sl.woodCut(L=[5, 9, 7], k=3))
