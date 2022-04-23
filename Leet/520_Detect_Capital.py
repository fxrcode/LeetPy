'''
Daily Challenge (Jan 24)
tag: easy
'''


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def os():
            """
            Runtime: 52 ms, faster than 19.70% of Python3 online submissions for Detect Capital.

            T: O(N)
            """
            n = len(word)
            if n == 1:
                return True
            # case 1: all cap
            if word[0].isupper() and word[1].isupper():
                for i in range(2, n):
                    if not word[i].isupper():
                        return False
            # case 2 and 3
            else:
                for i in range(1, n):
                    if word[i].isupper():
                        return False
            return True

        def artod():
            """
            Runtime: 36 ms, faster than 50.45% of Python3 online submissions for Detect Capital.

            T: O(N)
            """
            cnt = sum(c.isupper() for c in word)
            return cnt == len(word) \
                or cnt == 0 \
                    or cnt == 1 and word[0].isupper()