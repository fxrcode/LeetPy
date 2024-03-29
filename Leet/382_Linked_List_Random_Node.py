"""
date: 03092023
tag: Medium, Reservoir-sampling
✅ GOOD Reservoir Sampling
Daily Challenge (Jan 7)
"""

# Definition for singly-linked list.
from random import random
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """

    Approach 2: Reservoir Sampling

    XXX: Explanation for (Math.random() < 1.0 / scope)

    Math.random
    generate numbers from
    0.0 to 1.0 with equal probability

    0.0 to 0.5 with 50% probability
    0.0 to 0.8 with 80% probability

    therefore

    0.0 to 1/scope is scope% probability.
    45% <==> random < 0.45

    """

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self):
        n, k = 1, 1
        head, ans = self.head, self.head
        while head.next:
            n += 1
            head = head.next
            if random.random() < k / n:
                ans = ans.next
                k += 1

        return ans.val


class Solution_fxr:
    """
    Runtime: 90 ms, faster than 49.09% of Python3 online submissions for Linked List Random Node.

    """

    def __init__(self, head: Optional[ListNode]):
        cur = head
        i = 0
        self.D = {}
        while cur:
            self.D[i] = cur.val
            cur = cur.next
            i += 1
        print(self.D)

    def getRandom(self) -> int:
        r = int(random() * len(self.D))
        print(r)
        return self.D[r]
