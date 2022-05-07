"""
✅ GOOD Logic
Tag: Easy, Logic
Lookback:
- Totally logic, rather than DSA
- Insights: students order doesn't matter, reminds me #1498
"""

from collections import Counter, deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        def lee215():
            """
            Runtime: 63 ms, faster than 29.46% of Python3 online submissions for Number of Students Unable to Eat Lunch.

            Crux: Since students can go round and round again. So the order of them really does not matter.
            reminds me #1498
            """
            cnt = Counter(students)
            n, k = len(students), 0
            while k < n and cnt[sandwiches[k]]:
                cnt[sandwiches[k]] -= 1
                k += 1
            return n - k

        return lee215()

        def fxr():
            # Runtime: 77 ms, faster than 11.58% of Python3 online submissions for Number of Students Unable to Eat Lunch.
            nonlocal students, sandwiches
            students, sandwiches = deque(students), deque(sandwiches)
            while True:
                l = len(students)
                for _ in range(l):
                    if students[0] == sandwiches[0]:
                        students.popleft()
                        sandwiches.popleft()
                    else:
                        students.append(students.popleft())
                if l == len(students):
                    break
            return len(students)

        return fxr()


sl = Solution()
print(sl.countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
print(sl.countStudents(students=[1, 1, 1, 0, 0, 1], sandwiches=[1, 0, 0, 0, 1, 1]))
