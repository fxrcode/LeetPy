"""
FB tag (medium)
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        def fxr():
            """
            Runtime: 35 ms, faster than 57.94% of Python3 online submissions for Simplify Path.

            T: O(N)
            """
            stk = []
            ps = path.split("/")
            for s in ps:
                if s == "." or s == "":
                    continue
                elif s == "..":
                    if stk:
                        stk.pop()
                else:
                    stk.append(s)
            return "/" + "/".join(stk)

        return fxr()


sl = Solution()
paths = ["/home/", "/../", "/home//foo/", "/a/./b/../../c/", "/a/../../b/../c//.//"]
for p in paths:
    print(sl.simplifyPath(p))
