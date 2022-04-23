"""
✅ GOOD OrderedDict
tag: Medium, OrderedDict
Lookback:
- similar to LRU
- 1st time use OrderedDict, next(iter(dict.values)), dict.popitem(last=False), dict.move_to_end(key)
"""


from collections import OrderedDict


class AuthenticationManager:
    """
    Amortized O(1)
    Runtime: 203 ms, faster than 82.18% of Python3 online submissions for Design Authentication Manager.

    """

    def __init__(self, timeToLive: int) -> None:
        self.ttl = timeToLive
        self.expiry = OrderedDict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.evict_expired(currentTime)
        self.expiry[tokenId] = self.ttl + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.evict_expired(currentTime)
        if tokenId in self.expiry:
            self.expiry.move_to_end(tokenId)
            self.expiry[tokenId] = self.ttl + currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.evict_expired(currentTime)
        return len(self.expiry)

    def evict_expired(self, currentTime: int) -> None:
        while self.expiry and next(iter(self.expiry.values())) <= currentTime:
            self.expiry.popitem(last=False)


class AuthenticationManager_bruteforce:
    """
    Runtime: 344 ms, faster than 48.85% of Python3 online submissions for Design Authentication Manager.
    https://leetcode.com/problems/design-authentication-manager/discuss/1118827/Clean-Python-with-explanation

    """

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            if self.tokens[tokenId] + self.ttl > currentTime:
                self.tokens[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for time in self.tokens.values():
            if time <= currentTime < time + self.ttl:
                cnt += 1
        return cnt


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
