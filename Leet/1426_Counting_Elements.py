'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170
'''


from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        def os_sort():
            """
            Runtime: 36 ms, faster than 77.43% of Python3 online submissions for Counting Elements.

            OS impl is neat!
            """
            arr.sort()
            run_len = 1
            cnt = 0
            for i in range(len(arr)):
                if arr[i-1] != arr[i]:
                    if arr[i-1]+1 == arr[i]:
                        cnt += run_len
                    run_len = 0
                run_len = 1
            return cnt

        def fxr_sort():
            """
            Runtime: 32 ms, faster than 93.39% of Python3 online submissions for Counting Elements.

            I saw os's sort keyword, then impl my own without check the detail os algs.
            T: O(nlogn), M: O(1)
            """
            arr.sort()
            i = 0
            cnt = 0
            while i < len(arr):
                c = arr[i]
                j = i
                while j < len(arr) and arr[j] == c:
                    j += 1
                if arr[j] == c+1:
                    cnt += j-i
                i = j
            return cnt

        def fxr():
            """
            Runtime: 43 ms, faster than 42.41% of Python3 online submissions for Counting Elements.

            AC in 2.
            T: O(N), M: O(N)
            """
            sa = set(arr)
            cnt = 0
            for a in arr:
                if a+1 in sa:
                    cnt += 1
            return cnt

        return fxr()
