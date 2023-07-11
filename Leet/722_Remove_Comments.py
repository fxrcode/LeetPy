"""
✅ GOOD FSM (prerequisite of XXX)
Kevin

tag: medium, str
Lookback
- If not self-similar, refine granuality in iteration!
- Crystal clear in FSM design, then impl. Not the other around === MESSY
"""

from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        def kaygusuz():
            """
            Runtime: 48 ms, faster than 41.28% of Python3 online submissions for Remove Comments.

            https://leetcode.com/problems/remove-comments/discuss/323278/Clean-and-readable-Python-solution-using-2-state-FSM
            XXX: Clean and readable Python solution using 2-state FSM

            ![FSM diagram](../pics/722-fsm.png)
            """
            NORMAL = 1
            MLCOMMENT = 2
            res = []
            st = NORMAL

            buf = ""
            for line in source:
                i = 0
                while i < len(line):
                    if st == NORMAL:
                        if line[i : i + 2] == "//":
                            break
                        elif line[i : i + 2] == "/*":
                            st = MLCOMMENT
                            i += 2
                        else:
                            buf += line[i]
                            i += 1
                    elif st == MLCOMMENT:
                        if line[i : i + 2] == "*/":
                            st = NORMAL
                            i += 2
                        else:
                            i += 1

                # handle buf
                if st == MLCOMMENT:
                    pass
                else:
                    if buf:
                        res.append(buf)
                        buf = ""

            return res

        """
        # !WA: Don't know how to handle /*..*/ /*..*/ /*..*/, tried recursion, but failed
        
        def fxr_WA():
            st = 0
            res = []

            def addline(line: str, join=False):
                if line:
                    if join:
                        res[-1] += (line)
                    else:
                        res.append(line)

            for s in source:
                if st == 0:
                    lc, bc = s.find('//'), s.find('/*')
                    if lc == -1 and bc == -1:
                        # no comment, noops
                        addline(s)
                    elif lc == -1 and bc != -1:
                        st = 1
                        # remove till we find */
                        bbc = s.find('*/', bc + 2)
                        if bbc == -1:
                            # remove the rest of line, stay in st=1
                            addline(s[:bc])
                        else:
                            # remove till */
                            addline(s[:bc] + s[bbc + 2:])
                            st = 0
                    elif lc != -1 and bc == -1:
                        st = 2
                        # remove till end of line
                        addline(s[:lc])
                        st = 0
                    else:  # bot lc & bc found
                        if lc < bc:
                            addline(s[:lc])
                        else:
                            st = 1
                            # remove till we find */
                            bbc = s.find('*/', bc + 2)
                            if bbc == -1:
                                # remove the rest of line, stay in st=1
                                addline(s[:bc])
                            else:
                                # remove till */
                                addline(s[:bc] + s[bbc + 2:])
                                st = 0
                elif st == 1:  # given /*
                    bc = s.find('*/')
                    if bc != -1:
                        st = 0
                        # remove till bc+2
                        addline(s[bc + 2:], True)
                    else:
                        # remove whole line, so do nothing
                        pass

            return res
        """

        # return fxr()
        return kaygusuz()


sl = Solution()
source = [
    "/*Test program */",
    "int main()",
    "{ ",
    "  // variable declaration ",
    "int a, b, c;",
    "/* This is a test",
    "   multiline  ",
    "   comment for ",
    "   testing */",
    "a = b + c;",
    "}",
]
# source = ["a/*comment", "line", "more_comment*/b"]
source = [
    "struct Node{",
    "    /*/ declare members;/**/",
    "    int size;",
    "    /**/int val;",
    "};",
]
source = [
    "main() {",
    "  Node* p;",
    "  /* declare a Node",
    "  /*float f = 2.0",
    "   p->val = f;",
    "   /**/",
    "   p->val = 1;",
    "   //*/ cout << success;*/",
    "}",
    " ",
]
# source = ["   //*/ cout << success;*/"]
# source = ["a/*/b//*c", "blank", "d/*/e*//f"]
source = ["ni hao /*x1//*/ ab/**/cd ef/**//**/gh"]
print(sl.removeComments(source))
