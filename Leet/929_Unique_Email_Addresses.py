"""
tag: easy, str
Lookback
- use split vs find vs index
"""

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def fxr():
            """
            Runtime: 86 ms, faster than 41.98% of Python3 online submissions for Unique Email Addresses.

            """
            dif = set()
            for e in emails:
                loc, dom = e.split("@")
                # p = loc.find("+")
                # if p == -1:
                #     p = len(loc)
                l = loc.split("+")[0].replace(".", "")
                dif.add(l + "@" + dom)
            return len(dif)

        return fxr()


sl = Solution()
emails = [
    "test.email+alex@leetcode.com",
    "test.e.mail+bob.cathy@leetcode.com",
    "testemail+david@lee.tcode.com",
]
print(sl.numUniqueEmails(emails))
