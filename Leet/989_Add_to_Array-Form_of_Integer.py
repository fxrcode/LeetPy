"""
✅ GOOD MATH (addend as carry!)
tag: easy, math
Lookback
- just take k as carry to in-place add!
- So elegant and neat, common trick in math addition/multiply.

FB tag (easy)
[ ] REDO
"""
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        def lee215():
            """
            Runtime: 309 ms, faster than 84.27% of Python3 online submissions for Add to Array-Form of Integer.

            edge case:  num=[0],k=23

            XXX: use K as a carry!
            Add it to the lowest digit,
            Update carry K
            """
            nonlocal k
            for i in range(len(num) - 1, -1, -1):
                k, num[i] = divmod(k + num[i], 10)
            if k:
                return [int(i) for i in str(k)] + num
            else:
                return num

        return lee215()


sl = Solution()
print(sl.addToArrayForm(num=[1, 2, 0, 0], k=34))
print(sl.addToArrayForm(num=[2, 7, 4], k=181))
print(sl.addToArrayForm(num=[0], k=23))
