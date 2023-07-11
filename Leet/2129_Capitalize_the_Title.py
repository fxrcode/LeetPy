class Solution:
    def capitalizeTitle(self, title: str) -> str:
        def fxr():
            """
            Runtime: 28 ms, faster than 100.00% of Python3 online submissions for Capitalize the Title.

            T: O(N)
            """
            words = title.split()
            res = []
            for w in words:
                if len(w) <= 2:
                    res.append(w.lower())
                else:
                    res.append(w.capitalize())
            return " ".join(res)
