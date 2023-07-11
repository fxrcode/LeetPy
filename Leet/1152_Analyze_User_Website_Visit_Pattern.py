"""
✅ GOOD Pythonic
tag: medium, Amazon
Lookback:
- itertools.* returns TUPLE, so you can use it as KEY.
- zip, itertools, Counter is so handy!
- Counter.update(iterable) updates the freq.
"""
from collections import Counter, defaultdict
from itertools import combinations
from typing import List


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        def shreyshrey_pythonic():
            """
            Runtime: 65 ms, faster than 70.46% of Python3 online submissions for Analyze User Website Visit Pattern.

            """
            users = defaultdict(list)
            for u, t, w in sorted(
                zip(username, timestamp, website), key=lambda x: (x[0], x[1])
            ):
                users[u].append(w)

            patterns = Counter()
            for u, webs in users.items():
                patterns.update(Counter(set(combinations(webs, 3))))
            return max(sorted(patterns), key=patterns.get)

        return shreyshrey_pythonic()


sl = Solution()
print(
    sl.mostVisitedPattern(
        username=["ua", "ua", "ua", "ub", "ub", "ub"],
        timestamp=[1, 2, 3, 4, 5, 6],
        website=["a", "b", "a", "a", "b", "c"],
    )
)
