'''
Study Plan: Programming Skills I
https://leetcode.com/study-plan/programming-skills/?progress=drmo6ys

Lookback:
- if you can't solve the current problem, relax the requirements (range 3-7 => range 1-7, range 1-3)
'''


class Solution:

    def countOdds(self, low: int, high: int) -> int:

        def yaroslav_repeta():
            """
            Runtime: 30 ms, faster than 85.56% of Python3 online submissions for Count Odd Numbers in an Interval Range.

            (high - low + 1) is number of element between high and low where half of them are odd, so 
                (high - low + 1) // 2 and additionally add 1 if high and low are odd for case when there 
                are more odd numbers than even ones (for example 1..3)

            """
            return (high - low + 1) // 2 + (high % 2 and low % 2)

        def fxr():
            """
            Runtime: 30 ms, faster than 85.56% of Python3 online submissions for Count Odd Numbers in an Interval Range.

            AC in 1. 
            """
            return (high + 1) // 2 - low // 2

        def countEvens():
            # simple follow up
            # return (high - low + 1) - fxr()
            return (high - low + 1) // 2 + (high % 2 == 0 and low % 2 == 0)
