class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            tempProd = curMax * n # just for purpose of calculating new minProd without replacement
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tempProd, curMin * n, n)
            result = max(result, curMax)

        return result
