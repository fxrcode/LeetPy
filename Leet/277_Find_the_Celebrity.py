"""
✅ GOOD Logic
tag: Medium, Logic
Lookback:
- insight: every knows can reduce one person from candidate, so O(N-1) to remove N-1 candidates
- similar logic to #169. Boyce-Moore Algorithms
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

from secrets import choice


class Solution:
    def findCelebrity(self, n: int) -> int:
        def knows(a, b) -> bool:
            # GIVEN API
            return choice([True, False])

        def os_logic():
            """
            Runtime: 1895 ms, faster than 56.44% of Python3 online submissions for Find the Celebrity.

            T: O(N) = step1: O(N-1) + step2: O(N)
            """

            def is_celebrity(i):
                for j in range(n):
                    if i == j:
                        continue
                    if knows(i, j) or not knows(j, i):
                        return False
                return True

            candidate = 0
            # step 1: narrow down candidate
            for i in range(n):
                if knows(candidate, i):
                    candidate = i
            # step 2: verify it's REAL celebrity
            if is_celebrity(candidate):
                return candidate
            return -1
