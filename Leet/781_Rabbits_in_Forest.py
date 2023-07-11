"""
tag: Pigeonhole, Medium

Lookback:
- check 164. Maximum Gap

"""

from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        def premnath1():
            """
            Runtime: 47 ms, faster than 48.76% of Python3 online submissions for Rabbits in Forest.

            T: O(N)
            """
            d = {}
            count = 0
            for i in answers:
                # add 1 if rabbit says 0 other rabbits have same color
                if i == 0:
                    count += 1
                else:
                    # check if i is present in dictionary or not
                    # and also check whether the frequency of i and value of i is same or not
                    # For example [2,2,2] and [2,2] has the same result (i.e) 3 but [2,2,2,2] should
                    # be seperated into two groups and the result will be 6
                    # So we are again initializing the i value to 0
                    if i not in d or i == d[i]:
                        d[i] = 0
                        count += 1 + i
                    else:
                        d[i] += 1

        return premnath1()


sl = Solution()
print(sl.numRabbits([1, 1, 2]))
print(sl.numRabbits([2, 2, 2, 2, 3, 4]))
