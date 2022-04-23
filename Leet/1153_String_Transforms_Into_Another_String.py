'''
💡 INSIGHT (analysis)
✅ GOOD Graph

Google tag

Weekly Special (Dec W4)
'''
from collections import defaultdict


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        def os():
            """
            Runtime: 32 ms, faster than 58.27% of Python3 online submissions for String Transforms Into Another String.

            https://leetcode.com/problems/string-transforms-into-another-string/discuss/553209/Solution-with-a-narrative-of-how-you-might-derive-this-yourself-in-real-life

            let's continue testing the hypothesis on the particular predicates:
            we introduce a cycle to the valid case above to consider the cycle predicate of our hypothesis
            i.e. aabcc -> ccdaa (has cycle a->c->a)
            #                c -> z       a -> c      b -> d       z -> a
            # a a b c c -> a a b z z -> c c b z z -> c c d z z -> c c d a a
            # c c d a a

            hence, **cycles** are fine as long as there are characters available to use as temporary variables
            Now we can propose a theorem
            Theorem: transformation is possible iff:
               * character edges form a linear directed graph (no forks)
               * there are characters in the lexicon not accounted for in the strings that can be used as temporary variables
            """
            if str1 == str2:
                return True

            edges = dict()
            for c1, c2 in zip(str1, str2):
                if c1 not in edges:
                    edges[c1] = c2
                else:
                    if edges[c1] != c2:
                        return False

            # We built edges with no fork, but cycle may exist. So we see if we can use extra letter from vocabulary to break cycle
            return len(set(str1)) < 26 or len(set(str2)) < 26

        def fxr_WA():
            """
            https://www.youtube.com/watch?v=WBE1mQHsMI0
            XXX: Nice explain by Tony Teaches
                re-model as graph,

            say the whole volcabulary is {a,b,c}
            case 1: s1 = 'ab', s2 = 'bc'
            1st conv: ab->db
            2nd conv: db->dc
            3rd conv: dc -> bc (DONE)

            case 2: s1 = 'abc', s2 = 'cba'
            1st conversion: abc->cbc
            2nd conversion: cbc->aba->X (notice that 1-conversion convert ALL occurence)
            """
            l = len(str1)
            n1 = [-1] * l
            d1 = defaultdict(lambda: -1)
            n = 0
            for i, c in enumerate(str1):
                if d1[c] == -1:
                    d1[c] = n
                    n += 1
                n1[i] = d1[c]

            n2 = [-1] * l
            d2 = defaultdict(lambda: -1)
            n = 0
            for i, c in enumerate(str2):
                if d2[c] == -1:
                    d2[c] = n
                    n += 1
                n2[i] = d2[c]

            print(n1, n2)

            d = defaultdict(lambda: -1)
            for i in range(l):
                a = n1[i]
                if d[a] == -1:
                    d[a] = n2[i]
                elif d[a] != n2[i]:
                    return False
            return True

        return os()


sl = Solution()
print(sl.canConvert(str1="aabcc", str2="ccdee"))
print(sl.canConvert(str1="leetcode", str2="codeleet"))
print(sl.canConvert("xyzaa", "bbbcb"))
print(sl.canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"))
