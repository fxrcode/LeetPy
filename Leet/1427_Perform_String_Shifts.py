'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

Metacognition:
* I directly recognize it's like circular buffer, then shift accordingly to get the final starting point.
* But I do the % during shift, rather get the total shift, then do 1-time % as in OS.
'''


from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        def os():
            """
            Runtime: 32 ms, faster than 70.04% of Python3 online submissions for Perform String Shifts.

            """
            left_shift = 0
            for d, a in shift:
                if d == 1:
                    a = -a
                left_shift += a
            left_shift %= len(s)
            r = s[left_shift:]+s[:left_shift]
            return r

        def fxr():
            """
            Runtime: 42 ms, faster than 8.95% of Python3 online submissions for Perform String Shifts.

            AC in 1min!
            """
            n = len(s)
            p = 0
            for d, a in shift:
                if d == 0:
                    p = (p + n + a) % n
                else:
                    p = (p+n-a) % n
            ret = s[p:] + s[:p]
            return ''.join(ret)

        return fxr()


sl = Solution()
print(sl.stringShift(s="abc", shift=[[0, 1], [1, 2]]))
print(sl.stringShift(s="abc", shift=[[0, 1], [1, 20]]))
print(sl.stringShift(s="abc", shift=[[0, 20], [1, 2]]))
# print(sl.stringShift(s="abcdefg", shift=[[1, 1], [1, 1], [0, 2], [1, 3]]))
