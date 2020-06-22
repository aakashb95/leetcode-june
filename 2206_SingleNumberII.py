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


# Bitwise, O(1) space:
