"""
✅ GOOD Skills
✅ GOOD Logic

tag: easy, skills, Facebook
Lookback:
- don't simulate. Do it smartly!
- re-state the problem: combine sublist to see if match w/ arr (eric496 5loc)
"""

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        def eric496():
            """
            Runtime: 59 ms, faster than 57.07% of Python3 online submissions for Check Array Formation Through Concatenation.

            """
            mp = {p[0]: p for p in pieces}
            res = []
            for n in arr:
                res += mp.get(n, [])
            return res == arr

        return eric496()

        def os_3_map():
            """
            Runtime: 66 ms, faster than 42.60% of Python3 online submissions for Check Array Formation Through Concatenation.

            T: O(N)
            M: O(N)
            """
            n = len(arr)
            d = {p[0]: pi for pi, p in enumerate(pieces)}
            i = 0
            while i < n:
                # find target piece
                if arr[i] not in d:
                    return False
                pi = d[arr[i]]
                target_piece = pieces[pi]
                for x in target_piece:
                    if x != arr[i]:
                        return False
                    i += 1
            return True

        return os_3_map()

        def os_2_bisect():
            """
            Runtime: 66 ms, faster than 42.60% of Python3 online submissions for Check Array Formation Through Concatenation.

            """
            nonlocal pieces
            pieces.sort(key=lambda x: x[0])
            p_len = len(pieces)
            n = len(arr)
            i = 0
            while i < n:
                left, right = 0, p_len - 1
                found = -1
                # use bisect to find target piece
                while left < right:
                    mid = (left + right) // 2
                    if pieces[mid][0] >= arr[i]:
                        right = mid
                    else:
                        left = mid + 1
                target_piece = pieces[left]
                for x in target_piece:
                    if x != arr[i]:
                        return False
                    i += 1
            return True

        def os_1():
            """
            Your runtime beats 54.24 % of python3 submissions.

            T: O(N^2)
            M: O(1)
            """
            n = len(arr)
            i = 0
            while i < n:
                # find target piece:
                for p in pieces:
                    if p[0] == arr[i]:
                        break
                else:
                    return False
                # loop and match current piece for arr's sublist
                # python saves the last iterated p
                for x in p:
                    if x != arr[i]:
                        return False
                    i += 1
            return True

        return os_1()

        '''
        def fxr():
            """
            Runtime: 60 ms, faster than 54.24% of Python3 online submissions for Check Array Formation Through Concatenation.

            """
            p_i = list([i, 0] for i in range(len(pieces)))
            last_sublist = -1
            for a in arr:
                if last_sublist == -1:
                    for i, pi in enumerate(p_i):
                        pidx, it = pi[0], pi[1]
                        p = pieces[pidx]
                        if it < len(p) and p[it] == a:
                            last_sublist = i
                            it += 1
                            if it == len(p):
                                last_sublist = -1
                            else:
                                pi[1] = it
                            break
                    else:
                        return False
                else:
                    # in last_sublist
                    pidx, it = p_i[last_sublist]
                    p = pieces[pidx]
                    if p[it] != a:
                        return False
                    it += 1
                    if it == len(p):
                        last_sublist = -1
                    else:
                        p_i[last_sublist][1] = it
            return True
        '''


sl = Solution()
print(sl.canFormArray(arr=[15, 88], pieces=[[88], [15]]))
print(sl.canFormArray(arr=[49, 18, 16], pieces=[[16, 18, 49]]))
print(sl.canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]]))
