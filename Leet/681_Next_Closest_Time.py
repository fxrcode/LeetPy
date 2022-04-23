"""
tag: Medium, Enum, Logic
Lookback:
- No idea in analysis, thegoldenboy is SO SMART
[ ] REDO
"""


class Solution:
    def nextClosestTime(self, time: str) -> str:
        def thegoldenboy():
            hh, mm = time.split(":")
            # generate all 2 digit values, there're at most 16 sorted value here
            nums = sorted(set(hh + mm))
            two_digit_vals = [a + b for a in nums for b in nums]

            # check if the next valid minute is within the hour
            i = two_digit_vals.index(mm)
            if i + 1 < len(two_digit_vals) and two_digit_vals[i + 1] < "60":
                return hh + ":" + two_digit_vals[i + 1]

            # check if the next valid hour is within the day
            i = two_digit_vals.index(hh)
            if i + 1 < len(two_digit_vals) and two_digit_vals[i + 1] < "24":
                return two_digit_vals[i + 1] + ":" + mm

            # return the earlist time of the next day
            return two_digit_vals[0] + ":" + two_digit_vals[0]

        return thegoldenboy()


sl = Solution()
print(sl.nextClosestTime(time="10:34"))
print(sl.nextClosestTime(time="11:59"))
print(sl.nextClosestTime(time="23:59"))
