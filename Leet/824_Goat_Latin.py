'''
FB tag (6mo)
'''


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        """
        learn lee215's good coding style
        """
        vowal = set('aeiouAEIOU')

        def latin(w, i):
            if w[0] not in vowal:
                w = w[1:] + w[0]
            return w + 'ma' + 'a' * (i+1)
        return ' '.join(latin(w, i) for i, w in enumerate(sentence.split()))


sl = Solution()
print(sl.toGoatLatin(sentence="I speak Goat Latin"))
