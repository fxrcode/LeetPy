"""
✅ GOOD Greedy
tag: medium, greedy, sort
Lookback:
- similar to 316, based on lexical order
【宫水三叶の相信科学系列】为什么根据「拼接结果的字典序大小」决定「其在序列里的相对关系」是正确的
- 1st time `__lt__(x,y)`
"""
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def os():
            """
            Runtime: 40 ms, faster than 90.49% of Python3 online submissions for Largest Number.

            Code is easy
            """

            class LargerNumKey(str):
                def __lt__(x, y):
                    """
                    what does it mean? it means order by reverse order
                    """
                    return x + y > y + x

            largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
            return "0" if largest_num[0] == "0" else largest_num

        """
        def fxr_WA():
            numstr = [str(n) for n in nums]
            numstr.sort(reverse=True)
            return "".join(numstr)
        """

        # return fxr_WA()
        return os()


sl = Solution()
print(sl.largestNumber(nums=[10, 2]))
print(sl.largestNumber(nums=[4, 42]))
print(sl.largestNumber([4, 45]))
print(sl.largestNumber(nums=[3, 30, 34, 5, 9]))
