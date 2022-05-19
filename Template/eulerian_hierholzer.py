"""
TODO: how does this iterative algs works
Leetcode #332
https://github.com/stevenhalim/cpbook-code/blob/master/ch4/hierholzer.py
"""


def hierholzer(s, AL, N):
    ans = []
    idx = [0] * N
    st = [s]

    while st:
        u = st[-1]
        if idx[u] < len(AL[u]):
            st.append(AL[u][idx[u]])
            idx[u] += 1
        else:
            ans.append(u)
            st.pop()

    ans = ans[::-1]
    return ans
