'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        def fxr_minheap():
            """
            Runtime: 72 ms, faster than 81.55% of Python3 online submissions for High Five.

            T: O(nlogn)
            """
            id_to_scores5 = defaultdict(list)
            for id, score in items:
                # if len(id_to_scores5[id]) < 5:
                #     heappush(id_to_scores5[id], score)
                # else:
                #     if score > id_to_scores5[id][0]:
                #         heappushpop(id_to_scores5[id], score)
                heappush(id_to_scores5[id], score)
                if len(id_to_scores5[id]) > 5:
                    heappop(id_to_scores5[id])
            res = []
            for id in sorted(id_to_scores5.keys()):
                res.append([id, sum(id_to_scores5[id])//5])
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
                avg = sum(sorted(id_to_scores[id], reverse=True)[:5])//5
                res.append([id, avg])
            return res
