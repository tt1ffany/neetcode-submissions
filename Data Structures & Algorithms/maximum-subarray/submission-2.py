class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = nums[0]
        currentSum = 0

        for i in range(n):
            if currentSum < 0:
                currentSum = 0
            currentSum += nums[i]
            maxSum = max(maxSum, currentSum)

        return maxSum