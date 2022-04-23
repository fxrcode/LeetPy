'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List
from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        def os_set():
            """
            Same main idea: at most one char has odd occurence.
            We can add/remove to contaer-act it when it's even
            """
            sett = set()
            for c in s:
                if c not in sett:
                    sett.add(c)
                if c in sett:
                    sett.remove(c)
            return len(sett) <= 1

        def fxr():
            """
            Runtime: 28 ms, faster than 83.87% of Python3 online submissions for Palindrome Permutation.

            AC in 1.
            """
            cnt = Counter(s)
            odd = 0
            for k, v in cnt.items():
                if v % 2 == 1:
                    odd += 1
                    if odd == 2:
                        return False
            return True
