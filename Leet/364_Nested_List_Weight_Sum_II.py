'''

Weekly Special (Dec W2)
TODO: BFS
'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def fxr_math_1pass(nl: List[NestedInteger]) -> int:
            """
            Runtime: 24 ms, faster than 97.77% of Python3 online submissions for Nested List Weight Sum II.

            Similar to OS: do some math to analyze property (learned thought from 2033. Minimum Operations to Make a Uni-Value Grid)

            weight = maxdepth - depth_of_elem + 1. Can be broken into: fixed (maxdepth +1) - variable (depth_of_elem)
            """

            def dfs(nl: List[NestedInteger], depth, mxdep, simple_sm):
                '''
                do sum(elem) into addsup, and return elem * depth
                '''
                mxdep[0] = max(mxdep[0], depth)
                weighted_sm = 0
                for e in nl:
                    if e.isInteger():
                        simple_sm[0] += e.getInteger()
                        weighted_sm += e.getInteger() * depth
                    else:
                        weighted_sm += dfs(e.getList(),
                                           depth+1, mxdep, simple_sm)
                return weighted_sm

            mxdep = [1]
            addsup = [0]
            weighted_sm = dfs(nl, 1, mxdep, addsup)
            return (mxdep[0]+1)*addsup[0] - weighted_sm

        def fxr_brute(nl: List[NestedInteger]):
            """
            Runtime: 38 ms, faster than 23.43% of Python3 online submissions for Nested List Weight Sum II.

            Ac in 1
            Metacognition: brute force idea: 1st dfs to get mxdep, then 2nd dfs get weight so as to calculate sum
            """
            def dfs_f1(nl: List[NestedInteger], depth, mxdep):
                mxdep[0] = max(mxdep[0], depth)
                for e in nl:
                    if not e.isInteger():
                        dfs_f1(e.getList(), depth+1, mxdep)

            def dfs_f2(nl: List[NestedInteger], depth, mxdep):
                res = 0
                for e in nl:
                    weig = mxdep[0] - depth + 1
                    if e.isInteger():
                        res += e.getInteger() * weig
                    else:
                        res += dfs_f2(e.getList(), depth+1, mxdep)
                return res
            mxdep = [1]
            dfs_f1(nestedList, 1, mxdep)
            return dfs_f2(nestedList, 1, mxdep)
