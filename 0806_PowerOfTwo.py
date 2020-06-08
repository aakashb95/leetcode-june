# Powers of 2 in binary have only one '1'.
# 4 = 100, 8 = 1000 ...
# convert decimal to binary and if count(1) is 1, it is a power of 2.
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def d2b(a):
            l = []
            if a == 0 or a < 0:
                return [0]
            while a != 1:
                r = a % 2
                a = a // 2
                l.append(r)
            l.append(1)
            return l[::-1]

        binary = d2b(n)
        return True if binary.count(1) == 1 else False
