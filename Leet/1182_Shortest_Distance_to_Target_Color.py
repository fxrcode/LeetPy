"""
✅ GOOD Coding Skill
Tag: Medium, DP
Lookback:
- Study Plan: Dynamic Programming (Day 13: Min/Max Path Sum)
- Draw out example, and clear variable/index meaning
"""


from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class Solution:
    def shortestDistanceColor(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        def os_dp():
            """
            Runtime: 1836 ms, faster than 64.81% of Python3 online submissions for Shortest Distance to Target Color.

            XXX: learned a lot from it's logic (loop invariant!)
            T: O(N+Q), M: O(N)
            """
            n = len(colors)
            rightmost = [0, 0, 0]
            leftmost = [n - 1, n - 1, n - 1]

            distance = [[-1] * n for _ in range(3)]
            # looking forward
            for i in range(n):
                c = colors[i] - 1
                for j in range(rightmost[c], i + 1):
                    # so j's closest dist to its right (i)
                    distance[c][j] = i - j
                rightmost[c] = i + 1

            # look backward
            for i in range(n - 1, -1, -1):
                c = colors[i] - 1
                for j in range(leftmost[c], i - 1, -1):
                    # if we didn't find a target color on its (j) right, or we find out that
                    #   a target color on its left is closer to the one on its right
                    if distance[c][j] == -1 or distance[c][j] > j - i:
                        distance[c][j] = j - i
                leftmost[c] = i - 1

            return [distance[c][i] for i, c in queries]

        def adkakne():
            """
            Runtime: 2412 ms, faster than 22.76% of Python3 online submissions for Shortest Distance to Target Color.

            https://leetcode.com/problems/shortest-distance-to-target-color/discuss/376925/A-Novel-Method-using-DP-O(n)-or-O(n)-Explained/978493
            T: O(N+Q), M: O(N)
            """

            def preprocess(T, start, end, direction):
                for color in range(1, 4):
                    for i in range(start, end, direction):
                        if T[color, i - direction] != -1:
                            T[color, i] = T[color, i - direction] + 1
                        if color == colors[i]:
                            T[color, i] = 0

            def query(left, right, c, i):
                l, r = left[c, i], right[c, i]
                return max(l, r) if -1 in {l, r} else min(l, r)

            def dp():
                left, right = defaultdict(lambda: -1), defaultdict(lambda: -1)
                preprocess(left, 0, len(colors), 1)
                preprocess(right, len(colors) - 1, -1, -1)
                # query
                res = [query(left, right, c, i) for i, c in queries]

        def fxr_bisect():
            """
            Runtime: 1688 ms, faster than 97.35% of Python3 online submissions for Shortest Distance to Target Color.

            T: O(QlogN + N). Q: len(queries), N: len(colors)
            """

            def take_closest(li, n):
                """
                XXX: coding basics snippet
                Assumes myList is sorted. Returns closest value to myNumber.
                If two numbers are equally close, return the smallest number.
                """
                pos = bisect_left(li, n)
                if pos == 0:
                    return li[0]
                if pos == len(li):
                    return li[-1]
                before = li[pos - 1]
                after = li[pos]
                if after - n < n - before:
                    return after
                else:
                    return before

            c2idx = defaultdict(list)
            ans = []
            for i, c in enumerate(colors):
                c2idx[c].append(i)
            for i, c in queries:
                if c not in c2idx:
                    ans.append(-1)
                    continue
                ans.append(abs(take_closest(c2idx[c], i) - i))
            return ans

        def fxr_WA():
            T, n = defaultdict(lambda: [INF, INF, INF]), len(colors)
            T[0][colors[0] - 1] = 0
            T[n - 1][colors[-1] - 1] = 0
            # loop left->right, T means shortest distance to left closest
            for i in range(1, n):
                c = colors[i]
                T[i][c - 1] = 0
                others = [1, 2, 3]
                others.remove(c)
                for oc in others:
                    T[i][oc - 1] = min(T[i][oc - 1], T[i - 1][oc - 1] + 1)
            # loop right->left, T updates to min(right closest, left)
            for i in range(n - 1, 0, -1):
                c = colors[i]
                T[i][c - 1] = 0
                others = [1, 2, 3]
                others.remove(c)
                for oc in others:
                    T[i][oc - 1] = min(T[i][oc - 1], T[i - 1][oc - 1] + 1)

            print(T)

            ans = []
            for i, c in queries:
                closest = T[i][c - 1]
                ans.append(closest if closest != INF else -1)
            return ans
