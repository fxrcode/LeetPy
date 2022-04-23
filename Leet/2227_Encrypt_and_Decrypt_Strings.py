"""
tag: Hard, Hash
Lookback:
- Please understand the problem before coding!
- I got TLE, b/c I sticked w/ #1087 using backtrack, Trie didn't help still TLE.
- WC 286, Q4. So close to AK...
"""


from collections import Counter, defaultdict
from typing import List


class Encrypter:
    """
    Runtime: 412 ms, faster than 81.25% of Python3 online submissions for Encrypt and Decrypt Strings.

    """

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.d = {k: v for k, v in zip(keys, values)}
        # (2) The second hashmap self.dictmap is a Counter - we encrypt each word in the given dictionary and use the
        # encrypted string as the key and increase the counter by 1. As such, we have solved the duplication problem
        # of the decrypt() method.
        self.freq = Counter()
        for word in dictionary:
            self.freq[self.encrypt(word)] += 1

    def encrypt(self, word1: str) -> str:
        return "".join([self.d[c] for c in word1])

    def decrypt(self, word2: str) -> int:
        return self.freq[word2]


"""
class Encrypter_TLE:
    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.mp = {k: v for k, v in zip(keys, values)}
        self.rev = defaultdict(list)
        for v, k in zip(values, keys):
            self.rev[v].append(k)
        self.d = set(dictionary)
        self.root = {}

        def insert(s):
            cur = self.root
            for c in s:
                cur = cur.setdefault(c, {})
            cur["#"] = s

        for s in dictionary:
            insert(s)

    def encrypt(self, word1: str) -> str:
        res = []
        for w in word1:
            res.append(self.mp[w])
        return "".join(res)

    def decrypt(self, word2: str) -> int:
        def find(s):
            cur = self.root
            for c in s:
                if c not in cur:
                    return False
                cur = cur[c]
            return True

        q = []
        for i in range(0, len(word2), 2):
            q.append(word2[i : i + 2])

        def bt(i, path):
            if i == len(q):
                p = "".join(path)
                if p in self.d:
                    nonlocal res
                    res += 1
                return
            for k in self.rev[q[i]]:
                pre = "".join(path + [k])
                if not find(pre):
                    continue
                bt(i + 1, path + [k])

        res = 0
        bt(0, [])
        return res
"""

codec = Encrypter(keys=["a", "b", "c", "d"], values=["ei", "zf", "ei", "am"], dictionary=["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"])
print(codec.encrypt("abcd"))
print(codec.decrypt("eizfeiam"))
