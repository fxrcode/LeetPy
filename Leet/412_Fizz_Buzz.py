"""
https://leetcode.com/company/google/
Easy
"""
from typing import List


class Solution:
    def fizzBuzz_scalable(self, n: int) -> List[str]:
        """
        What if more mappings: eg. 3 ---> "Fizz" , 5 ---> "Buzz", 7 ---> "Jazz"
        How about 3,5,7,11,13,...? many primes mapping? then you need long condition check
        Q: How to make code scalable to primes mapping increasing?
        A: String Concatenation
        """
        ans = []
        for v in range(1, n + 1):
            divisible_by_3 = v % 3 == 0
            divisible_by_5 = v % 5 == 0

            v_str = ""
            if divisible_by_3:
                v_str += "Fizz"
            if divisible_by_5:
                v_str += "Buzz"
            if not v_str:
                v_str = str(v)
            ans.append(v_str)
        return ans

    def fizzBuzz_naive(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
