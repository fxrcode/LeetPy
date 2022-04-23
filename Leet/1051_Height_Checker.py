'''
https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/
leetcode explore: Array 101. Conclusion
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].
'''


from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Your runtime beats 96.64 % of python3 submissions.

        So smart: 2 pointers + Counting sort
        T: O(N), M: O(101)
        CS Dojo: <Learn Counting Sort Algorithm in LESS THAN 6 MINUTES!>, counting sort is stable and linear!
        XXX: The origin Counting Sort is : Frequency array, then prefix sum, and shift, to get the correct index, then loop arr reversely to put into output pos, then map[v]--.
        XXX: In here, we just use the counting sort idea, so we only check next bucket if current buckets #'s occurence met!
        """
        map = [0]*101
        for h in heights:
            map[h] += 1

        res = 0
        h_ptr = 1
        for h in heights:
            while map[h_ptr] == 0:
                h_ptr += 1
            if h_ptr != h:
                res += 1
            map[h_ptr] -= 1
        return res

    def heightChecker_fxr(self, heights: List[int]) -> int:
        """
        Your runtime beats 70.64 % of python3 submissions.
        AC in 1st try. T: O(nlogn), M: O(n)
        Explicit sort into another array.
        """
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count

    @staticmethod
    def countSort(arr):
        """
        https://www.geeksforgeeks.org/counting-sort/
        """
        # The output character array that will have sorted arr
        output = [0 for i in range(len(arr))]

        # Create a count array to store count of individual
        # characters and initialize count array as 0
        count = [0 for i in range(256)]

        # For storing the resulting answer since the
        # string is immutable
        ans = ["" for _ in arr]

        # Store count of each character
        for i in arr:
            count[ord(i)] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this character in output array
        for i in range(256):
            count[i] += count[i-1]

        # Build the output character array
        for i in range(len(arr)):
            output[count[ord(arr[i])]-1] = arr[i]
            count[ord(arr[i])] -= 1

        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(len(arr)):
            ans[i] = output[i]
        return ans


sl = Solution()

sl.heightChecker([1, 1, 4, 2, 1, 3])
# Driver program to test geeksforgeeks function
# arr = "geeksforgeeks"
# ans = sl.countSort(arr)
# print("Sorted character array is % s" % ("".join(ans)))
