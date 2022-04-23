'''
Amazon Top50
Tag: easy
'''

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def rock():
            """
            Runtime: 253 ms, faster than 29.53% of Python3 online submissions for Maximum Units on a Truck.

            https://leetcode.com/problems/maximum-units-on-a-truck/discuss/999125/JavaPython-3-Sort-by-the-units-then-apply-greedy-algorithm.

            XXX: coding logic, if truckSize not able to carry all this type, just take truckSize and return!
            """
            boxTypes.sort(key=lambda x: -x[1])
            ans, cap = 0, truckSize
            for b, u in boxTypes:
                if cap >= b:
                    ans += b * u
                    cap -= b
                else:
                    ans += cap * u
                    return ans
            return ans

        return rock()


sl = Solution()
print(sl.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4))
