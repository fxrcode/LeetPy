"""
tag: medium, Trie
Lookback:
- substr => suffix trie
- existing problem: LCS, LRS (longest common/repeated substr) check CP4

Similar:
1408. String Matching in an Array

"""


from collections import defaultdict


class Solution:
    def countDistinct(self, s: str) -> int:
        def blackspinner():
            """
            Runtime: 5668 ms, faster than 5.51% of Python3 online submissions for Number of Distinct Substrings in a String.

            T: O(N^2)
            """

            class Node:
                def __init__(self) -> None:
                    self.child = defaultdict(Node)

            root = Node()
            res = 0
            for i in range(len(s)):
                cur = root
                for j in range(i, len(s)):
                    if s[j] not in cur.child:
                        cur.child[s[j]] = Node()
                        res += 1
                    cur = cur.child[s[j]]
            return res

        return blackspinner()


sl = Solution()
print(sl.countDistinct(s="aabbaba"))
print(sl.countDistinct(s="abcdefg"))
