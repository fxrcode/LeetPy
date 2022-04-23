"""

https://leetcode.com/list?selectedList=5f4y8dwj
Must Do Easy Questions

"""


from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def fxr_brute():
            """
            Runtime: 168 ms, faster than 66.96% of Python3 online submissions for Find Words That Can Be Formed by Characters.

            AC in 1.
            T: O(N*L), M: O(N*L), L: average length
            """
            cnt = Counter(chars)
            ans = 0
            for word in words:
                cnt_word = Counter(word)
                for k, v in cnt_word.items():
                    if k not in cnt:
                        break
                    if v > cnt[k]:
                        break
                else:
                    # The else clause executes after the loop completes normally. book.pythontips.com
                    ans += len(word)
            return ans
        return fxr_brute()


sl = Solution()
print(sl.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))
print(sl.countCharacters(
    words=["hello", "world", "leetcode"], chars="welldonehoneyr"))
