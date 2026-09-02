class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            # if target found
            if nums[mid] == target:
                return mid
                
            # if left side sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    # if in range search left
                    right = mid - 1
                else:
                    # if not, then search right
                    left = mid + 1
                    
            # if right side sorted
            else:
                if nums[mid] < target <= nums[right]:
                    # if in range search right
                    left = mid + 1
                else:
                    # if not, then search left
                    right = mid - 1

        # if not in array, then return -1
        return -1
