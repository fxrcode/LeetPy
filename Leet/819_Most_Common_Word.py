"""
✅ GOOD String (manipulation)
tag: easy, string
Lookback
- 1st use re.sub(regex, repl, s)
- str process pipeline: re.sub -> lower -> split
- gotcha: Exception if you modify dict causes len change
"""


import re
from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        def lee215():
            """
            Runtime: 30 ms, faster than 96.61% of Python3 online submissions for Most Common Word.

            """
            lw = re.sub(r"[^a-zA-Z]", " ", paragraph).lower().split()
            Filter = Counter()
            for w in lw:
                if w not in set(banned):
                    Filter[w] += 1
            return Filter.most_common(1)[0][0]

        return lee215()


sl = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sl.mostCommonWord(paragraph, banned))
