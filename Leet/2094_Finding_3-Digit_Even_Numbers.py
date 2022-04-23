'''
Weekly Contest 270 (Dec 4, 2021)

Q1: Simple
'''

from typing import List


class Solution:
    def findEvenNumbers_fxr(self, digits: List[int]) -> List[int]:
        digits.sort()

        def li2v(path):
            v = 0
            v += path[0]*100
            v += path[1]*10
            v += path[2]
            return v

        def bt(start, path, used, res):
            if len(path) == 3:
                if path[-1] % 2 == 0:
                    res.append(li2v(path))
                return
            for i in range(start, len(digits)):
                d = digits[i]
                if d == 0:
                    continue
                if i - 1 >= 0 and digits[i] == digits[i-1] and i-1 not in used:
                    continue
                # XXX: missed `i` check used.
                #    I forgot dedup permutation!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                if i not in used:
                    used.add(i)
                    bt(i+1, path + [d], used, res)
                    used.remove(i)

        res = []
        bt(0, [], set(), res)
        return res
