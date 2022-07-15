"""
Tag: Easy, heapq
Lookback:
- LeetCode Curated Algo 170
- when you see top-k, use heapq (minheap)
"""


from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        def fxr_minheap():
            """
            Runtime: 95 ms, faster than 65.69% of Python3 online submissions for High Five.

            T: O(n)
            """
            id_score = defaultdict(list)
            for id, score in items:
                heappush(id_score[id], score)
                if len(id_score[id]) > 5:
                    heappop(id_score[id])
            res = []
            for id in sorted(id_score.keys()):
                res.append([id, sum(id_score[id]) // 5])
            return res

        def fxr_brute():
            """
            Your runtime beats 94.35 % of python3 submissions.

            T: O(nlogn)
            """
            id_to_scores = defaultdict(list)
            for id, score in items:
                id_to_scores[id].append(score)
            res = []
            for id in sorted(id_to_scores.keys()):
                avg = sum(sorted(id_to_scores[id], reverse=True)[:5]) // 5
                res.append([id, avg])
            return res
