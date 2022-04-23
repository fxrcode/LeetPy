'''
✅ GOOD Recursion
tag: medium, hash, PegionHole, recursion
'''

from typing import List


class Solution:
    def prisonAfternDays(self, cells: List[int], n: int) -> List[int]:
        def dbabichev():
            """
            Runtime: 63 ms, faster than 28.79% of Python3 online submissions for Prison Cells After N Days.

            REF: https://leetcode.com/problems/prison-cells-after-n-days/discuss/717491/Python-Loop-detection-explained

            T: O(K*min(N,2^K))  # K = #cells (in this problem K=8)
            """
            def nxt(C):
                '''
                XXX: must output to new list, cuz in-place change will re-change changed states!
                '''
                res = [0] * 8
                for i in range(1, 7):
                    res[i] = int(C[i - 1] == C[i + 1])
                return res

            def prison_after_days(cells, n):
                seen = {}
                for i in range(n):
                    # use tuple to make list immutable
                    c = tuple(cells)
                    if c in seen:
                        cycle = i - seen[c]
                        return prison_after_days(cells, (n - i) % cycle)
                    else:
                        seen[c] = i
                        cells = nxt(cells)

                return cells

            return prison_after_days(cells, n)

        return dbabichev()
        '''
        def fxr_WA():
            def nxt(C):
                for i in range(1, 7):
                    if C[i - 1] == C[i + 1]:
                        C[i] = 1
                    else:
                        C[i] = 0

            for d in range(n):
                nxt(cells)
                print(cells)
            return cells

        return fxr_WA()
        '''


sl = Solution()
cells = [0, 1, 0, 1, 1, 0, 0, 1]
n = 1
print(sl.prisonAfternDays(cells, n))
