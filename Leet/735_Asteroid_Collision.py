'''

✅ GOOD Stack
Amazon Top50
tag: Medium

Lookback:
+ collision must occur right->left, so use Stack
+ coding detail logic
'''

from typing import List


class Solution:

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        def os():
            """
            Runtime: 130 ms, faster than 41.27% of Python3 online submissions for Asteroid Collision.

            REF: https://leetcode.com/problems/asteroid-collision/discuss/109666/Python-O(n)-Stack-based-with-explanation
            XXX: for/while ... else
            T: O(N)
            """
            ans = []
            for new in asteroids:
                while ans and new < 0 < ans[-1]:
                    if ans[-1] < -new:
                        ans.pop()
                        continue
                    elif ans[-1] == -new:
                        ans.pop()
                        break
                    else:  # top > |new|
                        break

                # execute this when `while` failed: https://www.pythontutorial.net/python-basics/python-while-else/
                else:
                    ans.append(new)
            return ans

        return os()


sl = Solution()
# asteroids = [5, 10, -5]
# asteroids = [8, -8]
# asteroids = [10, 2, -5]
asteroids = [-1, 2, 3, 4, -5]
print(sl.asteroidCollision(asteroids))