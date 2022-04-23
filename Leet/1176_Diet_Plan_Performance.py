"""
✅ GOOD slide-win (unshrinkable)
Tag: Easy, slide-win, roll-hash
Lookback:
- practice on indexing (basic skills)
"""

from typing import List


class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        def rock_slide_win():
            """
            Runtime: 235 ms, faster than 74.39% of Python3 online submissions for Diet Plan Performance.

            Unshrinkable win: only outer loop
            """
            point, win = 0, 0
            for i, cal in enumerate(calories):
                win += cal
                if i >= k - 1:
                    if i > k - 1:
                        win -= calories[i - k]
                    if win < lower:
                        point -= 1
                    elif win > upper:
                        point += 1
            return point

        def fxr():
            """
            Runtime: 234 ms, faster than 75.12% of Python3 online submissions for Diet Plan Performance.
            XXX: copied #28's rolling-hash
            """

            def p(T):
                nonlocal points
                if T < lower:
                    points -= 1
                elif T > upper:
                    points += 1

            points = 0
            T = sum(calories[:k])
            p(T)
            for i in range(1, len(calories) - k + 1):
                T = T - calories[i - 1] + calories[i + k - 1]
                p(T)

            return points

        return fxr()


sl = Solution()
print(sl.dietPlanPerformance(calories=[1, 2, 3, 4, 5], k=1, lower=3, upper=3))
print(sl.dietPlanPerformance(calories=[3, 2], k=2, lower=0, upper=1))
