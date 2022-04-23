"""
✅ GOOD Slide-window (atMost trick)
❌
tag: easy, slide-window
Lookback:
- not fully understand slide-window use case. (DSA not only impl, but more importantly: it's use case!)
- Q: can slide-window do atLeast? check: #395
[ ] REDO

Similar:
Problems Solvable using this template
3. Longest Substring Without Repeating Characters
159. Longest Substring with At Most Two Distinct Characters (Medium)
340. Longest Substring with At Most K Distinct Characters
424. Longest Repeating Character Replacement
487. Max Consecutive Ones II
713. Subarray Product Less Than K
1004. Max Consecutive Ones III
1208. Get Equal Substrings Within Budget (Medium)
1493. Longest Subarray of 1's After Deleting One Element
1695. Maximum Erasure Value
1838. Frequency of the Most Frequent Element
2009. Minimum Number of Operations to Make Array Continuous
2024. Maximize the Confusion of an Exam
The following problems are also solvable using the shrinkable template with the "At Most to Equal" trick

930. Binary Subarrays With Sum (Medium)
992. Subarrays with K Different Integers
1248. Count Number of Nice Subarrays (Medium)
2062. Count Vowel Substrings of a String (Easy)
"""


from collections import Counter


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        def lzl124631x_brute():
            ans = 0
            for i in range(len(word)):
                for j in range(i + 5, len(word) + 1):
                    if set(word[i:j]) == set("aeiou"):
                        print(word[i:j])
                        ans += 1
            return ans

        def lzl124631x_atMost():
            """
            https://leetcode.com/problems/count-vowel-substrings-of-a-string/discuss/1563765/C%2B%2B-O(N)-Time-Sliding-Window-%2B-%22At-Most-to-Equal%22-trick
            🌟 Sliding Window "At Most to Equal" trick
            """
            vowel = set("aeiou")

            def atMost(s, goal):
                win = Counter()
                l, r = 0, 0
                cnt = 0
                while r < len(s):
                    c = s[r]
                    win[c] += 1
                    r += 1
                    if c not in vowel:
                        l = r
                        win.clear()
                        continue

                    # BUG: while not set(win.keys()).issubset(set(vowal)):
                    while len(win.keys()) > goal:
                        d = s[l]
                        win[d] -= 1
                        if win[d] == 0:
                            win.pop(d)
                        l += 1

                    #! this window [i, j) is the maximum window ending at `s[j-1]` that has at most `goal` number of unique vowels.
                    # Eg : For substring "eiuo", Length = 4, Number of vowel substrings ending with 'o' - 4 ({"eiuo","iuo","uo","o"}).
                    cnt += r - l
                return cnt

            am5 = atMost(word, 5)
            am4 = atMost(word, 4)
            # print(am5, am4)
            return am5 - am4

        return lzl124631x_atMost()


sl = Solution()
print(sl.countVowelSubstrings("aeiouu"))
print(sl.countVowelSubstrings(word="cuaieuouac"))
