# TLE
def getPermutation(n, k):
    permutations = []

    def toString(l):
        return "".join(str(i) for i in l)

    def permute(a, l, r):
        if l == r:
            permutations.append(toString(a))
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                permute(a, l + 1, r)
                a[l], a[i] = a[i], a[l]
        return permutations

    arr = [i + 1 for i in range(n)]
    n = len(arr)
    answer = permute(arr, 0, n - 1)
    answer.sort()

    return answer[k - 1]


# Help from Discuss
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = list(range(1, n + 1))
        k -= 1  # to divide into groups
        res = ""

        def fact(n):
            if n == 0 or n == 1:
                return 1
            return n * fact(n - 1)

        while n:
            n -= 1

            index, k = divmod(k, fact(n))
            res += str(arr.pop(index))

        return res
