"""
✅ GOOD Roll-Hash
tag: easy, roll-hash
Lookback:
- 1st time use good roll-hash template, use sys.maxsize for MOD.
    * will get WA for long needle if MOD not big enought (2e9 got WA)
https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
Explore Array & String: Intro String
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Rabin-karp: rolling hash. No need of KMP or aho-corasick state machine
"""
import sys


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def lccn345():
            """
            Runtime: 68 ms, faster than 57.49% of Python3 online submissions for Implement strStr().

            https://leetcode.com/problems/implement-strstr/discuss/665448/AC-simply-readable-Python-KMP-Rabin-Karp
            """

            def f(c):
                return ord(c) - ord("a")

            # ! careful on d,m, original ord(z)-ord(A), 2e9 cuz -1! and super slow!
            N, H, D, MOD = len(needle), len(haystack), ord("z") - ord("a") + 1, sys.maxsize
            if N > H:
                return -1
            DN, hash_n, hash_h = D ** (N - 1), 0, 0
            for i in range(N):
                hash_n = (D * hash_n + f(needle[i])) % MOD
                hash_h = (D * hash_h + f(haystack[i])) % MOD
            if hash_n == hash_h:
                return 0
            for i in range(1, H - N + 1):
                hash_h = (D * (hash_h - f(haystack[i - 1]) * DN) + f(haystack[i + N - 1])) % MOD  # e.g. 10*(1234-1*10**3)+5=2345
                if hash_n == hash_h:
                    return i
            return -1

        return lccn345()

        def fxr_brute():
            """
            common snippet: 2ptr slide-window (fix-size)
            eg. 1886
            """

            def brute(src, tgt):
                for s in range(len(src) - len(tgt) + 1):
                    for i in range(len(tgt)):
                        if src[s + i] != tgt[i]:
                            break
                    else:
                        return True, s
                return False, -1

            b, p = brute(haystack, needle)
            return p

        '''
        def clrs():
            """
            Your runtime beats 44.28 % of python3 submissions.

            https://www.programiz.com/dsa/rabin-karp-algorithm
            This is based on CLRS P993
            XXX: many coding details: index range, hash calculate, p==t_s check, then update t_{s+1}
            """
            m, n = len(needle), len(haystack)
            p, t = 0, 0  # hash code for pattern and text
            h = 1  # 31^(m-1)
            d, q = 31, 1e6
            for _ in range(m - 1):
                h = (h * d) % q

            # preprocess: hash code of pattern and text
            for i in range(m):
                p = (p * d + ord(needle[i])) % q
                t = (t * d + ord(haystack[i])) % q

            # matching: do the shift
            for i in range(n - m + 1):
                if p == t:  # mathcing p vs t_s
                    for j in range(m):
                        if haystack[i + j] != needle[j]:
                            break
                    j += 1
                    if j == m:
                        # return i
                        print("Pattern is found at position: " + str(i))

                # don't forget this, ow, haystack[i+m] may out of index. eg. abcde -> cde
                if i < n - m:
                    # compute t_s+1
                    t = (d * (t - ord(haystack[i]) * h) + ord(haystack[i + m])) % q
                    if t < 0:
                        t = t + q
            return -1
        '''


sl = Solution()
print(sl.strStr(haystack="hello", needle="ll"))
print(sl.strStr(haystack="aaaaa", needle="bba"))
print(sl.strStr("ababcaababcaabc", "ababcaabc"))
print(sl.strStr("baabbaaaaaaabbaaaaabbabbababaabbabbbbbabbabbbbbbabababaabbbbbaaabbbbabaababababbbaabbbbaaabbaababbbaabaabbabbaaaabababaaabbabbababbabbaaabbbbabbbbabbabbaabbbaa", "bbaaaababa"))
