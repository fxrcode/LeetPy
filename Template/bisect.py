from bisect import bisect_left, bisect_right
from os import stat


class Solution:
    """Binary Search template
    Use case
    ---
    * Sorted Array
    * find better solution than O(N)
    * OOXX pattern

    Complexity
    ---
    Time: O(logN)
    Space: O(1)
    """

    def binary_search_9chap(self, nums, target):
        # 9chap template, always correct but complicate
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        # must be start+1 < end!
        while start + 1 < end:
            # The result of division is always a float
            # mid = (start+end)/2

            mid = (start + end) // 2

            # do <, =, > case first, then we can check if = can be merge into other case
            if nums[mid] < target:
                start = mid
            elif nums[mid] == target:
                end = mid
            else:
                end = mid

        # when out of loop, start is adjacent to end. (start+1 >= end)
        # if we want to get 1st postition of target, then we check start before end
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        # if we got here, means we didn't find target
        return -1

    def binary_search(array) -> int:
        """
        XXX: Most Generalized Binary Search: Minimize k, s.t. condition(k) is True

        [Python] Powerful Ultimate Binary Search Template. Solved many problems
        https://leetcode.com/discuss/general-discussion/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems
        Only 3 parts to change to apply this template:

        1) Correctly initialize the boundary variables left and right to specify search space. Only one rule: set up the boundary to include all possible elements;
        2) Decide return value. Is it return left or return left - 1?
            !Remember this: after exiting the while loop, left is the minimal k​ satisfying the condition function;
        3) Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.

        For the interval notation, Professor E.W. Dijkstra favors left closed right open interval notation and explained why we benefit from this notation in his post which was published in 1982.
        https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html
        """
        search_space = range(100)

        def feasible(value) -> bool:
            pass

        # could be [0, n], [1, n] etc. Depends on problem
        l, r = min(search_space), max(search_space)
        while l < r:
            mid = (l + r) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l

    """
    XXX: Common snippet (bisect)
    https://www.geeksforgeeks.org/binary-search-bisect-in-python/
    https://docs.python.org/3/library/bisect.html

    !The bisect() functions are useful for finding insertion points but can be TRICKY
     or AWKWARD to use for common searching tasks. The following five functions
     show how to transform them into the standard lookups for sorted lists:
    """

    @staticmethod
    def index(a, x):
        "Locate the leftmost value exactly equal to x"
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return i
        raise ValueError

    @staticmethod
    def find_lt(a, x):
        "Find rightmost value less than x"
        i = bisect_left(a, x)
        if i:
            return a[i - 1]
        raise ValueError

    @staticmethod
    def find_le(a, x):
        "Find rightmost value less than or equal to x"
        i = bisect_right(a, x)
        if i:
            return a[i - 1]
        raise ValueError

    @staticmethod
    def find_gt(a, x):
        "Find leftmost value greater than x"
        i = bisect_right(a, x)
        if i != len(a):
            return a[i]
        raise ValueError

    @staticmethod
    def find_ge(a, x):
        "Find leftmost item greater than or equal to x"
        i = bisect_left(a, x)
        if i != len(a):
            return a[i]
        raise ValueError


test = Solution()
print(test.bin_search([1, 2, 3, 5, 9], 10))
print(test.bin_search([1, 2, 3, 5, 9], 3))
print(test.bin_search([1, 2, 3, 5, 9], 9))
print(test.bin_search([1, 2, 3, 5, 9], 1))
