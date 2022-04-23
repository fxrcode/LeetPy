'''
✅ GODD logic (impl)
similar: 1657
tag: Easy
'''

from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        def lee215(A, B):
            """
            Runtime: 49 ms, faster than 38.10% of Python3 online submissions for Buddy Strings.

            If A == B, we need swap two same characters. Check is duplicated char in A.
            In other cases, we find index for A[i] != B[i]. There should be only 2 diffs and it's our one swap.
            """
            if len(A) != len(B): return False
            if A == B and len(set(A)) < len(A): return True
            dif = [(a, b) for a, b in zip(A, B) if a != b]
            return len(dif) == 2 and dif[0] == dif[1][::-1]

        return lee215(s, goal)

        def fxr():
            """
            Runtime: 40 ms, faster than 55.95% of Python3 online submissions for Buddy Strings.

            """
            if len(s) != len(goal):
                return False

            C, C2 = Counter(s), Counter(goal)
            dif = 0
            for c, d in zip(s, goal):
                if c != d:
                    dif += 1
            if dif == 2:
                return C == C2
            if dif == 0:
                if any(v >= 2 for v in C.values()):
                    return True
            return False


sl = Solution()
print(sl.buddyStrings("abcaa", "abcbb"))
print(sl.buddyStrings("aa", "aa"))
