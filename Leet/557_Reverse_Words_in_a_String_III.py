'''
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/
Leetcode Explore Array & String: Conclusion
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

All the words in s are separated by a single space.
s does not contain any leading or trailing spaces.
There is at least one word in s.

'''


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Your runtime beats 15.56 % of python3 submissions.


        Args:
            s (str): [description]

        Returns:
            str: [description]
        """
        def rev(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        n = len(s)
        l, r = 0, 0
        s = list(s)
        while r < n:
            while r < n and s[r] != ' ':
                r += 1
            # r: right after word
            rev(s, l, r-1)
            # because only 1 space between words
            r += 1
            l = r

        return ''.join(s)


sl = Solution()
s = "God Ding"
print(sl.reverseWords(s))
