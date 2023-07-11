"""
✅ GOOD Interval (merge interval)
✅ GOOD Trie

tag: medium, interval, trie
Lookback:
- nice disguise of merge intervals
- beautiful usage of trie for strStr
- use `[start, end)` to ease merge interval & modify string.

Note: This question is the same as #616: https://leetcode.com/problems/add-bold-tag-in-string/
"""

from typing import List


class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        def sevenhe716_trie():
            """
            Runtime: 50 ms, faster than 90.00% of Python3 online submissions for Bold Words in String.

            https://leetcode.com/problems/bold-words-in-string/discuss/247076/Optimized-Python-Solution-using-Trie-Tree-and-Merge-Intervals

            """

            root, n, intervals = {}, len(s), []
            # create trie
            for w in words:
                cur = root
                for c in w:
                    cur = cur.setdefault(c, {})
                cur["#"] = 0

            # interval merge
            def merge_interval(iv):
                if not intervals or intervals[-1][1] < iv[0]:
                    intervals.append(iv)
                else:
                    intervals[-1][1] = max(intervals[-1][1], iv[1])

            # make max match and add to interval
            for i in range(n):
                cur, mx_end = root, None
                for j in range(i, n):
                    if s[j] not in cur:
                        break
                    cur = cur[s[j]]
                    if "#" in cur:
                        mx_end = j + 1  # jem: [i,j+1)
                # !only need to add max-match interval!
                if mx_end:
                    merge_interval([i, mx_end])
            # concat result
            res, prev_end = [], 0
            for l, r in intervals:
                res.append(s[prev_end:l] + "<b>" + s[l:r] + "</b>")
                prev_end = r
            return "".join(res + [s[prev_end:]])

        return sevenhe716_trie()

        def fxr():
            """
            Runtime: 266 ms, faster than 14.28% of Python3 online submissions for Bold Words in String.

            REF: sevenhe716, and used #56
            """
            intervals = []
            words.sort(key=lambda x: -len(x))
            for i in range(len(s)):
                for w in words:
                    if s[i:].startswith(w):
                        intervals.append([i, i + len(w)])

            def merge(I):
                res = []
                for itv in I:
                    if not res or res[-1][1] < itv[0]:
                        res.append(itv)
                    else:
                        res[-1][1] = max(res[-1][1], itv[1])
                return res

            merged = merge(intervals)
            # print(intervals)
            # print(merged)

            res, prev_end = [], 0
            for start, end in merged:
                res.append(s[prev_end:start] + "<b>" + s[start:end] + "</b>")
                prev_end = end
            return "".join(res + [s[prev_end:]])

            # ss = list(s)
            # for l, r in merged:
            #     ss[l] = "<b>" + ss[l]
            #     ss[r] = ss[r] + "</b>"
            # return "".join(ss)

        return fxr()


sl = Solution()
print(sl.boldWords(words=["ab", "bc"], s="aabcd"))
print(sl.boldWords(words=["ab", "cb"], s="aabcd"))
assert (
    sl.boldWords(["b", "dee", "a", "ee", "c"], "cebcecceab")
) == "<b>c</b>e<b>bc</b>e<b>cc</b>e<b>ab</b>"
