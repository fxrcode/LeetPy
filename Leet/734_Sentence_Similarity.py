'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        def fxr():
            """
            Runtime: 48 ms, faster than 64.79% of Python3 online submissions for Sentence Similarity.

            AC in 1.
            T: O(N+P)
            """
            sets = set()
            if len(sentence1) != len(sentence2):
                return False

            for a, b in similarPairs:
                sets.add((a, b))

            for w1, w2 in zip(sentence1, sentence2):
                # print(w1,w2)
                if w1 == w2:
                    continue
                if (w1, w2) not in sets and (w2, w1) not in sets:
                    return False
            return True
