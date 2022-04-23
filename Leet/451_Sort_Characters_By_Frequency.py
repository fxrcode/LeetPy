'''
✅ GOOD Bucket Sort
FB tag (Medium)
'''
from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        def os_bucket():
            """
            Runtime: 60 ms, faster than 45.40% of Python3 online submissions for Sort Characters By Frequency.

            T: O(N)
            """
            cnt = Counter(s)
            max_freq = max(cnt.values())

            # Bucket sort for the chars by freq
            buckets = defaultdict(list)
            for c, i in cnt.items():
                buckets[i].append(c)

            sb = []
            for b_size in range(max_freq, 0, -1):
                if b_size not in buckets:
                    continue
                for c in buckets[b_size]:
                    sb.append(c * b_size)
            return ''.join(sb)

        def os_mostcommon():
            """
            Runtime: 49 ms, faster than 62.58% of Python3 online submissions for Sort Characters By Frequency.

            T: O(NlogN)
            """
            cnt = Counter(s)
            sb = []
            for c, f in cnt.most_common():
                sb.append(c * f)
            return ''.join(sb)

        def fxr():
            """
            Runtime: 40 ms, faster than 84.53% of Python3 online submissions for Sort Characters By Frequency.

            https://stackoverflow.com/questions/44076269/sort-counter-by-frequency-then-alphabetically-in-python
            """
            cnt = Counter(s)
            ans = []
            for k, v in sorted(cnt.items(), key=lambda cf: (-cf[1], cf[0])):
                ans += [k] * v
            return ''.join(ans)

        fxr()


sl = Solution()
print(sl.frequencySort(s='tree'))