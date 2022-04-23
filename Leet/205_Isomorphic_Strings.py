'''
https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
Leetcode Explore: Hash Table. Practical Application - HashMap
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

NOTE: This is one of those problems where we can come up with a whole suite of different solutions, with similar
complexities. We only focus on solutions that reasonably easy to come up with during an interview.


Followup: group the isomorphic strings. Use encoding to Unicode is a good fit

input:
['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']

return:
[
['xyx'], 
['xyz', 'abc', 'def'], 
['aab', 'xxy']
]
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Runtime: 52 ms, faster than 34.50% of Python3 online submissions for Isomorphic Strings.

        Transform string uniformly to aabbccdd. How? by char's first occur index!
        T: O(n+m), M: O(256)
        """
        def num2unicode(n) -> s:
            return chr(n+48)  # 48 -> '0'

        def occur_1st(s) -> str:
            d = {}
            res = []
            for i, c in enumerate(s):
                if c not in d:
                    d[c] = i
                res.append(num2unicode(d[c]))
            return ''.join(res)
        encode_s = occur_1st(s)
        encode_t = occur_1st(t)
        print(encode_s, encode_t)
        return encode_s == encode_t

    def isIsomorphic_sol_twoway(self, s: str, t: str) -> bool:
        """
        Runtime: 52 ms, faster than 34.50% of Python3 online submissions for Isomorphic Strings.
        T: O(N), M: O(256) due to limit # of alpha
        """
        s2t, t2s = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 not in s2t) and (c2 not in t2s):
                s2t[c1] = c2
                t2s[c2] = c1
            else:
                if s2t.get(c1) != c2 or t2s.get(c2) != c1:
                    return False
        return True

    def isIsomorphic_fxr_twoway(self, s: str, t: str) -> bool:
        """
        Runtime: 61 ms, faster than 21.71% of Python3 online submissions for Isomorphic Strings.

        XXX: a bit over-complicate implementation
        """
        s2t, t2s = {}, {}
        for c1, c2 in zip(s, t):
            if c1 not in s2t:
                s2t[c1] = c2
                if c2 not in t2s:
                    t2s[c2] = c1
                elif t2s[c2] != c1:
                    return False
            else:
                if s2t[c1] != c2:
                    return False
                t2s[c2] = c1
        return True

    def isIsomorphic_fxr(self, s: str, t: str) -> bool:
        """
        Your runtime beats 43.61 % of python3 submissions.

        AC in 1.
        XXX: need 1-to-1 mapping, so two-way mapping
        """
        def mp(s, t):
            d = {}
            for i in range(len(s)):
                c1, c2 = s[i], t[i]
                if c1 not in d:
                    d[c1] = c2
                else:
                    if d[c1] != c2:
                        return False
            return True
        if len(s) != len(t):
            return False
        return mp(s, t) and mp(t, s)


sl = Solution()
print(sl.isIsomorphic("egg", "add"))
print(sl.isIsomorphic("egb", "add"))
