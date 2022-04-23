'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        def os():
            """
            OS is more clean!
            """
            i1, i2 = -1, -1
            ans = len(wordsDict)
            for i, w in enumerate(wordsDict):
                if w == word1:
                    i1 = i
                elif w == word2:
                    i2 = i
                if i1 != -1 and i2 != -1:
                    ans = min(ans, abs(i1-i2))
            return ans

        def fxr():
            """
            Runtime: 60 ms, faster than 94.19% of Python3 online submissions for Shortest Word Distance.

            AC in 1.
            XXX: Carefully do variable None testing!!!
            """
            p1, p2 = None, None
            ret = len(wordsDict)
            for i, w in enumerate(wordsDict):
                if w == word1:
                    p1 = i
                    if p2 is not None:
                        ret = min(ret, abs(p2-p1))
                if w == word2:
                    p2 = i
                    if p1 is not None:
                        # BUG: if p1:
                        # XXX: https://stackoverflow.com/questions/3965104/not-none-test-in-python
                        ret = min(ret, abs(p2-p1))
            return ret

        # return fxr()
        return os()


sl = Solution()
print(sl.shortestDistance(wordsDict=[
      "practice", "makes", "perfect", "coding", "makes"], word1="coding", word2="practice"))
print(sl.shortestDistance(wordsDict=[
      "practice", "makes", "perfect", "coding", "makes"], word1="makes", word2="coding"))
