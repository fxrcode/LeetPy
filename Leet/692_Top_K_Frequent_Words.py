"""
C3.ai mianjing
tag: medium, 
Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
"""

from collections import Counter
from heapq import heapify, heappop, heappush, nsmallest
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        def liner_3():
            """
            Runtime: 96 ms, faster than 30.65% of Python3 online submissions for Top K Frequent Words.

            https://leetcode.com/problems/top-k-frequent-words/discuss/108348/Python-3-solution-with-O(nlogk)-and-O(n)/776726
            T: O(nlogk)

            ! nsmallest is super handy with key lambda!
            """
            F = Counter(words)
            tmp = nsmallest(k, F.items(), key=lambda x: (-x[1], x[0]))
            return [w for w, f in tmp]

        def cixuuz():
            """
            Runtime: 60 ms, faster than 78.51% of Python3 online submissions for Top K Frequent Words.

            https://leetcode.com/problems/top-k-frequent-words/discuss/108348/Python-3-solution-with-O(nlogk)-and-O(n)
            T: O(nlogk)

            top K, so minheap (size=k).
            ! must use helper class for `__lt__` so as pop smaller (freq in natural order; break freq tie by reverse-lexi-order)
            """

            class Word:
                def __init__(self, freq, word) -> None:
                    self.f = freq
                    self.w = word

                def __lt__(self, other):
                    if self.f == other.f:
                        return self.w > other.w
                    return self.f < other.f

            C = Counter(words)
            pq = []
            for w, c in C.items():
                heappush(pq, Word(c, w))
                if len(pq) > k:
                    heappop(pq)
            res = [heappop(pq).w for _ in range(k)]
            return res[::-1]

        def hjwoo():
            """
            REF: https://leetcode.com/problems/top-k-frequent-words/discuss/1547242/Simple-Python-solution
            Runtime: 54 ms, faster than 75.40% of Python3 online submissions for Top K Frequent Words.

            T: O(klogN + N)
            """
            word_counts = Counter(words)
            # build max heap
            pq = []
            for word, counts in word_counts.items():
                pq.append((-counts, word))
            heapify(pq)

            return [heappop(pq)[1] for _ in range(k)]

        # return hjwoo()
        # return cixuuz()
        return liner_3()

        def fxr_WA():
            """
            Failed for ["i", "love", "leetcode", "i", "love"], k = 1. Should return 'i', rather 'love'

            """
            C = Counter(words)
            # top k => min k
            mink = []
            for w, f in C.items():
                heappush(mink, (f, w))
                if len(mink) > k:
                    heappop(mink)

            sw = sorted(mink, key=lambda tu: (-tu[0], tu[1]))
            return [w for f, w in sw]


sl = Solution()
print(sl.topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=1))
print(sl.topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2))
print(
    sl.topKFrequent(
        words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
        k=4,
    )
)
