class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set(nums)
        n = len(nums) + 1
        missing = 0

        for i in range(0, n):
            if i not in numSet:
                missing = i

        return missing