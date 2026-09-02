class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # if middle element is greater than right element, then the minimum must be on the right
                left = mid + 1
            # if middle element is less than or equal to right element, then the mid could be minimum or it's on the left
            else:
                right = mid

        return nums[left] 