"""
https://leetcode.com/company/google/
Easy
"""
from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        def os():
            """
            Runtime: 32 ms, faster than 69.21% of Python3 online submissions for Uncommon Words from Two Sentences.

            OS always has neater code!
            """
            count = {}
            for w in s1.split():
                count[w] = count.get(w, 0) + 1
            for w in s2.split():
                count[w] = count.get(w, 0) + 1

            return [w for w in count if count[w] == 1]

        def fxr():
            """
            Runtime: 32 ms, faster than 69.21% of Python3 online submissions for Uncommon Words from Two Sentences.

            T: O(n+m)
            """
            f1, f2 = Counter(s1.split()), Counter(s2.split())
            uncomm = []
            for w in set(f1.keys()).union(set(f2.keys())):
                cnt = 0
                if w in f1:
                    cnt += f1[w]
                if w in f2:
                    cnt += f2[w]
                if cnt == 1:
                    uncomm.append(w)
            return uncomm
