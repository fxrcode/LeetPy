from typing import List


def addSpaces(s, spaces):
    ans = []
    spaces.reverse()
    print(spaces)
    for i, c in enumerate(s):
        if spaces and i == spaces[-1]:
            ans.append(' ')
            spaces.pop()
        ans.append(c)
    return ''.join(ans)


# print(addSpaces(s="EnjoyYourCoffee", spaces=[5, 9]))


def getDescentPeriods(self, prices: List[int]) -> int:
    cnt = 0
    period = 1
    i = 1
    def f(n): return n*(n+1)//2
    while i < len(prices):
        if prices[i-1] == prices[i]+1:
            period += 1
        else:
            cnt += f(period)
            period = 1
        i += 1

    return cnt + f(period)


def minOperations(nums: List[int], s, k) -> int:
    """
    WA!
    """
    cnt = 0
    prev = nums[s]
    for i in range(s+k, len(nums), k):
        cur = nums[i]
        if cur < prev:
            prev = prev
            cnt += 1
            print(i, prev,)

        else:
            prev = cur
    return cnt


def kIncreasing(arr: List[int], k: int) -> int:
    # cnt = 0
    # for i in range(k, len(arr)):
    #     if not arr[i-k] <= arr[i]:
    #         cnt += 1
    # return cnt
    cnt = 0
    for i in range(k):
        cnt += minOperations(arr, i, k)
        print('\t', i)
    return cnt


# should be 1 rather 3! So greedy is WA!
print(kIncreasing(arr=[1, 2, 1, 1, 1], k=1))
# arr=[12, 6, 12, 6, 14, 2, 13, 17, 3, 8, 11, 7, 4, 11, 18, 8, 8, 3], k=1))
