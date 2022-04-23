'''
https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/
Leetcode Explore Array & String: Conclusion
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


'''


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Your runtime beats 33.63 % of python3 submissions.
        https://leetcode.com/problems/reverse-words-in-a-string/discuss/172258/Python-or-Two-Pointers-%2B-No-Cheating-tm
        """
        def rev(a, l, r):
            # inclusive l & r
            while l < r:
                a[l], a[r] = a[r], a[l]
                l += 1
                r -= 1

        def rev_words(arr):
            l, r = 0, 0
            while r < len(arr):
                while r < len(arr) and arr[r] != ' ':
                    r += 1
                # now r right after word
                rev(arr, l, r-1)
                r += 1
                l = r

        s = ' '.join(s.split())
        arr = list(s)
        rev_words(arr)
        rev(arr, 0, len(arr)-1)
        return ''.join(arr)

    '''
    def reverseWords_fxr_WRONG(self, s: str) -> str:
        # BUG: My 1st attempt, FAILED due to only 1 space allowed between words in return!
        s = list(s)

        def rev(s, l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        n = len(s)
        l, r = 0, n-1
        while l < r and s[l] == ' ':
            l += 1
        while r > l and s[r] == ' ':
            r -= 1
        if l == r:
            return ''

        i = l
        while i <= r:
            while s[i] == ' ':
                i += 1
            # s[i] is 1st char of word
            j = i
            while j <= r and s[j] != ' ':
                j += 1
            # j is right after word or j point to last word's last char
            # [i:j] is word
            rev(s, i, j-1)
            if j == r+1:
                break
            i = j
        rev(s, l, r)
        s = ''.join(s[l:r+1])
        print('['+s+']')
        return s
    '''


sl = Solution()
s = "  Bob    Loves  Alice   "
# s = "  Bob"
# s = "  Alice"
# s = "Google"
print(sl.reverseWords(s))
