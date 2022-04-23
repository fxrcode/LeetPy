'''
FB tag (Medium)
REF: https://leetcode.com/problems/print-immutable-linked-list-in-reverse/discuss/445408/Py-5-time-space-combinations-space-O(n)-O(n)-O(lg-n)-O(1)#divide-and-conquer

Follow up:

Could you solve this problem in:
+ Constant space complexity?
+ Linear time complexity and less than linear space complexity?
'''


class ImmutableListNode:
    """
    This is the ImmutableListNode's API interface.
    You should not implement it, or speculate about its implementation.
    """
    def printValue(self) -> None:  # print the value of this node.
        pass

    def getNext(self) -> 'ImmutableListNode':  # return the next node.
        pass


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def fxr():
            def dfs(n: 'ImmutableListNode'):
                """
                Runtime: 53 ms, faster than 25.71% of Python3 online submissions for Print Immutable Linked List in Reverse.

                T: O(N), M: O(N) call-stack
                """
                if n:
                    dfs(n.getNext())
                    n.printValue()

            dfs(head)