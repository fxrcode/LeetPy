"""
tag: medium, sort, logic
Lookback:

"""

from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        def fxr():
            """
            Runtime: 84 ms, faster than 86.19% of Python3 online submissions for Rank Teams by Votes.

            """
            ranks = {t: [0] * 26 + [t] for t in votes[0]}
            print(ranks)
            for vote in votes:
                for r, v in enumerate(vote):
                    ranks[v][r] -= 1
            ranks_list = list(ranks.values())
            ranks_list.sort()
            print(ranks_list)
            res = []
            for r in ranks_list:
                res.append(r[-1])
            return "".join(res)

        return fxr()


sl = Solution()
print(sl.rankTeams(votes=["ABC", "ACB", "ABC", "ACB", "ACB"]))
