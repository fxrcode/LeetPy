"""
✅ GOOD Logic
tag: Medium, Logic
Lookback:
- insight: every knows can reduce one person from candidate, so O(N-1) to remove N-1 candidates
- similar logic to #169. Boyce-Moore Majority Algorithms
"""


class Solution:
    def findCelebrity(self, n: int) -> int:
        def knows(a, b) -> bool:
            # The knows API is already defined for you.
            # return a bool, whether a knows b
            # def knows(a: int, b: int) -> bool:
            # GIVEN API
            return True

        def os_logic():
            """
            Runtime: 1890 ms, faster than 50.85% of Python3 online submissions for Find the Celebrity.

            T: O(N) = step1: O(N-1) + step2: O(N)
            """

            def is_celebrity(cand):
                for o in range(n):
                    if cand == o:
                        continue
                    if knows(cand, o) or not knows(o, cand):
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
