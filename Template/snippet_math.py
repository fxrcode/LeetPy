"""
Curated common snippet in Leetcode: Array
"""

# XXX: Must @staticmethod in class, ow, TypeError: str_to_int() takes 1 positional argument but 2 were given

from time import time


def rolling_hash(s):
    TODO: 718, etc


def str_to_int(si, k) -> int:
    """[summary]
    Convert str to integer (base k)
    from high to low
    '123' -> 123

    """
    v10 = 0
    for c in si:
        v10 = v10 * k + int(c)
    return v10


def toBaseB(v10, b):
    """
    https://leetcode.com/problems/sum-of-k-mirror-numbers/discuss/1589045/Python3-Try-all-base10-palindromes-with-base-k-with-explanation
    XXX: my 1st weekly contest
    """
    if v10 == 0:
        return "0"
    d = []
    while v10:
        d.append(str(v10 % b))
        v10 //= b
    return "".join(d[::-1])


def gcd(x, y):
    # Bezout: #1654
    # #914: reduce(gcd, freq)
    if y == 0:
        return x
    return gcd(y, x % y)


def prime_sieve(x):
    # get all primes < x
    if x < 2:
        return 0

    numbers = set()
    for i in range(2, int(x**0.5) + 1):
        if i not in numbers:
            for j in range(i * i, x, i):
                numbers.add(j)
    print(numbers)
    primes = []
    for v in range(2, x):
        if v not in numbers:
            primes.append(v)
    return primes


def trial_division2(n):
    # https://cp-algorithms.com/algebra/factorization.html
    dt = time()

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    d = 3
    while d**2 <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
    if n > 1:
        factors.append(n)
    print("time:", (time() - dt) * 1000)
    return factors


def prime_decompose(n):
    """
    https://leetcode.com/problems/largest-component-size-by-common-factor/solution/
    952. Largest Component Size by Common Factor
    """
    dt = time()
    factor = 2
    prime_factors = []
    while n >= factor**2:
        if n % factor == 0:
            prime_factors.append(factor)
            n //= factor
        else:
            factor += 1
    prime_factors.append(n)
    print("time:", (time() - dt) * 1000)

    return prime_factors


def sqrt_root(x):
    # no need to import math.sqrt
    return x**0.5


def bin_bits(x):
    # https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/
    return len(bin(x)) - 2


print(str_to_int("123", 10))
print(toBaseB(123, 2))
print(gcd(46, 12))
print(gcd(12, 46))
print(prime_sieve(16))
# print(trial_division2(288))
# print(prime_decompose(288))
print(bin_bits(25))
