"""
❌📌 GOOD String (counting)
Tag: Medium, Hash, Str
Lookback:
- Needs more practice on problem w/ simple algs, but neat impl
"""

from collections import Counter, defaultdict
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        def rock_neat():
            """
            use pairs to count the number of pairs of mirror words we found
            Use nonPaired (dict) to count words not in pairs yet
            use sym to count the symmetric words not in pairs;
            """
            pairs, sym, nonpaired = 0, 0, Counter()
            for w in words:
                rev = w[::-1]
                if nonpaired[rev] > 0:
                    pairs += 1
                    nonpaired[rev] -= 1
                    sym -= 1 if w[0] == w[1] else 0
                else:
                    nonpaired[w] += 1
                    sym += 1 if w[0] == w[1] else 0
            return pairs * 4 + (2 if sym else 0)

        return rock_neat()

        def tojuna_neat():
            """
            Runtime: 1400 ms, faster than 85.18% of Python3 online submissions for Longest Palindrome by Concatenating Two Letter Words.

            https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/discuss/1675343/Python3-Java-C%2B%2B-Counting-Mirror-Words-O(n)
            """
            counter, ans = [[0] * 26 for _ in range(26)], 0
            for w in words:
                a, b = ord(w[0]) - ord("a"), ord(w[1]) - ord("a")
                if counter[b][a]:
                    ans += 4
                    counter[b][a] -= 1
                else:
                    counter[a][b] += 1
            for i in range(26):
                if counter[i][i]:
                    ans += 2
                    break
            return ans

        return tojuna_neat()

        def fxr():
            """
            Runtime: 2521 ms, faster than 8.94% of Python3 online submissions for Longest Palindrome by Concatenating Two Letter Words.

            """
            dif = defaultdict(lambda: [0, 0])
            sym = Counter()
            for w in words:
                if w != w[::-1]:
                    signt = "".join(sorted(list(w)))
                    if w == signt:
                        dif[signt][0] += 1
                    else:
                        dif[signt][1] += 1
                else:
                    sym[w] += 1
            cnt_d = cnt_s = 0
            for w in dif:
                cnt_d += min(dif[w])
            odd = False
            for w in sym:
                if sym[w] % 2:
                    odd = True
                cnt_s += sym[w] // 2
            return (cnt_d + cnt_s) * 4 + odd * 2

        return fxr()


sl = Solution()
print(sl.longestPalindrome(words=["lc", "cl", "gg"]))
print(sl.longestPalindrome(words=["ab", "ty", "yt", "lc", "cl", "ab"]))
print(sl.longestPalindrome(words=["cc", "ll", "xx", "xx"]))
assert (
    sl.longestPalindrome(
        [
            "dd",
            "aa",
            "bb",
            "dd",
            "aa",
            "dd",
            "bb",
            "dd",
            "aa",
            "cc",
            "bb",
            "cc",
            "dd",
            "cc",
        ]
    )
    == 22
)
