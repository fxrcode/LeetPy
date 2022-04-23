"""
https://leetcode.com/problem-list/79h8rn6/
Top 100 Liked Questions

Daily Challenge (Nov 19)

Google phone screen 2016

barstow123: Is this the best interview question? Possibly, possibly not. This one is really easy to memorize, and I think that's kind of the problem. If you work hard and study efficiently, results in the form of high paying job offers will come your way.
XXX: O(N) = O(2N) = O(3N). so you can traverse multi-times!
"""


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def os():
            """
            XXX: use O(N) space, so res for l2r, then r2l on the fly.

            Memory Usage: 21.1 MB, less than 81.68% of Python3 online submissions for Product of Array Except Self.
            """
            m = len(nums)
            res = [1] * m
            for i in range(1, m):
                res[i] = nums[i-1] * res[i-1]

            R = 1
            # XXX: Prefer OS's indexing, use [i] to set consistently!
            for i in reversed(range(m)):
                res[i] = res[i] * R
                R *= nums[i]

            '''
            R = 1
            for i in range(m-2, -1, -1):
                R = R * nums[i+1]
                res[i] = res[i] * R
            '''
            return res

        def fxr():
            """
            Runtime: 244 ms, faster than 66.42% of Python3 online submissions for Product of Array Except Self.

            T: O(N), M: O(2N)
            """
            m = len(nums)
            l2r = [1] * m
            r2l = [1] * m
            for i in range(m-1):
                l2r[i+1] = l2r[i] * nums[i]
            print(l2r)
            for i in range(m-1, 0, -1):
                r2l[i-1] = r2l[i] * nums[i]
            print(r2l)
            res = list(map(lambda tu: tu[0]*tu[1], zip(l2r, r2l)))
            return res

        return os()


sl = Solution()
print(sl.productExceptSelf(nums=[5, 2, 3, 4]))
