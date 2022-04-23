"""
tag: Medium, Greedy, Logic
Lookback:
- I can't piecewise analysis ...
[ ] REDO
"""


class Solution:
    def minimumBuckets(self, street: str) -> int:
        def os_cn():
            """
            Runtime: 64 ms, faster than 79.82% of Python3 online submissions for Minimum Number of Buckets Required to Collect Rainwater from Houses.

            https://leetcode-cn.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/solution/cong-fang-wu-shou-ji-yu-shui-xu-yao-de-z-w2vj/
            """
            n = len(street)
            i, ans = 0, 0
            while i < n:
                if street[i] == "H":
                    if i + 1 < n and street[i + 1] == ".":
                        ans += 1
                        i += 2
                    elif i - 1 >= 0 and street[i - 1] == ".":
                        ans += 1
                    else:
                        return -1
                i += 1
            return ans

        return os_cn()

        """
        def fxr_BLOCKED():
            i = 0
            buckets = 0
            while i < len(street):
                if street[i] == 'H':
                    triple = street[i:i+3]
                    # case 1: .H.. , bucket left or right (so +1)
                    if triple == 'H..':
                        buckets += 1
                    # case 2: H.H, bucket at i+1 (so +1)
                    elif triple == 'H.H':
                        buckets += 1
                    # case 3: HH. , if i-1 = -1  => return -1, (ow +1)
                    # case 4: HHH. return -1
        """
