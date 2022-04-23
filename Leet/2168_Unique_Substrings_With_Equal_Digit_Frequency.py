"""
tag: medium, roll-hash
Lookback:
- start from brute force, then optimize it.
- I thought it's similar to 828, so I hesitated
- Why hash needs `+1`? 
    - Because digit might be 0, then if the substring has a leading 0, it will not be counted to the hash. In that case, 01 and 1 will have the same hash, which is false. You can use any positive number I believe.

"""

from collections import Counter


class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        def idontknoooo_rolling_hash():
            """
            Runtime: 5083 ms, faster than 50.53% of Python3 online submissions for Unique Substrings With Equal Digit Frequency.

            """
            n, s_set = len(s), set()
            D, MOD = 11, int(2e9 + 7)
            for i in range(n):
                cnt = [0] * 10
                unique = mx_cnt = s_hash = 0
                for j in range(i, n):
                    digit = ord(s[j]) - ord("0")
                    unique += 1 if cnt[digit] == 0 else 0
                    cnt[digit] += 1
                    mx_cnt = max(mx_cnt, cnt[digit])
                    # BUG: s_hash = (s_hash * D + digit) % MOD
                    s_hash = (s_hash * D + digit + 1) % MOD
                    if mx_cnt * unique == j - i + 1:  # if max frequency * unique digits == the substring length, meaning each digits have the same frequency
                        print(s_hash, i, j)
                        s_set.add(s_hash)
            return len(s_set)

        return idontknoooo_rolling_hash()

        def idontknoooo_bf():
            """
            Runtime: 6368 ms, faster than 28.19% of Python3 online submissions for Unique Substrings With Equal Digit Frequency.

            """
            n, s_set = len(s), set()
            for i in range(n):
                cur, cnt = "", [0] * 10
                for j in range(i, n):
                    cnt[ord(s[j]) - ord("0")] += 1
                    cur += s[j]
                    if len(set(cnt) - {0}) == 1:
                        s_set.add(cur)
            return len(s_set)

        def fxr():
            uniq = set()
            n = len(s)

            def equalfreq(num):
                vals = set(Counter(num).values())
                if len(vals) == 1:
                    return True
                return False

            for i in range(n):
                for j in range(i + 1, n + 1):
                    ss = s[i:j]
                    if equalfreq(ss):
                        uniq.add(ss)
            return len(uniq)


sl = Solution()
# print(sl.equalDigitFrequency(s="1212"))
# assert sl.equalDigitFrequency(s="12321") == 9
print(sl.equalDigitFrequency("012345"))
