class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums) # start with max value (avoids index out of range)

        for i in range(len(nums)):
            missing = missing ^ (i ^ nums[i])

        return missing