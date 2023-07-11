"""
Amazon tag (easy)
"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        Runtime: 45 ms, faster than 33.10% of Python3 online submissions for Reorder Data in Log Files.

        T: O(MNlogN), M: max len of single log
        """
        digits = []
        letters = []
        # divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # sort by suffix
        # when suffix is tie, sort by identifier
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        result = letters + digits  # put digit logs after letter logs
        return result


sl = Solution()
print(
    sl.reorderLogFiles(
        logs=[
            "dig1 8 1 5 1",
            "let1 art can",
            "dig2 3 6",
            "let2 own kit dig",
            "let3 art zero",
        ]
    )
)

print(
    sl.reorderLogFiles(
        [
            "a1 9 2 3 1",
            "g1 act car",
            "zo4 4 7",
            "ab1 off key dog",
            "a8 act zoo",
            "a2 act car",
        ]
    )
)
