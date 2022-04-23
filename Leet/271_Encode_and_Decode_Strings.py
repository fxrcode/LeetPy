"""
https://leetcode.com/list?selectedList=99566jt7
Neetcode Blind Curated 75
"""


class Codec:
    """
    Runtime: 64 ms, faster than 75.31% of Python3 online submissions for Encode and Decode Strings.

    REF: Neetcode, simple logic always easy to implement and handles edges
    """

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc = ''
        for s in strs:
            enc += str(len(s)) + '#' + s
        print(enc)
        return enc

    def decode(self, s: str) -> [str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

    '''
    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        XXX: failed for [""]
        """
        dec = []
        i = 0
        st = 0  # 0: digits, 1: delimiter(#), 2: str
        digits = ''
        while i < len(s):
            if st == 0 and s[i].isdigit():
                digits += s[i]
                i += 1
            elif st == 0 and s[i] == '#':
                digits = int(digits)
                st = 2
                i += 1
            # BUG: when length = 0, it'll not reach this state!
            #   so over-complicated (not KISS) === hard to debug/trickier in edge cases
            else:  # st == 1
                dec.append(s[i:i+digits])
                i += digits
                st = 0
                digits = ''
        return dec
    '''

    '''
    XXX: failed for ['a\t\nb']

    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        enc = '\t\n'.join(strs)
        return enc


    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        strs = s.split('\t\n')
        return strs
    '''


'''
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
'''
codec = Codec()
print(codec.decode(codec.encode(['a\t\nb'])))
print(codec.decode(codec.encode(["Hello", "World"])))
print(codec.decode(codec.encode([""])))
