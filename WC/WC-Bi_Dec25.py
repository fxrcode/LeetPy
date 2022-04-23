from typing import List
from functools import cache
from collections import defaultdict


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        mx = 0
        for s in sentences:
            mx = max(mx, len(s.split()))
        return mx

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        ["ju","fzjnm","x","e","zpmcz","h","q"]
        [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
        ["f","hveml","cpivl","d"]

        ["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"]
        [["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]]
        ["wi","otr","wbjr","fzr","xgp"]

        """
        ans = []
        sup = set(supplies)
        rec = set(recipes)
        r2i = {recipes[i]: set(ingredients[i]) for i in range(len(recipes))}
        d = [0]

        color = defaultdict(int)

        @cache
        def val(r):
            # d[0] += 1
            # if d[0] == 10:
            #     return False
            color[r] = 1
            print('\t:', r)
            for ing in r2i[r]:
                if ing in sup:
                    continue
                elif ing in r2i:
                    if color[ing] == 1:
                        return False
                    if not val(ing):
                        return False
                else:
                    return False
            color[r] = 2

            return True

        for r in rec:
            d[0] = 0
            print(r)
            if val(r):
                ans.append(r)
        return ans

        # for i in range(len(recipes)):
        #     ok = True
        #     for j in range(len(ingredients[i])):
        #         ing = ingredients[i][j]
        #         if not (ing in rec or ing in sup):
        #             ok = False
        #             break
        #     if ok:
        #         ans.append(recipes[i])

    def canBeValid(self, s: str, locked: str) -> bool:
        """
        no idea
        """
        pass

    def abbreviateProduct(self, left: int, right: int) -> str:
        '''
        TLE:
        '''
        prod = 1
        tens = 0
        for v in range(left, right+1):
            prod *= v
            while prod and prod % 10 == 0:
                prod //= 10
                tens += 1

        sp = str(prod)
        if len(sp) <= 10:
            return sp + 'e' + str(tens)
        else:
            f5 = sp[:5]
            l5 = sp[-5:]
            return str(f5) + '...' + str(l5) + 'e' + str(tens)


sl = Solution()
# ans = sl.findAllRecipes(["ju", "fzjnm", "x", "e", "zpmcz", "h", "q"],
#                         [["d"], ["hveml", "f", "cpivl"], ["cpivl", "zpmcz", "h", "e", "fzjnm", "ju"], ["cpivl", "hveml", "zpmcz", "ju", "h"], [
#                             "h", "fzjnm", "e", "q", "x"], ["d", "hveml", "cpivl", "q", "zpmcz", "ju", "e", "x"], ["f", "hveml", "cpivl"]],
#                         ["f", "hveml", "cpivl", "d"])
ans = sl.abbreviateProduct(left=410, right=70000)
print(ans)
