class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for cur in range(len(nums)):
            # Look at every element before the current
            for prev in range(cur):
                if nums[prev] < nums[cur]:
                    newIS = dp[prev] + 1
                    # Keep LIS ending at current element
                    dp[cur] = max(dp[cur], newIS)
        
        return max(dp)