'''

tag: Easy, Hash
'''

from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def lee215():
            """
            https://leetcode.com/problems/find-common-characters/discuss/247560/Python-1-Line

            dict 1 & dict 2 will intersect the two counters here, the lowest counts are preserved;
            elements() is Counter's method, it just take the elements as many times as their counts
            Ref: https://docs.python.org/3/library/collections.html#collections.Counter
            """
            res = Counter(words[0])
            for a in words:
                res &= Counter(a)
            return list(res.elements())

        return lee215()

        def rock():
            """
            https://leetcode.com/problems/find-common-characters/discuss/247558/JavaPython-3-12-liner-and-7-liner-count-and-look-for-minimum.

            """
            cnt = Counter(words[0])
            for s in words:
                cnt2 = Counter(s)
                for k in cnt.keys():
                    cnt[k] = min(cnt[k], cnt2[k])
            return cnt.elements()


sl = Solution()
print(sl.commonChars(words=["bella", "label", "roller"]))
