class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        nums.sort()

        if nums[-1] != len(nums):
            missing = len(nums)

        for i in range(0, len(nums)-1):
            if nums[i+1] not in nums:
                missing = nums[i]
            if nums[i] + 1 != nums[i+1]:
                missing = nums[i] + 1

        return missing
