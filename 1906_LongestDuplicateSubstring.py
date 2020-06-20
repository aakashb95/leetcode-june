from collections import defaultdict


def RabinKarp(text, M):
    if M == 0:
        return True
    q = (1 << 31) - 1  # 2 ** 31 - 1
    h, t, d = (1 << (8 * M - 8)) % q, 0, 256

    dic = defaultdict(list)

    for i in range(M):
        t = (d * t + ord(text[i])) % q

    dic[t].append(i - M + 1)
    for i in range(len(text) - M):
        t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
        for j in dic[t]:
            if text[i + 1 : i + M + 1] == text[j : j + M]:
                return (True, text[j : j + M])
        dic[t].append(i + 1)
    return (False, "")


def longestDupSubstring(S):
    beg, end = 0, len(S)
    Found = ""
    while beg + 1 < end:
        mid = (beg + end) // 2
        isFound, candidate = RabinKarp(S, mid)
        if isFound:
            beg, Found = mid, candidate
        else:
            end = mid
    return Found


# s = "banana"
# print(longestDupSubstring(s))

# Fastest submission:
from functools import reduce


class Solution(object):
    def longestDupSubstring(self, S):
        A = [ord(c) - ord("a") for c in S]
        mod = 2 ** 32

        def test(L):
            p = pow(26, L, mod)
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
            seen = {cur}
            for i in range(L, len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)

        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res : res + lo]
