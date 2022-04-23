'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List
"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """

        def post():
            """
            https://leetcode.com/problems/read-n-characters-given-read4/discuss/705183/Python-Simple-solution-with-explanation

            This is more clean clean
            """
            buf4 = ['']*4
            copied = 0
            while copied < n:
                got = read4(buf4)
                if got == 0:
                    break
                got = min(got, n-copied)
                # can copy short list to long list, no need ending for long, since it'll copy len(got)
                buf[copied:] = buf4[:got]
                copied += got
            return copied

        def fxr():
            '''
            Runtime: 28 ms, faster than 87.95% of Python3 online submissions for Read N Characters Given Read4.
            AC in 1.
            But took some time to handle edge case.
            '''
            buf4 = [0]*4

            chunks = n//4 + (1 if n % 4 else 0)
            actual = 0
            for c in range(chunks):
                l = read4(buf4)
                if l == 0:
                    break
                if c*4+l > n:
                    buf[c*4:n] = buf4[:n-c*4]
                    actual = n
                    break
                else:
                    buf[c*4:c*4+l] = buf4[:l]
                    actual += l
            return actual
