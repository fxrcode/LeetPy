"""
tag: Medium, sort, hash
Lookback:
- signature of anagram is char count, so O(S). no need of sort O(SlogS)

https://leetcode.com/problems/group-anagrams/
Leetcode Explore: Hash Table. Practical Application - Design the Key

Given an array of strings strs, group the anagrams together. You can return the answer in any order.


"""


from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def os():
            """
            Runtime: 150 ms, faster than 47.57% of Python3 online submissions for Group Anagrams.
            T: O(NS)
            """
            d = defaultdict(list)
            for s in strs:
                bucket = [0] * 26
                for c in s:
                    bucket[ord(c) - ord("a")] += 1
                d[tuple(bucket)].append(s)
            return d.values()

        return os()

        def fxr():
            """
            Runtime: 104 ms, faster than 88.48% of Python3 online submissions for Group Anagrams.
            T: O(NSlogS)
            """
            d = defaultdict(list)
            for s in strs:
                ss = tuple(sorted(s))
                d[ss].append(s)
            return d.values()

        return fxr()


sl = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sl.groupAnagrams(strs))
