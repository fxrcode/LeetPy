"""
tag: Medium, Linked-list
Lookback:
- coding skills
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        def fxr():
            # Runtime: 125 ms, faster than 78.36% of Python3 online submissions for Linked List Components.
            cc = len(nums)
            vals = set(nums)
            pre, cur = None, head
            while cur:
                if pre and pre.val in vals and cur.val in vals:
                    cc -= 1
                pre, cur = cur, cur.next
            return cc
