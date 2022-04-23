'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

Metacognition:
* obviously, it's similar to merge() in mergesort, only merge if 3 elem are same, then all incr, ow, only incr the index min elem.
* But wasted 5min in using heapq, etc to implement the 3pointer.

Lookback:
* The brute-force is simple intersection!
'''


from typing import List
from collections import Counter
import heapq


class Solution:
    def arraysIntersection(self, A: List[int], B: List[int], C: List[int]) -> List[int]:
        def os_brute():
            ans = []
            cnt = Counter(A+B+C)
            for k in cnt:
                if cnt[k] == 3:
                    ans.append(k)
            return ans

        def os_3ptr():
            """
            Runtime: 99 ms, faster than 37.17% of Python3 online submissions for Intersection of Three Sorted Arrays.

            XXX: check the else case: no need to move the smallest, just move the pointer that points to smaller!
            T: O(N)
            """
            i, j, k = 0, 0, 0
            res = []
            while i < len(A) and j < len(B) and k < len(C):
                if A[i] == B[j] == C[k]:
                    res.append(A[i])
                    i, j, k = i+1, j+1, k+1
                else:
                    if A[i] < B[j]:
                        i += 1
                    elif B[j] < C[k]:
                        j += 1
                    else:
                        k += 1
            return res

        def fxr():
            """
            Runtime: 128 ms, faster than 23.26% of Python3 online submissions for Intersection of Three Sorted Arrays.

            AC in 1 (15 min, so slow)
            """
            i, j, k = 0, 0, 0
            res = []
            while i < len(A) and j < len(B) and k < len(C):
                if A[i] == B[j] == C[k]:
                    res.append(A[i])
                    i, j, k = i+1, j+1, k+1
                else:
                    tmp = [A[i], B[j], C[k]]
                    mn = min(tmp)
                    p = tmp.index(mn)
                    if p == 0:
                        i += 1
                    elif p == 1:
                        j += 1
                    else:
                        k += 1
            return res
        # return fxr()
        return os()


sl = Solution()
print(sl.arraysIntersection(A=[1, 2, 3, 4, 5],
      B=[1, 2, 5, 7, 9], C=[1, 3, 4, 5, 8]))
print(sl.arraysIntersection(A=[197, 418, 523, 876, 1356], B=[
      501, 880, 1593, 1710, 1870], C=[521, 682, 1337, 1395, 1764]))
