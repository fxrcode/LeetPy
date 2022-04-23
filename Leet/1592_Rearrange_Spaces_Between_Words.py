"""
tag: easy, str, skills
Lookback:
- split(' ') doesn't work
- when div, think about div0
Similar:
- 68. Text Justification
"""


class Solution:
    def reorderSpaces(self, text: str) -> str:
        def leihao1313():
            """
            Runtime: 61 ms, faster than 10.31% of Python3 online submissions for Rearrange Spaces Between Words.

            https://leetcode.com/problems/rearrange-spaces-between-words/discuss/855335/JavaPython-3-6-liners-w-analysis./811262
            Neat and Pythonic, elegant
            """
            sp = text.count(" ")
            words = text.split()
            l = len(words) - 1
            x, y = divmod(sp, l) if l else (0, sp)
            return (" " * x).join(words) + (" " * y)

        return leihao1313()


sl = Solution()
print(f'[{sl.reorderSpaces(text="  this   is  a sentence ")}]')
print(f'[{sl.reorderSpaces(" practice   makes   perfect")}]')
print(f'[{sl.reorderSpaces("  a")}]')
