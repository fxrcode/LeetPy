'''

Lookback:
- similar: 1247
- Set/Dict has no index, so the equality check is natural check, no need to order!
'''

from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def dbabichev():
            """
            Runtime: 230 ms, faster than 49.14% of Python3 online submissions for Determine if Two Strings Are Close.

            T: O(N)
            """
            # return set(word1) == set(word2) and \
            #     Counter(Counter(word1).values()) == Counter(Counter(word2).values())
            C1, C2 = Counter(word1), Counter(word2)
            return C1.keys() == C2.keys() \
                and Counter(C1.values()) == Counter(C2.values())

        return dbabichev()


sl = Solution()
print(sl.closeStrings('abc', 'bca'))
print(sl.closeStrings('a', 'aa'))
print(sl.closeStrings('cabbba', 'abbccc'))
print(sl.closeStrings('uau', 'ssx'))
print(sl.closeStrings("abbzzca", "babzzcz"))
