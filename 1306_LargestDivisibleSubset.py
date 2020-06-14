class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [[num] for num in nums]

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0 and len(dp[i]) >= len(dp[j]):
                    dp[j] = dp[i] + [nums[j]]

        dp.sort(key=len)

        return dp and dp[-1]
