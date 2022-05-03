"""
Common snippets for Str problems
- Palindrome
- Parentheses
- Substr
- Groupby
"""


from itertools import groupby


def minAddToMakeValid(s):
    """
    301, 921, 1249, 2116
    Runtime: 43 ms, faster than 48.43% of Python3 online submissions for Minimum Add to Make Parentheses Valid.

    https://www.youtube.com/watch?v=Sv5Xb-kfDok
    Q: How did Huifeng Guan analyze the Greedy correctness?
    A: Use concrete example: s = (()))((

    Stack: (**)
    Greedy:  count-> # un-matched left '('

    (( ...       count = 2
    (() ...      count = 1
    (()) ...     count = 0
    (())) ...    count = -1 => count = 0   (by +1 left)
    (()))( ...   count = 1
    (()))((      count = 2 => count = 0    (by +2 right)

    """
    count, ret = 0, 0
    for c in s:
        if c == "(":
            count += 1
        else:
            count -= 1
        if count == -1:
            ret += 1
            count = 0
    ret += count
    return ret


def validPalindrome(s):
    # 680: 2ptr + palindrome check
    return s == s[::-1]


def rle_groupby(s):
    # 809, 914, 830
    l, r = 0, 0
    res = []
    while l < len(s):
        res.append(s[l])
        while r < len(s) and s[l] == s[r]:
            r += 1
        # s[l] != s[r] or r = len(s)
        res.append(r - l)
        l = r
    return res


def os_groupby(s):
    for k, grp in groupby(s):
        print(k, list(grp))


def check_nice_str(s):
    # 1763
    return set(s) == set(s.swapcase())


def all_substr(s):
    def method2():
        # used in 1763
        res = []
        for r in range(len(s)):
            for l in range(r):
                res.append(s[l : r + 1])
        return res

    def method1():
        res = []
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                res.append(s[i:j])
        return res
