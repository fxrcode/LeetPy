'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''

from typing import List


class Solution:
    def confusingNumber(self, N: int) -> bool:
        def wangqiuc():
            """
            Runtime: 28 ms, faster than 84.89% of Python3 online submissions for Confusing Number.

            """
            nonlocal N
            x, y, cmap = N, 0, {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
            while N:
                n, m = divmod(N, 10)
                if m not in cmap: return False
                N, y = n, y * 10 + cmap[m]
            return x != y

        def fxr_brute():
            """
            Runtime: 28 ms, faster than 80.31% of Python3 online submissions for Confusing Number.

            T: O(N), M:O(N)
            TODO: without extra space (build rotate number rather string!)
            """
            nonlocal N
            mp = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
            # ns = ''
            ns = str(N)
            ns_to_rev = ''
            while N:
                d = N % 10
                if d not in [0, 1, 6, 8, 9]:
                    return False
                # ns += str(d)
                ns_to_rev += str(mp[d])
                N //= 10
            print(ns, ns_to_rev[::-1])
            return ns != ns_to_rev[::-1]

        return fxr_brute()


sl = Solution()
nn = [6, 89, 11, 25]
for n in nn:
    print(sl.confusingNumber(n))
