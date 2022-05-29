"""
Tag: Easy, Math
Lookback:
Teaching Kids & Wife Programming (Day 385)
Similar
- Weekly contest 376 (Q2)
"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        def os_count_bit():
            """
            XXX: The bits slid along, and each became the "last" bit. Notice how the 0s took 1 step to remove
                and the 1s took 2 steps to remove!
            T: O(logN)
            """
            steps = 0
            binary = bin(num)[2:]
            for bit in binary:
                if bit == "1":
                    steps += 2
                else:
                    steps += 1
            return steps - 1

        def fxr():
            """
            Runtime: 25 ms, faster than 87.21% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

            T: O(logN)
            """
            nonlocal num
            jump = 0
            while num:
                if num % 2 == 1:
                    num -= 1
                else:
                    num //= 2
                jump += 1
            return jump

        return os_count_bit()


sl = Solution()
print(sl.numberOfSteps(num=14))
print(sl.numberOfSteps(num=8))
print(sl.numberOfSteps(num=0))
