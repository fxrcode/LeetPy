'''
https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
Leetcode Explore Array 101: Searching for Items in array

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
'''


from typing import List
import bisect


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Forum: https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/503441/JavaPython-3-HashSet-w-analysis.
        just single traversal: just check if double or half of current has been seen.
        XXX: Polya
        """
        seen = set()
        for i in arr:
            if i / 2 in seen or i*2 in seen:
                return True
            seen.add(i)
        return False

    def checkIfExist_bisect(self, arr: List[int]) -> bool:
        """
        Your runtime beats 90.49 % of python3 submissions.
        AC in 1st try. But not the best, because T: O(nlogn)
        """
        # no need to persist origin index, additionaly, how does bisect works on List[Tuple]?
        # aug = sorted([(arr[i], i)
        #              for i in range(len(arr))], key=lambda tu: tu[0])
        sarr = sorted(arr)

        for i in range(len(sarr)):
            pi = bisect.bisect_left(sarr, sarr[i] * 2)
            # XXX: 0 = 0*2, so I need to test if index same
            if pi < len(sarr) and pi != i and sarr[pi] == sarr[i]*2:
                print(sarr[i], sarr[pi])
                return True
        return False

    @staticmethod
    def test_bisect():
        # XXX: the diff of bisect_left vs bisect_right is the equal part
        #      bisect_left: all A[:i] < x and A[i:] >= x
        #      bisect_right: all A[:i] <=x and A[i:] > x
        #      so return of bisect_left is just before the leftmost x
        #      while bisect_right is just beyond the rightmost x
        arr = [1, 5, 7, 10, 15]
        print(arr, bisect.bisect_left(arr, 6))
        arr = [1, 5, 6, 6, 6, 7, 10, 15]
        print(arr, bisect.bisect_left(arr, 6))
        arr = [1, 5, 7, 10, 15]
        print(arr, bisect.bisect_right(arr, 6))
        arr = [1, 5, 6, 6, 6, 7, 10, 15]
        print(arr, bisect.bisect_right(arr, 6))

        # XXX: note, bisect return might = len(arr)!
        print(arr, bisect.bisect_left(arr, 100))


sl = Solution()
# arr = [7, 1, 14, 11]
# arr = [10, 2, 5, 3]
# arr = [3, 1, 7, 11]
arr = [-2, 0, 10, -19, 4, 6, -8]
print(sl.checkIfExist(arr))
# sl.test_bisect()
