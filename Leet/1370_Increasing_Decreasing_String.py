"""
tag: Easy, Hash, Sort
Lookback:
- Not familiar w/ dict iteration if dict will be modified
"""


from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        def rock():
            """
            Runtime: 87 ms, faster than 62.61% of Python3 online submissions for Increasing Decreasing String.

            https://leetcode.com/problems/increasing-decreasing-string/discuss/531811/JavaPython-3-Two-clean-codes-w-explanation-and-analysis.
            XXX: iterate copy of key if you need to modify dict!
            XXX: use asc flag if asc/desc logic is similar
            """
            cnt, ans, asc = Counter(s), [], True
            while cnt:
                for c in sorted(cnt) if asc else reversed(sorted(cnt)):
                    ans.append(c)
                    cnt[c] -= 1
                    if cnt[c] == 0:
                        cnt.pop(c)
                asc = not asc
            return "".join(ans)

        return rock()

        def fxr():
            freq = Counter(sorted(s))
            res = []
            while freq:
                for p in freq:
                    if freq[p] > 0:
                        res.append(p)
                        freq[p] -= 1
                for p in reversed(freq):
                    if freq[p] > 0:
                        res.append(p)
                        freq[p] -= 1
                if all(freq[p] == 0 for p in freq):
                    break
            return "".join(res)

        return fxr()


sl = Solution()
print(sl.sortString("rat"))
print(sl.sortString(s="aaaabbbbcccc"))
