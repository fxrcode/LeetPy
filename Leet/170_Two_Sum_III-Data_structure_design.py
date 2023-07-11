"""
https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1179/
Leetcode Explore: Hash Table. Conclusion
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.
"""

from collections import defaultdict


class TwoSum:
    """
    Runtime: 320 ms, faster than 95.31% of Python3 online submissions for Two Sum III - Data structure design.

    XXX: carefully handle duplicate numbers!
    eg: ["TwoSum","add","find"]
    [[],[0],[0]]

    T: add: O(1), find: O(N)
    M: O(N)
    """

    def __init__(self):
        self.seen = defaultdict(int)

    def add(self, number: int) -> None:
        self.seen[number] += 1

    def find(self, value: int) -> bool:
        for n in self.seen:
            if value - n in self.seen:
                if n != value // 2:
                    return True
                elif self.seen[n] > 1:
                    return True
        return False

        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)
