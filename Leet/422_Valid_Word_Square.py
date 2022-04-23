'''
https://leetcode.com/problem-list/552y65ke/
LeetCode Curated Algo 170

'''


from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words:
            return True
        for i, w in enumerate(words):
            for j in range(len(w)):
                if j >= len(words):
                    return False
                if len(words[j]) <= i:
                    return False
                if w[j] != words[j][i]:
                    return False
        return True

        def zhugejunwei():
            """
            Your runtime beats 49.85 % of python3 submissions.

            https://leetcode.com/problems/valid-word-square/discuss/91167/Only-three-false-conditions%3A-too-short-too-long-letter-not-equal
            # only 3 false conditions: too short, too long, letter not match
            """
            if not words:
                return True
            for i, w in enumerate(words):
                for j in range(len(w)):
                    if j >= len(words):
                        return False
                    if len(words[j]) <= i:
                        return False
                    if w[j] != words[j][i]:
                        return False
            return True

        def fxr():
            """
            Runtime: 68 ms, faster than 73.16% of Python3 online submissions for Valid Word Square.

            AC in 2nd. Should clean assumptions (aka. edges happen) in mind
            """
            for i, word in enumerate(words):
                row = word
                col = ''
                for w in words[:len(word)]:
                    if i >= len(w):
                        return False
                    print(i, w)
                    col += w[i]
                if row != col:
                    return False
            return True

        # return fxr()
        return zhugejunwei()


sl = Solution()
# print(sl.validWordSquare(words=["abcd", "bnrt", "crmy", "dtye"]))
print(sl.validWordSquare(words=["abcd", "bnrt", "crm", "dt"]))
# print(sl.validWordSquare(["ball", "asee", "let", "lep"]))
