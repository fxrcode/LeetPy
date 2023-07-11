"""
💡insight
Zoox: Horses Neigh
tag: medium, counting, logic
Lookback
- basic counting logic, go through eg to understand the logic
"""


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        def xavier_():
            """
            Runtime: 169 ms, faster than 86.12% of Python3 online submissions for Minimum Number of Frogs Croaking.

            REF: https://leetcode.com/problems/minimum-number-of-frogs-croaking/discuss/586497/2-Easy-Python%3A-croak-%2B-croak-growl-hum-grunt-mew-bawl-creak-...
            T: O(N)
            """
            watermark = c = r = o = a = k = 0
            for x in croakOfFrogs:
                if x == "c":
                    c += 1
                    watermark = max(watermark, c - k)
                elif x == "r":
                    r += 1
                elif x == "o":
                    o += 1
                elif x == "a":
                    a += 1
                else:
                    k += 1
                if not c >= r >= o >= a >= k:
                    return -1
            return watermark if c == k else -1

        def general_xavier(sound, soundOfAnimals):
            """
            Check xavier's explain: https://leetcode.com/problems/minimum-number-of-frogs-croaking/discuss/586497/2-Easy-Python%3A-croak-%2B-croak-growl-hum-grunt-mew-bawl-creak-...
            """
            watermark, d = 0, {s: 0 for s in sound}
            for ch in soundOfAnimals:
                if (
                    ch not in sound
                    or ch != sound[0]
                    and d[ch] == d[sound[sound.index(ch) - 1]]
                ):
                    return -1
                else:
                    d[ch] += 1
                if ch == sound[0]:
                    watermark = max(watermark, d[sound[0]] - d[sound[-1]])
            return watermark if d[sound[0]] == d[sound[-1]] else -1
