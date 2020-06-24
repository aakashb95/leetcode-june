# Counter approach, Naive, very easy. O(n) space, O(n) time
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for k, v in d.items():
            if v == 1:
                return k


# Bitwise, O(1) space - sum(1)%3 approach
class Solution:
    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            rem = count % 3
            if i == 31 and rem:
                res -= 1 << 31
            else:
                res |= rem * (1 << i)
        return res


# Bitwise using XOR:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1, x0 = 0, 0
        for num in nums:
            x1, x0 = x1 ^ (x0 & num), x0 ^ num
            mask = ~(x1 & x0)
            x1, x0 = x1 & mask, x0 & mask
        return x0
