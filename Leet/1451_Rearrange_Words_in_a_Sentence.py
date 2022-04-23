"""
tag: medium, sort
Lookback:
- Python uses Timsort, which is STABLE sort.
- Timsort has been Python's standard sorting algorithm since version 2.3

"""


class Solution:
    def arrangeWords(self, text: str) -> str:
        def ye15():
            # Runtime: 61 ms, faster than 59.32% of Python3 online submissions for Rearrange Words in a Sentence.
            return " ".join(sorted(text.split(), key=len)).capitalize()

        def fxr():
            """
            Runtime: 99 ms, faster than 15.75% of Python3 online submissions for Rearrange Words in a Sentence.

            T: O(nlogn), M: O(2n + n)
            """
            words = text.split()
            lwi = [(w, i) for i, w in enumerate(words)]
            lwi.sort(key=lambda x: (len(x[0]), x[1]))
            res = [w.lower() for w, i in lwi]
            return " ".join(res).capitalize()

        return fxr()


sl = Solution()
text = "Leetcode is cool"
print(sl.arrangeWords(text))
