'''
https://leetcode.com/explore/learn/card/recursion-ii/507/beyond-recursion/2905/
Leetcode explore Recursion II: Conclusion
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
'''


from typing import List

MP = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:

    def letterCombinations(self, digits: str) -> List[str]:
        def bt_archit91_a(i, path, res):
            """
            XXX: This is the right way!
            Your runtime beats 96.76 % of python3 submissions.

            https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/1148252/Short-and-Easy-Solutions-or-Multiple-Approaches-Explained-or-Beats-100
            Lets consider digits = "253"
            We would form the combinations one-by-one as follows -

            1.                                                                                   [""]
                                         ___________________________________________________________________________________________________________________
                                        /     								        		      |    								        		        \
            2.[                        "a"                                                       "b"                                                         "c"  ]
                       __________________________________                       ___________________________________                        ____________________________________
                      /      	        |                 \                     /     	          |                 \                      /     	          |                 \
            3.[     "aj"               "ak"               "al"                "bj"               "bk"               "bl"                "cj"                "ck"                "cl"  ]
                 ___________        ___________        ___________         __________         __________          __________          __________          __________          __________
                /     |     \      /     |     \      /     |     \       /    |     \       /    |     \        /    |     \        /    |     \        /    |     \        /    |     \
            4["ajd"  "aje"  "ajf" "akd" "ake" "akf" "ald"  "ale" "alf"  "bjd"  "bje"  "bjf" "bjd"  "bje"  "bjf" "bjd" "bje" "bjf"  "cjd"  "cje"  "cjf" "cjd"  "cje"  "cjf" "cjd" "cje" "cjf"  ]


            1. We are starting with empty array.
            2. We take the first digit from 'digits' and form all the possible combinations with it. 
            3. Now, the main thing you must notice is that, we are just extending the previous combination. We are taking  "a" from the previous combination and combining it with each letter mapped with digit 5, 
            then we take "b" from previous combination and again combine it with each letter mapped with digit 5 and repeat the same process for "c".
            4. Again, extend previous combination by taking from each previously formed combination and combining it with all the letters mapped with the digit under current iteration (3).
            """
            if i == len(digits):
                res.append(path[:])
                return
            for c in MP[digits[i]]:
                bt_archit91_a(i+1, path+c, res)

        def bt_fxr1(start_idx, path, res):
            """
            Runtime: 32 ms, faster than 68.63% of Python3 online submissions

            Although AC, this shows that I don't have clear understanding of backtracking: combination/subset vs permutation!
            """
            # BUG: This will include str that not valid, say '23' can generate 'd'
            #   because the for i in [start, len] can try next digit without filling previous digit, so path = ''+'d' = 'd'
            # if start_idx == len(digits):
            if len(path) == len(digits):
                # BUG: res.append(list(path)). Now I know why prefer path[:]
                #       because list will convert str to list of char!
                res.append(path[:])
                return

            for i in range(start_idx, len(digits)):
                # BUG: I don't clearly understand combination/subset vs permutation!
                #       This is not subset, since we have make choice for each digit! Therefore we can skip! So not using start_idx!
                #       In stead, we use simple i (as pos of digits)
                # candidates for cur i-th digit:
                for c in MP[digits[i]]:
                    # BUG: no need of visited, because each candidate will pick once only
                    # if c in visited:
                    #     continue
                    # visited.add(c)
                    bt_fxr1(i + 1, path+c, res)
                    # visited.remove(c)

        res = []
        if digits == '':
            return res
        # bt_fxr1(0, '', res)
        bt_archit91_a(0, '', res)
        return res


# print(Solution.choices('9'))
sl = Solution()
print(sl.letterCombinations('23'))
