'''
https://www.lintcode.com/problem/128/description
hash function is using 2 constant:
radix = 33, hash_size = large int (1e6?)
'''


class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        radix = 33
        hash_v = 0
        for c in key:
            hash_v = (hash_v * radix + ord(c)) % HASH_SIZE
        return hash_v
