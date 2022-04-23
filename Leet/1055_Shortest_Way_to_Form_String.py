'''
✅ GOOD DP (Subsequence)
✅ GOOD Logic
[ ] REDO: copied ans to finish Study Plan on last day (Dec 1)

This is a google phone screen question.

https://leetcode.com/study-plan/dynamic-programming/?progress=r5nylos
Study Plan: Dynamic Programming
Day 12: DP on String


Metacognition:
* totally no clue!!!
'''
from collections import defaultdict
from bisect import bisect_left, bisect_right


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def twohu():
            """
            Runtime: 28 ms, faster than 97.83% of Python3 online submissions for Shortest Way to Form String.

            https://leetcode.com/problems/shortest-way-to-form-string/discuss/304662/Python-O(M-%2B-N*logM)-using-inverted-index-%2B-binary-search-(Similar-to-LC-792)

            It's the same idea as 792. Number of Matching Subsequences. I recommend solving that question first.

            The runtime is O(M) to build the index, and O(logM) for each query. There are N queries, so the total runtime is O(M + N*logM). M is the length of source and N is the length of target. The space complexity is O(M), which is the space needed to store the index.

            Closing thoughts: As usual, there are multiple solutions to this problem. One way other way to solve is the naive O(M*N) solution using two pointers. This solution won't be enough to pass a phone screen. There is also a dynamic programming O(|Σ|*M + N) solution (where |Σ| is the size of the alphabet, or 26 in this question). xiangmo posted an example solution here.
            """
            invert_index = defaultdict(list)
            for prev, ch in enumerate(source):
                invert_index[ch].append(prev)

            # Initialize prev = -1 (i represents the smallest valid next offset)
            # loop_cnt = 1 (number of passes through source). My pov: this means we need to start a new subseq
            loop_cnt = 1
            prev = -1
            for ch in target:
                if ch not in invert_index:
                    return -1
                offset_list_for_ch = invert_index[ch]
                j = bisect_right(offset_list_for_ch, prev)
                if j == len(offset_list_for_ch):
                    loop_cnt += 1
                    prev = offset_list_for_ch[0]
                else:
                    prev = offset_list_for_ch[j]
            return loop_cnt
