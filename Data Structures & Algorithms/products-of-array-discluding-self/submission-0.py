class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        # Already initialized with 1s, no need to set base case (also no need to    calculate the 1st prefix and last postfix)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            output[i] = prefix[i] * postfix[i]

        return output